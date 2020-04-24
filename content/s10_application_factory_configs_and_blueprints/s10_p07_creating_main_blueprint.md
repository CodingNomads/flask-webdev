Creating the Main Blueprint
-----------------------------

the `url_for()` must change to either "main.index" or ".index"

Made main/__init__.py because that's where the Blueprint is born. imports views and errors from there. you'll use this module to register our blueprint later

views and errors.py go in a folder `main`, as well as our form class. These views, error handlers, and forms are all part of the blueprint. Theoretically, our blueprint is in a dormant state until you register with our flask app. It's a bit like a keyboard or mouse, where the devices are dormant until you plug them into the computer. So once you register our bp, our views come to life! Error handlers actually need the `app_` to make them work app wide. you import our form in the views module. Note the `main` folder is also a python package, but it's within a package