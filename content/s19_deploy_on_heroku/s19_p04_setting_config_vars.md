Heroku gives you both a **CLI** as well as a **GUI web interface** to set environment variables for your remote application. You can think of it in the same way as setting your environment variables locally. Below you will learn the essentials. You can always consult the <a href="https://devcenter.heroku.com/articles/config-vars" target="_blank">official documentation on Config Vars</a>.

### Setting Config Vars Through Heroku CLI

After you have the Heroku CLI successfully installed and created your Heroku app, you can quickly set config vars in your remote environment similarly to how you would do that locally using `export`:

```bash
$ heroku config:set SECRET_KEY=blablablablablablablablablabla
```

With <a href="https://devcenter.heroku.com/articles/config-vars#using-the-heroku-cli" target="_blank">similar commands</a> you can also read (`get`) and remove (`unset`) config vars.

For your secret key in production, it's recommended to use something like Python's `uuid` module to generate a random string in hex, from your terminal like so:

```bash
$ python -c "import uuid; print(uuid.uuid4().hex)"
995366f815394c0eab0e2f8bbd50f1cb
```

Then, you can use the `heroku config` command like shown above to use the output as your app's `SECRET_KEY` when deployed through Heroku.

### Setting Config Vars Through Heroku's Dashboard

Alternatively, you can use the web GUI interface to view, add, and remove config variables for your remote environment on a per-app basis.

Access your <a href="https://dashboard.heroku.com/" target="_blank">Heroku Dashboard</a>, click to access your app, then click on the "Settings" tab:

<img alt="Settings tab Heroku Dashboard" title="Settings tab Heroku Dashboard" class="img-responsive cn_image" src="https://github.com/CodingNomads/static/blob/main/flask-webdev/imgs/config_vars_setting.png?raw=true">

Here you have the option to click "Reveal Config Vars". Be brave and click that button:

<img alt="Reveal Config Vars button" title="Reveal Config Vars button" class="img-responsive cn_image" src="https://github.com/CodingNomads/static/blob/main/flask-webdev/imgs/config_vars_reveal.png?raw=true">

You will be presented with a GUI view of your current config vars, which is also an interface to set, edit, and delete them. This is where you'll want to add your `SECRET_KEY`:

<img alt="Config Vars Heroku Dashboard" title="Config Vars Heroku Dashboard" class="img-responsive cn_image" src="https://github.com/CodingNomads/static/blob/main/flask-webdev/imgs/config_vars.jpg?raw=true">

### Other Variables To Set

Once you have the `SECRET_KEY` set, you'll want to set these other variables on the Heroku side as well:

- **`FLASK_APP`**: Set to `ragtime.py`, of course!
- **`FLASK_DEBUG`**: Set to `0` since you don't want to reveal any debug information to users
- **`FLASK_CONFIG`**: Set to `heroku`; you'll see more about this value later
- **`MAIL_USERNAME`**: Set to `<your email username>`
- **`MAIL_PASSWORD`**: Set to `<your email password>`; this will be the *app password* for Gmail!

___

Super duper, once you do all that, let's discuss Heroku's convenient Dashboard a little more on the next page.
