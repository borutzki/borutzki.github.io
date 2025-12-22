---
layout: post
title:  "How to reuse Pydantic model_validator across multiple models without boilerplate code?"
excerpt_separator: <!--more-->
---

Recently I've been working with Pydantic models quite a lot. And I mean multiple models with multiple fields and validators. I noticed that in some cases, reusing validators in some smart way would reduce my codebase by even hundredths of lines of code. So I tried to come up with a solution for that problem...

![Code snippet]({{ site.baseurl }}/assets/img/snippets/2025-12-22-how-to-reuse-pydantic-model_validator-across-multiple-models-without-boilerplate-code.png)

<!--more-->

## Starting point

Let's say I need a model of a list with exactly three elements inside, enforced by model validator (yes, I know I don't need a model validator to do that, but I needed a simplistic example).

Let's call this model `SomeModel`. It would look something like this:

```python
class SomeModel(pydantic.RootModel):
    root: list[str]

    @pydantic.model_validator(mode="after")
    def length_should_be_3(self) -> "SomeModel":
        if len(self.root) == 3:
            return self
        raise ValueError
```

Now let's say that I need another model, that happens to perform exactly the same validation logic on similar field. Let's call it `SomeOtherModel`:

```python
class SomeOtherModel(pydantic.RootModel):
    root: list[str]

    @pydantic.model_validator(mode="after")
    def length_should_be_3(self) -> "SomeOtherModel":
        if len(self.root) == 3:
            return self
        raise ValueError
```

Copy-pasting the same logic in two models seem wasteful...

## Extracting validation logic

...so maybe let's try to extract validation logic to a separate function and reuse the logic by calling it within `model_validator`:

```python
def length_should_be_3(model: pydantic.RootModel) -> pydantic.RootModel:
    if len(model.root) == 3:
        return model
    raise ValueError


class SomeModel(pydantic.RootModel):
    root: list[str]

    @pydantic.model_validator(mode="after")
    def length_should_be_3(self) -> "SomeModel":
        return length_should_be_3(self)

class SomeOtherModel(pydantic.RootModel):
    root: list[str]

    @pydantic.model_validator(mode="after")
    def length_should_be_3(self) -> "SomeOtherModel":
        return length_should_be_3(self)
```

Looks a bit cleaner now, but notice that with each new model reusing the validation logic, I would have to copy-paste the same `length_should_be_3` method... Isn't there a better way?

## Extracting model_validator

Good news: Pydantic supports even more minimal way of reusing validators. But it's not mentioned in documentation - even though at some point it was, with example of `field_validator`.[^reuse]

Using this approach, we can do something like below.

```python
def length_should_be_3(model: pydantic.RootModel) -> pydantic.RootModel:
    if len(model.root) == 3:
        return model
    raise ValueError


class SomeModel(pydantic.RootModel):
    root: list[str]
    # Validators
    _validate_length = pydantic.model_validator(mode="after")(length_should_be_3)


class SomeOtherModel(pydantic.RootModel):
    root: list[str]
    # Validators
    _validate_length = pydantic.model_validator(mode="after")(length_should_be_3)
```

It's even more minimal than previous iteration, isn't it?

## But does this even work?

Of course! And you can test it yourself, using the following single-file module with definitions and tests. Feel free to copy-paste it and run with PyTest (but remember to install [`Pydantic`](https://docs.pydantic.dev/latest/install/) and [`PyTest`](https://docs.pytest.org/en/stable/getting-started.html#install-pytest) first!):

```python
# test_pydantic_reused_validators.py
"""This files showcases possibility to reuse model validators across Pydantic models.

It is based on the following page of Pydantic documentation:
https://docs.pydantic.dev/2.0/usage/validators/#reuse-validators

It is not specified in newer versions of Pydantic documentation, although it works flawlessly,
reducing boilerplate code being added to models.
"""

import pydantic
import pytest


def length_should_be_3(model: pydantic.RootModel) -> pydantic.RootModel:
    if len(model.root) == 3:
        return model
    raise ValueError


class SomeModel(pydantic.RootModel):
    root: list[str]

    # Validators
    _validate_length = pydantic.model_validator(mode="after")(length_should_be_3)


class SomeOtherModel(pydantic.RootModel):
    root: list[str]

    # Validators
    _validate_length = pydantic.model_validator(mode="after")(length_should_be_3)


@pytest.fixture(params=[SomeModel, SomeOtherModel])
def model(request: pytest.FixtureRequest) -> type[SomeModel] | type[SomeOtherModel]:
    return request.param


def test_both_models_can_be_built(
    model: type[SomeModel] | type[SomeOtherModel],
) -> None:
    # Given
    input_data = ["one", "two", "three"]
    # When
    result = model.model_validate(input_data)
    # Then
    assert isinstance(result, model)
    assert result.root == input_data


def test_both_models_fail_on_length_other_than_3(
    model: type[SomeModel] | type[SomeOtherModel],
) -> None:
    # Given
    input_data = ["one", "two", "three", "four"]
    # Then
    with pytest.raises(ValueError):
        model.model_validate(input_data)
```

## But doesn't the resulting code look a bit unreadable?

Yes, when taken out of context. But in a team that works with models on a daily basis, it shouldn't be a big deal. Sometimes the code can't be self-documenting, but hey - that's what comments are for.

My main concern is that such usage of validators could get deprecated by Pydantic at some point, especially given the lack of documentation. But it seems like what I do here is basically calling a parametrized decorator directly, as a function. So the risk might be real, but looks like not not that high in the end.

___

*That's it for today. Happy hacking! 🐍*

[^reuse]: <https://docs.pydantic.dev/2.0/usage/validators/#reuse-validators>
