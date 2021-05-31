In this lesson, you'll find below a couple more tests, and there's also a discussion on keeping tests consistent across the code.

### Flask Test Configuration

Before going over the tests, there's something to be aware of. In the last section, you built the `TestConfig` class. Now you can put it to use in your tests. The `TestConfig` needs the `DATABASE_TEST_URL` environment variable set, or the default value should work just fine. Make sure this gets set to a *different* value from your normal development database. Your test database can be called something like `data-test.sqlite` to distinguish it.

### Additional App Creation Test

Here's an another test that also ensures app creation, and makes sure that `current_app` is available once the application context is pushed. It also checks that the `TESTING` configuration variable is set to `True`.

```python
from flask import current_app

def test_current_app():
    app = create_app('testing')
    app.app_context().push()
    assert current_app
    assert current_app.config['TESTING']
```

### Database Insertion Test

Now what about testing something more complicated, like an insertion into the database?

```python
from app import db
from app.models import User

def test_database_insert():
    app = create_app('testing')
    assert app.config['TESTING']
    # ensure test database configured
    assert 'data-test.sqlite' in app.config['SQLALCHEMY_DATABASE_URI']
    app.app_context().push()
    # create all tables if not created
    db.create_all()

    u = User(email='john@example.com', username='john')
    db.session.add(u)
    db.session.commit()

    # IMPORTANT clear database for future tests
    db.session.remove()
    db.drop_all()
```

Are you starting to see a pattern with these unit tests? :) This third test checks that the correct database is configured for testing. Once confirmed, it creates any and all tables necessary, then performs the insertion. There aren't any asserts because it is assumed that SQLAlchemy has no trouble inserting a row in the `users` table, if it is able to of course. If it isn't successful you'll know in the form of an exception.

<img alt="Testing Train Wreck" title="Testing Train Wreck" class="img-responsive cn_image" src="https://github.com/CodingNomads/static/blob/main/flask-webdev/imgs/important.png?raw=true">

The last part denoted as "IMPORTANT" is, well, pretty important, so don't skip over these here next couple paragraphs unless you understand. At the point right before this block, your test has *changed the state* of the database: it now has a row in a table. If you created another test that assumes the database is completely empty at the time it runs and it *isn't*...

<img alt="Testing Train Wreck" title="Testing Train Wreck" class="img-responsive cn_image" src="https://github.com/CodingNomads/static/blob/main/flask-webdev/imgs/train_wreck.jpg?raw=true">

...this might happen. So it's always good that your tests *begin* in a clean or known state, and *end* in a clean or known state. Variables like `app` in this test are local to the function, so changing it is no issue, but the database `db`, as mentioned before, is not and might be altered throughout your tests.

Once you understand that and practice being *clean* in your tests, your ready to continue your testing journey. But perhaps you have this on your mind: that's a lot of code to do a simple test. What to do about that?

### Next Lessons: Testing Setup and Fixtures

Indeed, that *is* a good bit of code to write for each test. Not only does it get annoying to rewrite the same chunks of code, it's also error prone and it can get messy. Plus, you may want to organize your increasingly complex test code into different folders based on what they do, such as *unit* and *functional* tests. There must be a solution or two to these problems, right?

Of course there is! You aren't taking this course for nothing, after all. ;) In the next couple lessons, you'll get your custom test code organized in a way that allows you to write tests quickly. You'll also learn about fixtures which will let you write reuseable code that your tests can use as necessary.
