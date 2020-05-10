Are you ready to learn the way of the application factory

### Application Package

You should have already made a folder `app/` and moved many of your files there, as well as created a new `__init__.py`. If not, do that because this is the way of the application factory. What this does is it creates a package for your Flask application where all the application code lives including templates and static files. The new `models.py` file in the `app/` folder is where all your models `Role` and `User` will be moved to.

<div class="alert alert-warning" role="alert"><strong>Note: </strong>Did you read that last sentence? :)</div>

When your package is in a working state later in this section, a piece of Python code that exists outside the package can create your app. The name `app` for the folder is just a generic name, it could be anything and it would still be a package.

### Why Use A "Factory Pattern?"

### Application Factory

[//]: # (Now that you know about the factory pattern and how it helps us with configuration...)

To get your super cool application factory spitting out applications like a pro, you'll have to move much of your original `hello.py` script to the new `__init__.py` file in your `app/` folder. Particularly, this is where all the initialization of extensions goes, as well as a new `create_app()` function:

```python
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)

    return app
```

This new `create_app()` function is a factory function, otherwise known as your **application factory**! That means you can give the `create_app()` function the name of a configuration you'd like to use, and it'll give you a brand spankin' new Flask application instance with those configuration settings. For now, you only have one *set* of configuration settings, so the only parameter that makes sense here is `'default'`. The `config` dictionary from before is indexed with the `config_name` passed in, which grabs the config `class`. Then the neat part: `app.config` makes a *copy* of all the configuration settings from that class using its `from_object()` method. If any initialization is needed for the configuration, `init_app()`'s invocation will get the job done.

Again, this avoids the problem of having to change configuration settings within your *previously single* file. You can instead specify everything you want in a config class. The only drawback is that you can't change the configuration on the fly anymore, but what's gained is that your project is a lot more organized. And take note that your package encapsulates everything in a folder, so you can load your configurations from outside.

The two extensions that are defined don't get initialized right away. Did you notice there's no application instance to hand to them at first? That's okay, though, because they can be initialized later with their own `init_app()` method once an application is created. You'll still want them in the global scope so you can import them from other modules if needed.

This is all pretty cool, isn't it? A function that *makes* different "flavors" of your Flask application. First it makes the application, then it initializes the extensions, and finally it... Oh dear, it appears it doesn't do that yet. That is, it is completely missing any semblance of *routes*! Without those, there's nothing to do and nowhere to go except to the next lesson.
