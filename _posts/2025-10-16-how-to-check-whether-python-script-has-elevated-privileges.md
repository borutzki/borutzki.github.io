---
layout: post
title:  "How to check whether Python script has elevated privileges?"
excerpt_separator: <!--more-->
---

It may happen that a Python script needs `root` privileges on Linux / macOS or `admin` privileges on Windows to run properly. If it does not have them, there is no point in continuing. Let's see how to quickly check whether the current runtime has those privileges.

<!--more-->

## Linux / macOS

On Linux and macOS, this is straightforward. Elevated privileges are marked by user ID `0`, and Python built-in library `os` provides the function `getuid()`[^1] that returns current user ID. Hence, it's enough to just grab this value, compare it with `0` and return the result.

```python
import os

def is_root():
    """Return True if the current script is running on Linux/macOS with root privileges, otherwise False."""
    if os.name == "posix":
     # On Linux, user ID 0 indicates the root user
        return os.getuid() == 0
    else:
        return False
```

## Windows

On Windows, the approach with user ID will not work because Windows manages users in a different way. But the check for admin privileges is still relatively simple. It requires using C libraries available on Windows, which can be accessed through Python's built-in `ctypes` module.[^2]

In this case, the most elegant approach I found was to call `windll.shell32.IsUserAnAdmin`.[^3] I'm not saying it's the best solution, but it worked well when I needed it

```python
import ctypes
import os

def is_admin() -> bool:
    """Return True if the current script is running on Windows with admin privileges, otherwise False."""
    if os.name == "nt":
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    else:
        return False
```

>*That's it for today. Happy hacking! 🐍*

___

[^1]: <https://docs.python.org/3/library/os.html#os.getuid>
[^2]: <https://docs.python.org/3/library/ctypes.html>
[^3]: <https://learn.microsoft.com/en-us/windows/win32/api/shlobj_core/nf-shlobj_core-isuseranadmin>
