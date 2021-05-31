In this lesson, you'll create a couple configurations to get your app one big step closer toward deployment.

___

### Production Configuration

You might remember that the Flask application instance has it's own logger attached, as `app.logger`. The logger writes any log messages to the console in debug mode (meaning `FLASK_DEBUG=1`), but since production is *not* part of debug, how would you possibly see that your app has any problems? One way is to attach another handler to the app logger, one that can send an email when an error occurs. Let's see what setting that up would look like in the `ProductionConfig` class:

```python
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        f'sqlite:///{os.path.join(basedir, "data.sqlite")}'

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        import logging
        from logging.handlers import SMTPHandler
        creds = None
        secure = None
        if getattr(cls, 'MAIL_USERNAME', None) is not None:
            creds = (cls.MAIL_USERNAME, cls.MAIL_PASSWORD)
            if getattr(cls, 'MAIL_USE_TLS', None):
                # logging: to use TLS, must pass tuple (can be empty)
                secure = ()
        mail_handler = SMTPHandler(
            mailhost=(cls.MAIL_SERVER, cls.MAIL_PORT),
            fromaddr=cls.RAGTIME_MAIL_SENDER,
            toaddrs=[cls.RAGTIME_ADMIN],
            subject=cls.RAGTIME_MAIL_SUBJECT_PREFIX + " Application Error",
            credentials=creds,
            secure=secure
        )
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)
```

This class, also based on the base `Config` class like your other configuration classes, actually has a use for the `init_app()` method that no configuration classes so far have used. You can use this method to set up, you guessed it, the log handler for sending emails. The `SMTPHandler` class is imported, but before invoking it to create an instance of `SMTPHandler` class, there's first a bit of setup that needs to be done. Mostly, it's the settings for SMTP that the `app.logger` object will need to be able to send emails about errors, and of course needed are the username and password for the email. Later in the creation of the handler, the SMTP server settings are also passed. You can check out the `SMTPHandler` class <a href="https://docs.python.org/3/library/logging.handlers.html#smtphandler" target="_blank">here</a> for the details.

Oh, what? I forgot to mention something? Maybe even forgot to tell you about setting up an environment variable? Ah, the `SQLALCHEMY_DATABASE_URI`, set from the environment variable `DATABASE_URL`. Well, if somehow there is no environment variable with that name, then it will be a SQLite file like you've been doing before. However, Heroku doesn't use SQLite, but does use PostreSQL. Now what?

Well, to set `DATABASE_URL` to the proper value AND set with a value reflecting a PostgreSQL database is actually surprisingly easy. Just add Heroku's convenient PostreSQL addon to your project:

```bash
$ heroku addons:create heroku-postgresql:hobby-dev
Creating heroku-postgresql:hobby-dev on <app name>
Database has been created and is available
 ! This database is empty. If upgrading, you can transfer
 ! data from another database with pg:copy
Created postgresql-spherical-70199 as DATABASE_URL
Use heroku addons:docs heroku-postgresql to view documentation
```

Heroku's hobby-dev version of the PostgreSQL let's you have up to 10000 rows of SQL data, all for free. And do you see that? It looks like `DATABASE_URL` has been set for you. Pretty convenient, huh? That means, when you deploy your app on Heroku, it will take care of the `DATABASE_URL` environment variable for you.

### Heroku-specific Configuration

So you're off to a good start with the `ProductionConfig`; in general it's a good configuration for most any production environment. Because Heroku has it's own "flavor", it's good to create a configuration just for Heroku based on the production configuration.

What is this flavor I'm talking about? Well, Heroku considers log output other than just error messages. You can write more general and informative log messages, and Heroku will capture it. Why would you want to capture messages other than errors? Because knowledge is power! Let's take a look at the new config:

```python
class HerokuConfig(ProductionConfig):
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # log to stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler
        file_handler.setLevel(file_handler, level=logging.INFO)
        app.logger.addHandler(file_handler)
```

So here, the level handled is `INFO`, which also allows warnings to pass through to the log output.

Now what about that `heroku` config setting you set earlier? You might have guess correctly already, you'll need to add it to your `config` dictionary:

```python
config = {
    # ...
    'heroku': HerokuConfig,
    # ...
}
```

___

Heroku requires some additional platform-specific settings that you will adjust next. On the upcoming page you will follow Heroku's instructions to assure your app is ready for Heroku deployment.
