In this lesson, you'll learn about how to use fixtures to create reusable chunks of test code.

### What's A Fixture?

A **test fixture** is defined in the Wikipedia as:

> A software test fixture sets up a system for the software testing process by initializing it, thereby satisfying any preconditions the system may have.

That sounds like a mouthful, but it's simpler than you might think. Test fixtures help you do any setup that your tests may need, and even help you "tear down" your setup if necessary. As the pytest documentation puts it:

> They provide a fixed baseline so that tests execute reliably and produce consistent, repeatable results.

<img alt="Fixture" title="Fixture" class="img-responsive cn_image" src="https://github.com/CodingNomads/static/blob/main/flask-webdev/imgs/fixture.png?raw=true">

So what do these things look like and how do they work?

### Fixtures in Pytest

Fixtures in pytest are defined as functions, but not only that: the functions must be decorated with the `pytest.fixture` decorator. Here's a quick example:

```python
@pytest.fixture
def my_list():
    return [3, 4, 7, 8]

def test_3_in_list(my_list):
    assert 3 in my_list

def test_4_in_list(my_list):
    assert 4 in my_list
```

The fixture `my_list` simply returns a list of numbers. In order to use the fixture, the `test_3_in_list()` function declares the `my_list` fixture as a parameter. Then, it simply references the fixture when checking if 3 exists in the list. You'll notice that it doesn't haven't to explicitly define the same list, it instead uses the list returned from the fixture as if it *were* defined in the `test_3_in_list()` function. The same is true in the `test_4_in_list()` function, and this is the beauty of fixtures: they can get your tests initialized so your tests don't have to do extra work.

The code looks a little counter-intuitive, doesn't it? How does the `test_3_in_list` know that the `my_list` fixture returns `[3, 4, 7, 8] just from declaring a parameter with the same name?

Pytest is doing some magic behind the scenes. First, it finds any fixtures you defined. Then, when it discovers your test functions, it passes the value(s) returned by the fixtures with the same name.

#### Fixture Scope

The scope of a fixture directly relates to how often the fixture is run per test. In other words, when resources are initialized by a fixture, they *survive* for a certain period of time. Here's a table of the scope of a fixture, and what that means for how often it is run:

| Scope      | Frequency            |
| :--------- | :------------------- |
| `function` | Run once per test    |
| `class`    | Run once per class   |
| `module`   | Run once per module  |
| `session`  | Run once per session |

Fixtures by default have a scope of `function`. In this last example, that means the `my_list` fixture was run *twice*, once per test function that used it. A list like that only needs to be run once, so if `my_list` were set to the scope `module` it would be run once but would still be accessible to both functions.

Be sure to check out <a href="https://docs.pytest.org/en/6.2.x/fixture.html#what-fixtures-are" target="_blank">pytest's documentation on fixtures</a>, it provides a great description and examples of how tests and fixtures actually work.

#### The `conftest.py` File

You just learned about the different scopes a fixture can take on. If you've been trying out some tests with the `python -m pytest` command, you've probably only had one or two files that contained all your tests. However, what if you had two files or *modules* with tests that needed to use the same fixture? Let's assume the tests above were separated into two different files, or modules:

```python
# test_file_1.py
def test_3_in_list(my_list):
    assert 3 in my_list
```

```python
# test_file_2.py
def test_4_in_list(my_list):
    assert 4 in my_list
```

You could set the `my_list` fixture to have a scope of `module`, where the fixture would be run twice, once per module. but would the fixture go in one of the files, both, or perhaps a different one? This is where the `conftest.py` file comes in, it's a one-stop-shop where you can place your fixtures to be accessed by *any* test file located in the same directory.

The `conftest.py` file isn't required for pytest to run tests, but it can make your life a whole lot easier. It makes it so that tests from multiple modules can access common fixtures. What might that look like, file structure-wise? The following files you don't need to make yourself, but with your test setup it might look like this:

```
tests/
├── conftest.py # my_list fixture defined here
└── unit/
    ├── __init__.py
    ├── test_file_1.py
    └── test_file_2.py
```

Then all you would need to do is call `python -m pytest tests/` as you've done before. You can read more about `conftest.py` <a href="https://docs.pytest.org/en/6.2.x/fixture.html#conftest-py-sharing-fixtures-across-multiple-files" target="_blank">here</a>.

#### Setup *and* Teardown

While you can have a fixture that sets up resources and provides them to your test functions, you can also have it *teardown* those resources so that your test environment is in a clean state. As said before, it's important for your database to be in a clean state (all rows deleted) at the end of a test or set of tests.

So how can you have a fixture that does that? By using the `yield` keyword instead of `return`, your function can have a setup phase *and* a teardown phase. Here's a silly example to demonstrate:

```python
@pytest.fixture
def order():
    # setup resource (order food)
    diner_order = DinerOrder()
    # return resource (give order to test)
    yield diner_order
    # teardown resource (remove plates, etc...)
    diner_order.clean_up()
```

### Rethinking Database Insertion Test

Now that you've gotten the rundown of fixtures, take a look at the previous page and think about how you might make a fixture that initializes your app and the test database and tears them down at the end. Try to combine all or most of the knowledge you gained from this lesson.

<div class="alert alert-info" role="alert"><b>Task: </b>Make a fixture <code>new_app</code> with scope <code>module</code> that:
<br><br>
<ol>
<li>Creates an instance of your app</li>
<li>Pushes an application context</li>
<li>Creates the tables of the database</li>
<li>Yields an app instance</li>
<li>Tears down the database</li>
<li>Tears down the application context</li>
</ol>
<br><br>
Try testing it out with by passing the fixture to a new test function.
</div>
___

Once you give this some thought (challenge yourself!), you'll be shown this fixture in the next lesson.
