---
layout: post
title:  "How to parametrize exception testing in PyTest?"
excerpt_separator: <!--more-->
---

Sometimes it's useful to provide different input data and test different exceptions being raised. Not every exception deserves its own unit test, though. In such cases, I tend to combine PyTest's `parametrize` marker with Python's `contextlib.nullcontext` builtin.

<!--more-->

Here's how to use it:

```python
from contextlib import nullcontext as does_not_raise
import pytest
from pytest import raises


@pytest.mark.parametrize(
    ["x", "y", "expectation"],
    [
        (3, 2, does_not_raise()),
        (0, 1, does_not_raise()),
        (1, 0, raises(ZeroDivisionError)),
        (1, "0", raises(TypeError)),
    ],
)
def test_division(x, y, expectation):
    with expectation:
        x / y
```

The topic is actually described in the PyTest documentation[^1] and it was even raised as a question on StackOverflow[^2] but I still feel like it's pretty obscure knowledge.

I like to use this approach when testing exceptions is repetitive and I don't need to cover it thoroughly. Or when I need to get as close to 100% code coverage as possible.

The `nullcontext` usage may be a pretty obscure piece of knowledge, but with a small rename on import, its purpose becomes much clearer for anyone randomly encountering such unit test.

> *That's it for today. Happy hacking! 🐍*

___

[^1]: PyTest documentation: <https://docs.pytest.org/en/stable/example/parametrize.html#parametrizing-conditional-raising>
[^2]: Question from StackOverflow: <https://stackoverflow.com/a/68012715/18577080>
