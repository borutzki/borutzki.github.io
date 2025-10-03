---
layout: post
title:  '>>> print("Hello World!")'
excerpt_separator: <!--more-->
---

<!--more-->

Hi there!

My name is Kacper. I work as a Python developer and have experience with things like Django, Robot Framework, PyTest, GitLab, Docker and technologies surrounding it. Since I've worked with network automation, I can say I'm somewhat familiar with it, too.

I wanted to start this blog for quite a while. I've collected multiple notes with technical solutions, how-tos, guidelines, and general tips that I believe could be useful to others. So I decided to start sharing them here.

You may expect straightforward posts about topics like:

- Python (core functionalities, pro tips, optimisation) 🐍
- Python libraries (Pydantic, Jinja2, Django, Flask) 📚
- TDD and unit tests (unittest, PyTest, how to write testable code) 🧪
- Quality assurance (Robot Framework, BDD, test strategies) 🤖
- DevOps and related tools (Docker, GitLab, GitHub) 🐳
- Network automation (protocols, how-to articles, examples) 🕸️
- Tools I use daily (Visual Studio Code, Obsidian, Jekyll) 🧑‍💻
- Solutions to random technical problems with Linux / macOS / Windows 🧑‍🔧
- Software architecture (architectural styles, design patterns, clean code, technical writing) 🏛️
- Technical books (short reviews) 📚

I don't want to bloat my posts with chatter (unless I clearly warn you in advance). I mean to provide simple solutions for problems I came across working with code. More topics to come as I learn.

The first few posts will be mostly Python-related. These will include various tips I wrote about using #DailyPythonista hashtag on social media, recent notes about code I worked with, and examples of code.

When all of that is here, I will try to write a series of posts about Robot Framework - from beginner to pro. It seems like this topic is not much covered on the web, especially regarding new versions of the tool.

Feel free to reach out on social media if you'd like to ask something specific, share feedback, discuss a topic I might be familiar with, or even talk about a job offer. I'm open to discussion.

## By the way: various ways to print `"Hello world"` in Python

To leave you with something "useful", let's see multiple ways to print `"Hello world"` in Python. The list of examples is not exhaustive and could easily be extended. I just wanted to have some wordplay with the title of a popular movie.

### The good

Good because it's simple.

```python
>>> print("Hello world")
Hello world
```

Still good anyway, even though variable name is vague:

```python
>>> x = "Hello world"
>>> print(x)
Hello world
```

Good because it has neat padding in the output:

```python
>>> x = "Hello world"
>>> print(f"|{x:^20}|")
|    Hello world     |
```

### The bad

Bad because it's over-engineered:

```python
>>> def hello_world_factory(): return "Hello world"
...
>>> print.__call__(hello_world_factory())
Hello world
```

### The ugly

Ugly because of left padding:

```python
>>> x = "Hello world"
>>> print(f"|{x:<20}|")
|Hello world         |
```

Ugly because of right padding:

```python
>>> x = "Hello world"
>>> print(f"|{x:>20}|")
|         Hello world|
```

___

*That's it for today. Happy hacking!*
