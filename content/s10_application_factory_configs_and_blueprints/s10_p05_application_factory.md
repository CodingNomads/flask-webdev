
Application Factory
------
you make a folder app and putting most of the files in there because this is the way of the app factory. It uses the factory pattern aka the `create_app` function. you're making a flask app inside a package. with this factory, you can put in any configuration you want and get out a flask app that uses that configuration. the only drawback is that you can't change the configuration dynamically anymore. Our package is called `app`. This encasulates everything in a folder, and you can load the config from outside.
