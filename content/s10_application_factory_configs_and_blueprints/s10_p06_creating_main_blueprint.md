Hopefully by now you have "blueprint" in your head of what Flask blueprints actually do. In this lesson, you'll make your first one.

### Main Blueprint

This blueprint will not be *doing* anything new. It'll actually just replace all the existing functionality you had before: the view function(s), your `NameForm`, and the error handlers. It'll be called "main" because it will define the *main* functionality of your app.

#### Create the Blueprint

The only thing that *is* new is that you have to make the Blueprint! If you haven't already, make your `main/` package with an `app/main/__init__.py` file. Then put this in the `__init__.py` file:

```python
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
```

Blueprints in Flask are defined by the `Blueprint` class. Here, `main` is a `Blueprint` with a name of `'main'`. The second argument in a `Blueprint` is the module where the blueprint is located. It's just like the one you used for instantiating a `Flask` object in the `create_app()` function. The `__name__` Python variable is usually fine. The last line then imports the view functions and the error handlers, which you'll move to `app/main/views.py` and `app/main/errors.py` later, respectively. The views and error handlers will be part of the main blueprint instead of the global app you had before this section. The reason this line comes after the blueprint creation is to prevent errors from cropping up due to circular dependencies. You'll see in a sec why this is.

#### (Re)Defining the Routes

Let's now move on to `app/main/views.py`. This is where your view functions from `hello.py` will be moved to, and there's a few differences:

```python
from flask import session, render_template, redirect, url_for, flash
from . import main
from .forms import NameForm
from .. import db
from ..models import Role, User

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        # ...
        return redirect(url_for('.index'))
    return render_template(
        'index.html',
        form=form,
        name=session.get('name'),
        known=session.get('known', False))
```

In particular, for `index()`, it's no longer decorated by `app.route`, but by the `main` blueprint. The code snippet here shows a bunch of other relative imports, because remember, the `main` blueprint is part of the `main/` package, as well as `forms`. To access the `Role` and `User` models as well as the database, that requires another `.`, as in `..` in order to grab those since they exist in the `app/` package.

See how the `main` blueprint is imported? In your `__init__.py`, if you had imported `views` and `errors` *before* you made your `main` blueprint, this `from . import main` would have caused you an issue.

[//]: # (need to clarify this)

Did you notice anything else that's different? I wouldn't blame if you didn't, as it's hard to see! A mini-lesson first: when it comes to using blueprints and referencing their view functions, the `url_for()` endpoint argument needs to be the name of the blueprint, followed by a `.`, followed by the view function name. In the case where you want the url for a view function *in the same blueprint*, the blueprint name is optional.

Okay, that might not have made sense, so let's go a bit slower. Say you have a view function outside the `main` blueprint and you want to redirect to the `'/index'` page defined in the `main` blueprint. To do that, you'd need `redirect(url_for('main.index'))`. Flask works this way because it allows different blueprints have the same endpoint names. So you could have a "main" blueprint define an `'/about'` page, and a "second" blueprint that has an `'/about'` page, too. Assuming the standard `route` decoration, the endpoint names would then be `main.about` and `second.about`. These two endpoints can coexist peacefully.

If you haven't seen it yet in the code above, what's different is the `'.index'` instead of `'main.index'`, but they are the same thing! Using just `'index'` instead will not work because it's defined in the "main" blueprint.

### (Re)Defining the Error Handlers and Form

There's not too much difference in how your error handlers will be defined, but there's something important to point out. Go ahead and put this in your `error.py` file:

```python
from flask import render_template
from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    error_title = "Not Found"
    error_msg = "That page doesn't exist"
    return render_template('error.html',
                           error_title=error_title,error_msg=error_msg), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    error_title = "Internal Server Error"
    error_msg = "Sorry, we seem to be experiencing some technical difficulties"
    return render_template("error.html",
                           error_title=error_title,
                           error_msg=error_msg), 500
```

Let's think about error handlers again. Before, when you had your app and its routes defined globally, any 404 or 500 errors would get routed to your error handlers `page_not_found()` or `internal_server_error()`, respectively. Your error handlers were designated as such by the `errorhandler` decorator. However, if you make a blueprint and define error handlers for it with the `errorhandler` decorator, those only become error handlers for the routes defined in the *same* blueprint, and not the app as a whole. But fear not, for you can make your error handlers handle errors globally by using the `app_errorhandler` instead.

Finally, the `NameForm` you made before can go in `forms.py`. Then once you do that, the main blueprint is complete!

### Registering the Blueprint

If you jumped the gun too quick and tried to run your app, you would have eventually found that no matter where you go, you get those ugly "Not Found" errors wherever you try to navigate to. Neither your routes or even your error handlers will work! That's because you still need to register your blueprint, and you can do so easily with the Flask `register_blueprint()` method. Bring up your `app/__init__.py` file and add this to your `create_app()` function.

```python
def create_app(config_name):
    # ...

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
```

Bam! Now whenever you create an application with your application factory, you'll get an application that's *not* dull and lifeless, but that has all your routes, error handlers, and forms. The `app.register_blueprint()` method takes all that's packaged with the `main` package and treats it as part of itself in a way. Haven't you ever seen those fictional giant robot battles? Well, metaphorically speaking, you just added your robot's legs (the main blueprint) to your own robot's torso (the Flask app). You're about to run, but there's still more to do! Let's get those "legs" running by getting your app working again, in its superior modular form. To the next lesson!

![](https://images.unsplash.com/photo-1562461089-907f104c2b9d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=634&q=80)
