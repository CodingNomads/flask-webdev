You might have been able to get your app running in the last section, but even if you were it wasn't pretty, was it? Well, it wasn't pretty, was it? In this lesson, you'll get your app running lickety split, and this will be a checkpoint for you to make sure you have your app working as it did before.

### Application Script

The last Python file you haven't touched yet is `ragtime.py`. That's where your Flask application will be born. Despite what your parents may have told you about baby webapps, they aren't just flown over by Tim Berners-Lee.

Anyway, yes, your Flask app `instance` will be created in this file, so go ahead and bring it up in your editor:

```python
from app import create_app, db
from app.models import User, Role
from flask_migrate import Migrate

app = create_app('default')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)
```

The first thing this does is make the familiar `app`. Did you miss it? You throw in the `'default'` argument because that's the "name" of your configuration. Next is instantiating the `migrate` object. Since your database `db` is created along with the app, it has to get instantiated after the call to `create_app()`. Then last, you put in your `shell_context_processor` for your `flask shell` sessions.

<div class="alert alert-warning" role="alert"><strong>Note: </strong>Now that the filename with your Flask instance in it, <code>ragtime.py</code>, is different from the previous <code>hello.py</code>, you'll have to update the <code>FLASK_APP</code> to use the new name. It's also a swell idea to turn on <code>FLASK_DEBUG</code> if you'd like.</div>

### Test Drive

You've taken Flask out for it's initial test drive in the sections up to this point. In this section, you took your app to the pit stop to get it suited up for the complex road ahead. Now that you made some major changes, you'll need to take it for another spin to make everything works as it should. Before you move on, take this time to get your app in a working state. Feel free to go back to the other sections if needed. Then, you're ready to define to define more configurations and finally, learn about some tips to keep your app moving throughout its development!

![](https://images.unsplash.com/photo-1579987323085-529f1a806810?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80)
