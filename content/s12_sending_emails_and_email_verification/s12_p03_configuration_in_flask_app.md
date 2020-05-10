It's time to configurate the configuration of your Flask-Mail config settings. In no time, you'll be sending emails from your app left and right. Ready?

### The Configuration Settings

Alright, so what exactly do you need to do for the SMTP configuration stuff? There's plenty of settings, but this lesson will guide you through it all. In particular, Flask-Mail will need to have these configuration keys set:

- `MAIL_SERVER`: The hostname or IP of the email server. Default: `localhost`
- `MAIL_PORT`: The port of the email server. Default: 25
- `MAIL_USE_TLS`: To enable Transport Layer Security (TLS), or not to enable. That is the question. Default: `False`
- `MAIL_USE_SSL`: To enable Secure Sockets Layer (SSL), or not to enable. That is the other question. Default: `False`
- `MAIL_USERNAME`: Mail account username
- `MAIL_PASSWORD`: Mail account (app) password

### Settings For Your Gmail Account

To enable email support using your new Gmail account, you'll have to set most of the settings above. What better place than your `config.py` file? To take advantage of inheritance, you can place these in your base `Config` class.

For your new Gmail account, you can set your configuration settings like this:

```python
class Config():
    # ...

    # Flask-Mail config
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    # Other email settings
    RAGTIME_ADMIN = os.environ.get('RAGTIME_ADMIN')
    RAGTIME_MAIL_SUBJECT_PREFIX = 'Ragtime —'
    RAGTIME_MAIL_SENDER = 'Ragtime Admin <ragtime.flask@gmail.com'
```

The first three configuration key settings come <a href="https://support.google.com/a/answer/176600?hl=en#gmail_reqs" target="_blank">straight from the horse's mouth</a>, that is, from Google. Next is the username you signed up with, then your **app password** that you wrote down in the last lesson. These settings are taken from environment variables only since, y'know, it's pretty sensitive stuff. You can set them in the CLI like so:

```bash
export MAIL_USERNAME=<your Gmail username>
export MAIL_PASSWORD=<your Gmail app password>
```

<div class="alert alert-info" role="alert"><b>Info: </b>If you haven't already, now might be a good time to create a new file to instantiate your various environment variables.</div>

The last three configuration key settings are for your app. They are more for convenience and not required for Flask-Mail, but configuration files are good at that, convenience. The first one `RAGTIME_ADMIN` is the email account of the administrator of the Flask app. That just means it's the email that gets *notifications* about various things that occur within your app, like when a new user signs up or when the server catches on fire. Yours doesn't have to have `RAGTIME` in the name, of course.

![It burns!](../images/server_on_fire.png)

The `RAGTIME_MAIL_SUBJECT_PREFIX` is just that, the subject prefix for when the app sends an email. When the app sends email to users, it will be *from* whatever the value of the `RAGTIME_MAIL_SENDER`.

### Initializing Flask-Mail

To initialize Flask-Mail, you must place your lit candles on each point of the pentagram, then recite a blessing of Cthulhu. Just kidding, all you need to do is the usual extension initialization. Here's what you'll add in your app package's `__init__.py`.

```python
from flask_mail import Mail
mail = Mail()

def create_app(config_name):
    # ...
    mail.init_app(app)
```

___

You've just configurated Flask-Mail to help you send emails from your app. Now the next step? Sending emails from your app! The next lesson awaits...
