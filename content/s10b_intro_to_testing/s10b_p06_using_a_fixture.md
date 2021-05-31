In this lesson, you'll be shown the app creation test fixture and how to apply it to a test for your Flask app.

___

### The Fixture

In the last lesson, you were tasked with creating a fixture that you could use throughout your tests. How did you do? It probably looks something like this:

```python
@pytest.fixture(scope='module')
def new_app():
    # setup
    app = create_app('testing')
    assert 'data-test.sqlite' in app.config['SQLALCHEMY_DATABASE_URI']
    test_client = app.test_client()
    ctx = app.app_context()
    ctx.push()
    db.create_all()

    # testing begins
    yield test_client

    # teardown
    db.session.remove()
    db.drop_all()
    ctx.pop()
```

If not, no worries, you're learning after all. :) Remember this goes in the `conftest.py` file. First is the app creation using the `testing` configuration. And instead of using the application instance directly, you use a `test_client` instead, as recommended in the <a href="https://flask.palletsprojects.com/en/2.0.x/api/" target="_blank">Flask documentation for testing</a>. The application context is pushed, the database tables created, and then the application is provided to whichever tests are using it. Remember that the `scope` is `module`, so all tests in a python script full of test functions that use the fixture will be given the test application instance `test_client`.

Then once the tests that use the fixture have completed, the teardown begins. First the database session is removed, then the tables are dropped. Finally, the application context is popped.

### Database Insertion Test Revisited

Now that you've got this new fixture, it's time to use it! Let's take another look at that database insertion test a few lessons ago. There was a lot going on there, but now with your new fixture, it will look a lot simpler:

```python
from app import db
from app.models import User

def test_database_insert(new_app):
    u = User(email='john@example.com', username='john')
    db.session.add(u)
    db.session.commit()
```

As a reminder of how fixtures work, the `test_client` yielded from the fixture is available as `new_app` in the `test_database_insert` test function. Pytest has done the voodoo behind the scenes, all you had to do was make `new_app` as a parameter to your test function. Notice it's the same name as your fixture!

But the test itself looks pretty simple, doesn't it? Indeed, the fixture has made life quite easy in this case, because your test can focus on what it needs to and lets the fixture take care of the rest. In this case, a `User` is created, then added to the database.

### More Tests To Come

For now, you have learned the basics of using pytest to test your Flask app. Great job in keeping up! Later, as you continue in the course, you'll be tasked with creating more tests that will ensure correct functionality of the new parts of your app as you build them. A tested app is a working app!

<img alt="Working App" title="Gears" class="img-responsive cn_image" src="https://github.com/CodingNomads/static/blob/main/flask-webdev/imgs/gears.png?raw=true">
