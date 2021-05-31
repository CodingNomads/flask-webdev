
In this lesson, you'll learn how to use pytest to make your unit tests. This will be a mini crash course in how to get you up and running with pytest and Flask.

___

### What Is Pytest?

Pytest is a framework for unit testing, right? What's so special about it other than that? Well, let's see what its documentation has to say.

> pytest is a framework that makes building simple and scalable tests easy. Tests are expressive and readable—no boilerplate code required. Get started in minutes with a small unit test or complex functional test for your application or library.

As was hinted at before, pytest is not just a framework, it may be the only framework you'll ever need for testing your python code. Then again, it's also a great framework for getting started with as a beginner. Now that you have a better idea of what pytest is, next is more about how it discovers your tests.

### Test Discovery

Pytest might be the easiest unit testing framework in existence. (DISCLAIMER: This is my exaggerated opinion.) It does most of the work of finding your tests *for you*, so all you have to worry about it is setting up your files, writing your code, and running the command to test. When you initiate the command `pytest`, it automatically looks for Python files that begin with `test_` and runs those. Within *those* files, it looks for functions that begin with `test` in their name. Couldn't be easier, right?

With that said, while you might have a basic idea for how to run a test, there's been no mention so far of how to test your *Flask app*. Let's get into that right now.

### Testing Your Flask App

Next, you'll learn about how to run your first Flask app test, along with other helpful tips and additional tests.

#### First Test

The first step, as you probably know, is to make a file where your tests will go. Make a file called `test_app.py` and put it in your project's top-level directory, like so:

```
app/
└── ... # app package files
... # all your other files and folders
test_app.py
```

That should make it so that your `app` package can easily be imported by your test file. Let's have your first test create an `app` instance using your new application factory with the `testing` configuration:

```python
from app import create_app

def test_app_creation():
    app = create_app('testing')
    assert app
```

The `assert` makes sure the `app` is defined. And barring any exceptions that may occur in the `create_app` function, your test should pass! Give it a shot:

```bash
# from your top-level project directory
(env) $ pytest
```

Here's what you'd expect your output to be:

```
============================= test session starts ==============================
platform darwin -- Python 3.9.1, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
rootdir: /Users/Shared/git_repos/flask-webdev-master
collected 1 item

test_app.py .                                                            [100%]
```

If it worked right away, great! You wrote your first successful test for your Flask app. Didn't work? If it's an import error, see below. Otherwise, that's okay! That's what tests are for, to help you find bugs. The problem could also be with your test file itself, usually in the form of "module not found" or "X has no attribute Y". Just remember that tests are *normally* worth the trouble of getting running since they can save you time in the long wrong, so keep trying until the test passes, or get some help from the <a href="https://forum.codingnomads.co/c/courses/flask-webdev/33" target="_blank">forum</a> or from your mentor.

<div class="alert alert-warning" role="alert"><strong>Note: </strong>

If your <code>app</code> package can't be found by your test script when you run <code>pytest</code>, try instead:
<pre><code class="bash language-bash">python -m pytest</code></pre>

This is because running <code>pytest</code> by itself may not add the *current directory* `.` to the `PYTHONPATH` environment variable. `PYTHONPATH` tells python where to look for your local modules/packages (like `app/`). Using <code>python -m pytest</code> ensures this.
</div>

<div class="alert alert-info" role="alert"><b>Info: </b>
Throughout the rest of this section, <b>please assume that the </b><code>python -m pytest</code><b> command is the way you should run your tests.</b>
</div>

___

Once you've written your first test, there's always room for more! The next page contains a couple more tests to show you how your tests grow and evolve.
