---
layout: post
title:  "How to assert exception message in PyTest?"
excerpt_separator: <!--more-->
---

I kept forgetting how to assert exception messages in PyTest, so I finally checked [the docs](https://docs.pytest.org/en/stable/reference/reference.html#pytest-raises). Here's a reference snippet.

```python
import pytest

def broken() -> None:
    raise ValueError("something went wrong")

def test_broken() -> None:
    with pytest.raises(ValueError, match="went wrong"):
        broken()
```

> *That's it for today. Happy hacking! 🐍*
