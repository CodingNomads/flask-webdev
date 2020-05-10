Now it's your turn to make a blueprint! This lesson will apply all that you've learned in the last section about blueprints, so refer to it if needed. Along with fleshing out the blueprint itself, you'll make all the necessary files and folders.

### Make The Authentication Blueprint

#### The Package

Make a subpackage called `auth` within the `app` package. This is where all your authentication-related view functions, forms, and other stuff will live.

#### The Blueprint

Create the `Blueprint` in `__init__.py`. This file will be short.

#### The View Functions

Make the view functions in `views.py`. Make view functions `login()` and `register()`, with routes of the same name. Have them render templates `login.html` and `register.html`, respectively. Make these empty template files in the folder `templates/auth/`. You don't have to implement any functionality yet.

#### Register The Blueprint

Finally, register the `Blueprint` with the application. In your call to `register_blueprint()`, use the `url_prefix` argument with value `'/auth'`. This makes it so that any view functions associated with the blueprint will be accessible as `/auth/login`, for example.

#### Other Files

While you're at it, you can also create an empty `forms.py`.
___

Once you have all that, you're good to go for the next lesson, where you'll give your `User` model the functionality needed to see if a user is authenticated or not.
