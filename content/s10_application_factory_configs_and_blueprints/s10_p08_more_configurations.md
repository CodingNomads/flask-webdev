If your app it up and running again, congrats! You'll learn about getting it set up for any kind of configuration in this lesson.

### Inheriting Configuration Classes

[//]: # (May still need to talk about those different config sets)

As you learned previously, your app will probably need all kinds of sets of configuration. There's the configuration sets you may use for development, for testing, and for production when your app is ready for the world.

That means just having one config class just won't do. To get your app's configuration capabilities to its full potential, and taking advantage of object-oriented programming, you'll inherit your `Config` class! Here's what it looks like:

```python
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or "keep it secret, keep it safe"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_DEV_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL') or \
        'sqlite://'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        f'sqlite:///{os.path.join(basedir, "data.sqlite")}'

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
```

So what happened? The first thing to notice is that `SQLALCHEMY_DATABASE_URI` is not defined in `Config` anymore, but rather inside the new child classes, `DevelopmentConfig`, `TestingConfig`, and `ProductionConfig`.

#### Development Config

First up is the development configuration. You've basically been using a development configuration this whole time because you've been, well, developing and debugging and such. The database URL you had before is the same as it was in `Config`, but now it's in `DevelopmentConfig`. However, now there's `os.environ.get('DATABASE_DEV_URL')`. Whazzat? The `DATABASE_DEV_URL` is an environment variable just like the `FLASK_APP` environment variable. At least, that's what your code will look for if you have it defined or not. If you don't, it will opt for the database URL you were using before. You'll notice the same sort of thing was done for the `SECRET_KEY` in `Config` and the other database URLs in the other classes.

<div class="alert alert-warning" role="alert"><strong>Note: </strong>Just like you did for <code>FLASK_APP</code>, you can define any other environment variable with the `export` command (Mac and Linux only).</div>

The next config setting in `DevelopmentConfig` is `DEBUG`. This is basically the same as setting the `FLASK_DEBUG` environment variable. However, it's important to know that any setting for `FLASK_DEBUG` will override the `DEBUG` setting you may have in a configuration. For example, if `DEBUG` is `True` and you set `FLASK_DEBUG` to `0`, Flask debugging mode won't be enabled.

<div class="alert alert-warning" role="alert"><strong>Note: </strong>Remember, if you want to use VSCode to debug and set breakpoints with a `launch.json`, it's recommended that you *don't* have Flask's debugging mode enabled!</div>

#### Testing Config

> Something that is untested is broken.
> ~Unknown

That comes from Flask's <a href="" target="_blank">"Testing Flask Applications"</a> page, so it seems like the developers think it's pretty important to test your Flask apps! That's why you'll have a configuration solely for running tests on your app. The `TESTING` configuration flag will disable error catching during request handling, so it's good for getting juicier error reports so you can fix things quicker. If there's no environment variable set for the database, it'll default to no database. The reasoning behind this is that you can theoretically have multiple tests that tests multiple different things, including different *database* setups. Having no database for testing would tell you you didn't set one up when you ran your tests!

#### Production Config

And now for the `ProductionConfig`, which is used for when you're deploying your app. You'll get to that point soon enough, but this config will be waiting for you once you do. Not much new here, just a different database URL defined.

### (Re)Configuring your Application

The last part of `config.py` is the `config` dictionary, and some more names have been added here. The `'default'` name is now `DevelopmentConfig`, and `Config` is no longer used.

Let's go back to `ragtime.py` to make a quick changes in regards to the config. You can change it so that it uses a new `FLASK_CONFIG` environment variable to define the name of the config to use (from the `config` dictionary):

```python
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
```

Sweet. There shouldn't be anything else needed, except to set all your environment variables! In fact, you could make a bash script that you can "source" in order to set these environment variables automatically:

```bash
export FLASK_APP=ragtime.py
export FLASK_DEBUG=1
export FLASK_CONFIG=development
```
[//]: # (export FLASK_ENV=development needed?)

You can call it something like `development_settings.sh`, then run it with

```. development_settings.sh```

every time you're ready to develop.

___

And now for the final stretch before we get into the nittiest of gritty of the webapp's functionality. Head over to the next lesson to learn about it.
