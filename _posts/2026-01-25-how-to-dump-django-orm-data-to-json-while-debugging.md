---
layout: post
title:  "How to dump Django ORM data to JSON while debugging?"
excerpt_separator: <!--more-->
---

Sometimes, I need to debug specific high-level tests by inspecting what gets created in the database as a side effect. I could use a debugger and poke around the Django ORM at a breakpoint - but quite often it's simply faster to dump the entire table to JSON, see what's there, and then apply fixes accordingly.

<!--more-->

Normally, to do that, `manage.py dumpdata` could be used. But since tests are ephemeral and don't necessarily preserve the database after they finish, a more scripted approach is often more convenient. This is where `serializers.serialize` comes in handy.

Here's how to use it:

```python
from django.core import serializers
from .models import Service

with open("dump.json", "w") as out:
    data = serializers.serialize("json", Service.objects.all())
    out.write(data)
```

and the result for my model is as shown below (auto-formatted for readability).

```json
[
    {
        "model": "blog.service",
        "pk": 1,
        "fields": {
            "name": "SERVICE_1",
            "service_type": "L3Connection",
            "created_at": "2026-01-25T11:17:48.880Z"
        }
    },
    {
        "model": "blog.service",
        "pk": 2,
        "fields": {
            "name": "SERVICE_2",
            "service_type": "L3Connection",
            "created_at": "2026-01-25T11:17:48.880Z"
        }
    }
]
```

This approach is neat because it doesn't prevent me from narrowing down the data. If I'm only interested in a subset of records, I can simply replace `all()` with `filter()` and dump exactly what I need.

To try it yourself inside a `TestCase`, feel free to copy-paste the snippet below:

```python
class DebugWithDumpTests(TestCase):
    def test_dump_to_json(self) -> None:
        _ = Service.objects.create(service_type="L3Connection", name="SERVICE_1")
        _ = Service.objects.create(service_type="L3Connection", name="SERVICE_2")

        with open("dump.json", "w") as out:
            data = serializers.serialize("json", Service.objects.all())
            out.write(data)
```

but remember not to commit the database dump to your repository!

> *That's it for today. Happy hacking! 🐍*
