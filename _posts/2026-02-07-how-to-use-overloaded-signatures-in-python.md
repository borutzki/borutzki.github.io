---
layout: post
title:  "How to use overloaded signatures in Python?"
excerpt_separator: <!--more-->
---

Sometimes a function takes multiple arguments of different types, and the return type depends on specific combinations of inputs. It's often easy to understand by reading code, but how do you tell the type checker that this is the case? This is where the `@overload` decorator from the `typing` module comes handy.

<!--more-->

## But what's the problem to solve?

Let's take the function below as an example.

```python
def generate_config(context: dict, action: Action) -> dict | list[str]:
    config = build_from_context(context, DEFAULT_TEMPLATE)
    if action == Action.DELETE:
        return build_list_of_xpaths(config)  # <- returns list[str]

    return config  # <- returns dict
```

It takes a template context and depending on `Action`, builds either `config` dictionary[^3] or a list of XPaths to be removed from some other config. The code here is pretty straightforward and let's assume it cannot be split into two functions because "some legacy dependencies".

Now let's say we need two proxy functions to generate specific types of configs somewhere else, like below.

```python
def function_that_needs_delete_config(context: dict) -> list[str]:
    return generate_config(context, action=Action.DELETE)


def function_that_needs_modify_config(context: dict) -> dict:
    return generate_config(context, action=Action.MODIFY)
```

Given the implementation of `generate_config`, we know that type hints are correct here. But let's see what happens if we run `mypy` on this code.

```bash
➜  code_samples git:(main) ✗ uv run mypy /Users/borutzki/Dev/code_samples/python/overload.py
python/overload.py:39: error: Incompatible return value type (got "dict[Any, Any] | list[str]", expected "list[str]")  [return-value]
python/overload.py:43: error: Incompatible return value type (got "dict[Any, Any] | list[str]", expected "dict[Any, Any]")  [return-value]
```

Yep, `mypy` sees two problems:

- in `function_that_needs_delete_config` it expects `list[str]` as return type, but `generate_config` can return either this or `dict`,
- in `function_that_needs_modify_config` it expects `dict` as return type, but `generate_config` can return either this or `list[str]`.

But I want to have neat type hints, and I know the issue doesn't actually exist, right? If only I could tell this stupid type checker what I know...

## `@overload`ing function signature

Thankfully, there's the `@overload`[^1] decorator in Python's `typing` module. Below is how to use it.

```python
from typing import overload, Literal, Any

# ... code omitted

@overload
def generate_config(context: dict, action: Literal[Action.MODIFY]) -> dict: ...
@overload
def generate_config(context: dict, action: Literal[Action.DELETE]) -> list[str]: ...
def generate_config(context: dict, action: Action) -> dict | list[str]:
    config = build_from_context(context, DEFAULT_TEMPLATE)
    if action == Action.DELETE:
        return build_list_of_xpaths(config)  # <- returns list[str]

    return config
```

What did I do? Created two additional signatures for the same function. One specifies result type for `MODIFY` action, the other - for `DELETE` action. Let's see output from `mypy` now.

```bash
➜  code_samples git:(main) ✗ uv run mypy /Users/borutzki/Dev/code_samples/python/overload.py
Success: no issues found in 1 source file
```

There's one catch here, though. Once you define at least one `@overload`, all valid call patterns must be described by overloads, because the implementation signature is ignored by type checkers. Otherwise, `mypy` will complain again.

As an example, let's add another proxy function, this time for `ADD`.

```python
def function_that_needs_add_config(context: dict) -> dict:
    return generate_config(context, action=Action.ADD)
```

Now, when I run `mypy` again, I get the following output:

```bash
➜  code_samples git:(main) ✗ uv run mypy /Users/borutzki/Dev/code_samples/python/overload.py
python/overload.py:47: error: No overload variant of "generate_config" matches argument types "dict[Any, Any]", "Action"  [call-overload]
python/overload.py:47: note: Possible overload variants:
python/overload.py:47: note:     def generate_config(context: dict[Any, Any], action: Literal[Action.MODIFY]) -> dict[Any, Any]
python/overload.py:47: note:     def generate_config(context: dict[Any, Any], action: Literal[Action.DELETE]) -> list[str]
```

which is a bit confusing, but points to a simple fact - that I am missing an overload variant for `Action.ADD`. I can add it, like below.

```python
@overload
def generate_config(context: dict, action: Literal[Action.ADD]) -> dict: ...
@overload
def generate_config(context: dict, action: Literal[Action.MODIFY]) -> dict: ...
@overload
def generate_config(context: dict, action: Literal[Action.DELETE]) -> list[str]: ...
def generate_config(context: dict, action: Action) -> dict | list[str]:
    config = build_from_context(context, DEFAULT_TEMPLATE)
    if action == Action.DELETE:
        return build_list_of_xpaths(config)  # <- returns list[str]

    return config  # <- returns dict
```

Afterwards, `mypy` once again has no complaints about my code.

```bash
➜  code_samples git:(main) ✗ uv run mypy /Users/borutzki/Dev/code_samples/python/overload.py
Success: no issues found in 1 source file
```

Since `Action.MODIFY` and `Action.ADD` will return the same type, I can reduce them to a single `@overload`.

```python
@overload
def generate_config(context: dict, action: Literal[Action.ADD, Action.MODIFY]) -> dict: ...
@overload
def generate_config(context: dict, action: Literal[Action.DELETE]) -> list[str]: ...
def generate_config(context: dict, action: Action) -> dict | list[str]:
    config = build_from_context(context, DEFAULT_TEMPLATE)
    if action == Action.DELETE:
        return build_list_of_xpaths(config)  # <- returns list[str]

    return config  # <- returns dict
```

## Couldn't it be done in some other way?

Let me analyse some other solutions that didn't solve the problem described here.

### Split the function into two

This would work if it was feasible in the code, and in the code from which the example emerged, it was not. The "legacy dependency" was real.

### `@functools.singledispatch`

I thought about using `@singledispatch`[^2] decorator for the function, but it has two limitations that make it infeasible.

First, it can only dispatch based on the *type* of first argument - so I would have to refactor all non-keyword-argument calls to the function. But even putting that aside, single-dispatch does not work with values - and in this case, `Action` is an enum, so its type is the same for all the arguments. Only value changes in signatures.

Technically, these problems could be solved by defining different type (class) for each action, but would it be really that readable?

### Disable type checking

It's tempting to disable type checker for this specific case, but even having all obvious downsides of it put aside, every call to the function would have to ignore the return type. And I would lose the information about incorrect expected return types. And IDE hints. Not nice.

## Summary

Maybe there are more approaches to the type-checking issue, but `@overload` was perfectly suited for the job. Hopefully, now you know how it can be used in similar cases in your own code.

> *That's it for today. Happy hacking! 🐍*

___

<br>  

[^1]: <https://typing.python.org/en/latest/spec/overload.html#overload-definitions>
[^2]: <https://docs.python.org/3/library/functools.html#functools.singledispatch>
[^3]: For brevity, I don't use specific type hints for the dict type.
