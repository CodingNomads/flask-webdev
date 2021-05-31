Your config vars are set, now you need to let your Flask app know how to _find_ all of them on Heroku. Open up your `config.py` file and make the following changes:

### `SECRET_KEY` variable

Change your `SECRET_KEY` setting to the following:

```python
import os

SECRET_KEY = os.environ.get('SECRET_KEY') or 'anyRandomLongStringUseNumbersYo#123'
```

Remember that you will want to declare a long random string as your _actual_ `SECRET_KEY` and put that value into your Heroku config vars. Flask cannot operate without a `SECRET_KEY` variable being set, this is why you'll keep a _default value_ as the second argument in the method call. The default value is used in case Flask can't find a value with the name `SECRET_KEY` that you need to define in your config vars.

<div class='alert alert-warning' role='alert'>
    <strong>Note:</strong> Keep in mind that the default value, in this case <code>'anyRandomLongStringUseNumbersYo#123'</code> should <em>never</em> be used in production.
</div>

### `FLASK_CONFIG` variable

[//]: # (While there are some other settings that usually need to be changed in your Flask app for it to work in production, Heroku arranges these changes for you. You will learn more about them in the chapter about IaaS deployment later on.)

[//]: # (Last one: config setting)

You'll definitely not want to use your app's `default` configuration for production. That's why you'll make a new configuration (or two) for production. You'll learn more about it in the next lesson.

### Next Up: Flask Configuration Additions

[//]: # (Next section: Flask configuration additions (config.py) (NEW PAGE))

The general adaptations mentioned above are necessary for any Flask deployment. You will _always_ need to make sure you are not showing the `SECRET_KEY` in production, and the `FLASK_CONFIG` value must be a configuration created with production in mind. You'll build such a configuration in the next page.
