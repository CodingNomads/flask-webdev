In this lesson, you'll learn about what Heroku needs along with adjustments you need to make in your Flask app.

___

### The basics

First, and most importantly, Heroku web applications require a `Procfile`.

This file is used to explicitly declare your application’s process types and entry points, and you can <a href="" target="_blank">read more detailed information</a> on Heroku's dev center. It is located in the root of your repository. The `Procfile` helps the web server software to know how to communicate with your app.

#### Procfile

```Procfile
web: gunicorn ragtime:app
```

This Procfile can initiate a variety of tasks. For your web app, the `Procfile` defined above will simply start the production web server, in this case using Gunicorn. What's the `web` mean? It's actually a task name recognized by Heroku to start the web server. Then, Gunicorn takes the name of your module and the name of your application instance separated with a colon.

<div class='alert alert-info' role='alert'>
    <strong>Info:</strong> The Procfile does not have any file extension. You can simply name it <code>Procfile</code>
</div>

#### Installing `gunicorn`

```bash
$ pip install gunicorn
```

`gunicorn` is your web server that will handle the communication between your Flask app and the web.

### Security

You're about to release your app into the wilds of the internet, and security should be at the top of your priorities. Below you'll learn how to easily add top-notch security to your Flask app.

#### Adding Encryption To Requests

While you've been developing your app, you've been using regular ol' HTTP to make everything work. But using *less secure, vanilla HTTP* is not going to cut it for a production webapp, as it is possible for user's credentials to get intercepted while in transit to the server. There are also other considerations that the Flask development team outlines <a href="https://flask.palletsprojects.com/en/1.1.x/security/" target="_blank">here</a>. You can easily add secure HTTP, or **HTTPS**, using <a href="https://github.com/GoogleCloudPlatform/flask-talisman" target="_blank">Flask-Talisman</a>:

```bash
$ pip install flask-talisman
```

Along with helping you quickly apply protections against some common web security issues, Flask-Talisman will enable **<a href="https://en.wikipedia.org/wiki/Transport_Layer_Security" target="_blank">TLS</a>** to encrypt all communications between clients and server, which is a win for both you and your users. But you only need to activate this when your app is in a production environment, so in your application factory you'll want to add this code:

```python
# app/__init__.py

def create_app(config_name='default'):
    # ...
    if app.config['HTTPS_REDIRECT']:
        from flask_talisman import Talisman
        Talisman(app, content_security_policy={
                'default-src': [
                    "'self'",
                    'cdnjs.cloudflare.com',
                ],
                # allow images from anywhere, 
                #   including unicornify.pictures
                'img-src': '*'
            }
        )
```

At this point, adding another extension to your app should be somewhat trivial, so what's up with all this content_security_policy stuff? By default, Flask-Talisman would clamp down on security by *outright disallowing scripts or styles* from outside your app, known as `'self'` above. Safe, but a little *too* safe. The additions to the policy will allow your app to use Bootstrap styling and to download images from anywhere.

<div class="alert alert-info" role="alert"><b>Info: </b>If you add new features to your app, you may need to update the <code>content_security_policy</code> to allow additional resources from outside your app.</div>

And that's right, you'll need to add `HTTPS_REDIRECT` as a configuration variable:

```python
class Config():
    # ...
    HTTPS_REDIRECT = False

class HerokuConfig(ProductionConfig):
    HTTPS_REDIRECT = True if os.environ.get('DYNO') else False
    # ...

    from werkzeug.middleware.proxy_fix import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)
```

`HTTPS_REDIRECT` is only set to `True` if the `DYNO` environment variable exists, which is set by Heroku in it's environment. If you were to test your Heroku configuration locally, your app would not use TLS.

"Hey wait, what's this `ProxyFix` thing?" You see, Heroku uses a *reverse proxy server* to redirect any client requests meant for your website to *your* app; these client requests don't go directly to your app but instead to this proxy server. Because of how Heroku's proxy server <a href="https://devcenter.heroku.com/articles/http-routing" target="_blank">works</a>, your app would get confused and would send external links like confirmation tokens through *http://*. To ensure your app *doesn't* get confused, you can use Werkzeug's `ProxyFix` to, well, fix it.

#### Cross-Site Request Forgery (CSRF) Protection

While you're at, you can easily add global CSRF protection across your app. You already learned a bit about this back in the section about forms, and they are already protected from CSRF attacks, but any requests outside your form may not be. Flask-WTF's CSRFProtect object will do the job:

```python
from flask_wtf.csrf import CSRFProtect
# ...
csrf = CSRFProtect()

def create_app(config_name='default'):
    # ...
    csrf.init_app(app)
```

It may be overkill in terms of security, but doing this now will provide peace of mind in case you add certain features to your app later.

### Deployment Tasks

When you install your app on a production server, you still need to be able to perform setup tasks like creating your database tables, upgrading your database, and inserting roles. Doing this all manually is tedious iffy because it could lead to errors, so adding a `deploy` command to do these tasks is a great idea:

```python
from flask_migrate import upgrade

@app.cli.command()
def deploy():
    """ Run deployment tasks """
    # migrate database
    upgrade()

    Role.insert_roles()

    User.add_self_follows()
```

You'll see how to use this command once you actually deploy your app to Heroku.

### Top-Level `requirements.txt` File

The last step to get your Flask app ready for deployment is to add a top-level `requirements.txt` file. Heroku looks in the top-level directory of your app for this file in order to install package dependencies. Before you create this this file, you'll first want to make a `heroku.txt` file for your Heroku-specific dependencies. This will include Flask-Talisman and Gunicorn, *as well as* psycopg2 that Heroku will need to get your fancy PostgreSQL production database going. The file will look something like this:

```powershell
# requirements/heroku.txt
-r prod.txt
flask-talisman==0.7.0
gunicorn==20.1.0
psycopg2==2.8.6
```

Version numbers may vary, of course. Then, you just need to copy those requirements to the new `requirements.txt` file:

```powershell
# requirements.txt
-r requirements/heroku.txt
```

___

That's it. You are now ready to deploy your app. On the next page you will learn how to finally get your webapp deployed on Heroku.
