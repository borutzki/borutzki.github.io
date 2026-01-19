---
layout: post
title:  "Why using [n] on a Django QuerySet can be unsafe?"
excerpt_separator: <!--more-->
---

What if I told you that the following way of taking the second object from a Django `QuerySet` might be unreliable and can lead to non-deterministic failures under some circumstances?

```python
second_service = Service.objects.filter(service_type="L3Connection")[1]
```

<!--more-->

Let me dig a bit into the topic in this brief note.

* Do not remove this line (it will not be displayed)
{:toc}

## Backstory

### Some info about setup

On a daily basis I work on a Django app based off Netbox. The app uses PostgreSQL instance as a database service (or container with it for testing purposes). The database schema is pretty complex, and the workflows I develop have multiple side effects impacting multiple database rows.

### The problem

So, the other day I was debugging one unit test, that was randomly failing in my project's CI pipeline. The culprit was the fact that the following line of code:

```python
second_service = Service.objects.filter(service_type="L3Connection").first()
```

was changed to this one:

```python
second_service = Service.objects.filter(service_type="L3Connection")[1]
```

because code behaviour changed.

The query aimed to retrieve an object created during the workflow. Two objects of the same type existed, but only one mattered for the test. Before the change, it was the first object; after, it was the second.

After the change in test code, unit tests started failing approximately 50% of the time.

But why?

## How does `.filter()` work?

Let's start by saying that reading Django documentation for `filter()` method[^1] is not really saying too much about default ordering:

> `filter(_*args_, _**kwargs_)`[¶](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.filter "Link to this definition")
>
> Returns a new `QuerySet` containing objects that match the given lookup parameters.
>
> The lookup parameters (`**kwargs`) should be in the format described in [Field lookups](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#id4) below. Multiple parameters are joined via `AND` in the underlying SQL statement.
>
> If you need to execute more complex queries (for example, queries with `OR` statements), you can use [`Q objects`](https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.Q "django.db.models.Q") (`*args`).

and it's not weird, because `QuerySet` depends on model configuration.

More information can be found in `django.db.models` documentation - specifically for `Options.ordering`.[^2] There's a yellow callout with ***Warning*** that says explicitly:

> **If a query doesn’t have an ordering specified, results are returned from the database in an unspecified order. A particular ordering is guaranteed only when ordering by a set of fields that uniquely identify each object in the results**. For example, if a `name` field isn’t unique, ordering by it won’t guarantee objects with the same name always appear in the same order.

This means that `filter()` returns objects in unspecified order, unless directly specified otherwise either in model definition or in the `filter` method itself.

But then, why it never failed when using `.first()`?

## How does `first()` pick the first element from the query?

Fortunately, the answer for this question is easier to find. It's right in the documentation of `first()`:[^3]

> Returns the first object matched by the queryset, or `None` if there is no matching object. **If the `QuerySet` has no ordering defined, then the queryset is automatically ordered by the primary key**. This can affect aggregation results as described in [Interaction with order_by()](https://docs.djangoproject.com/en/6.0/topics/db/aggregation/#aggregation-ordering-interaction).

So seemingly, `first()` adds an implicit `ORDER BY pk` to the `QuerySet`, which direct indexing (`[n]`) obviously does not.

That's why the test was failing. When index is used to retrieve an object, it is returning the second row of an unordered result set. And `first()` was consistently picking the first created one.

## What can be done about it?

There are multiple approaches to the problem.

### Make the query stricter

This is what I did to fix the test. I added one more query parameter to ensure that I get only one instance of a `Service` from the query.

```python
second_service = Service.objects.filter(
    service_type="L3Connection", related=some_other_service_instance
).first()
```

This approach is only as good as it's feasible. It's easy to apply, but sometimes adding new parameter is not really helping, and only makes the code unreadable. In my case, I could switch to using `get()` instead of `filter()` after applying the change.

### Chain `order_by` with  `filter`

Another approach is to specifically order the `QuerySet` retrieved by `filter()`:

```python
second_service = Service.objects.filter(
    service_type="L3Connection",
).order_by("created_at", "pk")[1]
```

This approach adds some complexity to the query, but at least does not require any new state migrations to be performed. I use `created_at` timestamp here, but any other ordered field should do the job.

Note that if ordering is done only by `created_at`, and the same timestamp is used in more than one instance, non-deterministic ordering may still occur. Hence the usage of `pk`.

### Specify `ordering` in model's `Meta`

To avoid taking care of sorting the `QuerySet` in place, adding `ordering` attribute to `Meta` of model class should do the job, too. It could be as simple as the following:

```python
class Service(models.Model):
    class ServiceTypes(models.TextChoices):
        L3_CONNECTION = "L3Connection"
        ROUTING = "ROUTING"

    name = models.CharField(max_length=100, null=True, blank=True)
    service_type = models.CharField(max_length=100, choices=ServiceTypes)
    created_at = models.DateTimeField(auto_now_add=True)

    # Added ordering to the model
    class Meta:
        ordering = ["created_at", "pk"]

```

This approach requires additional migration being executed (even though no SQL changes are applied), but it might also be the cleanest long-term solution for the problem of undefined ordering of query sets.

## Summary

So as you can see, with great complexity of the database, more knowledge about Django ORM's internals can be needed to solve obscure issues.

The problem I described was probably specific to the app I work on and its combination of Netbox, PostgreSQL and multi-endpoint workflows being tested.

Anyway, I wasted too much time on observing CI pipelines randomly failing on my branches because of someone else's tests, so I decided to take a look. And since the topic looked quite curious - I decided to describe it here.

Lesson learned: Make your QuerySets deterministic, either via stricter filters, explicit ordering, or `Meta.ordering`.

> *That's it for today. Happy hacking! 🐍*

___

<br>

[^1]: <https://docs.djangoproject.com/en/6.0/ref/models/querysets/#filter>
[^2]: <https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.ordering>
[^3]: <https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.first>
