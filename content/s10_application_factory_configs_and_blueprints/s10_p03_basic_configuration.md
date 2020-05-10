Once you get your project organized with the new structure, it's time to define the app's configuration.

Flask allows you to load a configuration as a class, which means you can create a class and define CONSTANTS within it to pass your settings to the app. Put this in your `config.py` file:

```python
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = "keep it secret, keep it safe"
    SQLALCHEMY_DATABASE_URI =\
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

config = {'default': Config}
```

You'll notice that it's not much different than the `app.config` settings you defined earlier. The only difference is, again, that you can define constants in a class instead of defining them directly with the `app.config` dictionary object.

And now you see see the static `init_app()` method. You're probably confused, either because this might be the first time you've seen a static method, or don't see the point of defining an empty `init_app()`. Or both! Well, you've already seen the `init_app()` methods called for some Flask extensions, and you can treat your configuration class as if it were an extension itself. Not *because* it is an extension (it isn't), but because config classes may have some initialization of their own. Further, you can *extend* your configuration classes, so if you want a configuration that's *slightly* different than one you have, you can just use the original as a base class and change what you need. The `init_app()` function is there in case you need to do any initialization with your derived config class.

The last thing here is a dictionary called `config`. While there's only one configuration class so far to make things easy, you'll add more classes to the `config.py` file later. This dictionary is just a way of "naming" these classes so they can be referenced more easily. So, the `'default'` configuration refers to the new `Config` class.

If that doesn't quite make sense in terms of why a config class may have it's own initialization, or why there's a dictionary, not to worry. You'll learn about extending this class into other base classes later in this section.

In the next lesson, you'll see how you'll use this class to get your app configured! That's what it's supposed to do, after all.
