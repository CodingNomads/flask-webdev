Configurations, configs, configuration settings. So much config. But rest easy, because you're done with that for a while! You won't have to see those words again for a while. Instead, you'll make sure you're prepped for the remainder of your Flask course marathon.

### Requirements File

Imagine the future: you have a superb app that does amazing things and your peers and people you don't even know are *surrounding* you because it's such an amazing app! And they want to try it themselves.

![](https://images.unsplash.com/photo-1465199308303-08e6bc3fa443?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1567&q=80)

But they would be crushed if you didn't have a `requirements.txt` in your repo. This little file is what allows them to create a virtual environment in Python that is *just like yours*. It gives all the package dependencies your app has with their exact versions you used. If that sounds like an undertaking, you're mistaken, because making and filling out this file is super easy. Just run:

```bash
(env) $ pip freeze > requirements.txt
```

[//]: # (Show an example, indicate the versions may be outdated)

You'll want to include this file in your `flask-webdev` git repo, so don't forget to add it! As you develop your app, you'll want to keep updating this file as you did with the command above. Then, anyone who wants to try out your app, including you, can make a new virtual environment and run the command:

```bash
(env) $ pip install -r requirements.txt
```

### Unit Tests

While there's not a whole lot to test right now, it's still important that you know where you'll put your tests. In this course, you'll use pytest to make your unit tests. This will be a mini crash course in how to get you up and running with pytest and Flask.

#### How Pytest Works

[//]: # (TODO: Add more)

If you haven't already installed pytest, go ahead and run:

```bash
(env) $ pytest
```

Pytest might be the easiest unit testing framework in existence. (DISCLAIMER: This is the author's very exaggerated opinion.) It does most of the work of finding your tests *for you*, so all you have to worry about it setting up your files, writing your code, and running the command to test. When you initiate the command `pytest`, it automatically looks for Python files that begin with `test_` and runs those, then looks for `test*` functions. Couldn't be easier, right? That's why you made the `tests/` folder earlier in this section.

Here's what your `tests/` folder setup will look like:

[//]: # (TODO: Might include "functional" folder later)

```
tests/
├── conftest.py
└── unit/
    └── test_app.py
```

#### conftest.py

The `conftest.py` file isn't required for pytest to run tests, but it can make your life a whole lot easier. That's because in this file, you can create **fixtures**. Fixtures are reusable pieces of test code.

#### First Test

(content coming soon)

### What's To Come

Way to go! You officially just finished tearing your app apart, then put it back together like some sort of Frankenstein's monster. Except this is your monster, and it's not a monster at all. It's now a well-greased, ready-for-so-much-more webapp that you'll continue developing in a much more orderly fashion. You're ready to battle user authentication, email notifications and verification, and so much more. Onward!

![](https://images.unsplash.com/photo-1568223661110-54147ba680b0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80)
