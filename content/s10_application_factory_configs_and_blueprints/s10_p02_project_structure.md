Now that you know why modularizing your Flask application is important, let's now take a look at what it looks like.

### Before You Start

This little paragraph right here that you're reading is to tell you that the information below is only informational. (Wow, what a sentence!) While you'll actually implement all of this at some point in this section, it will be step by step. Your application might not be in a working state until the end of this, but that's okay! This is a major restructuring of your albeit small app, so keep that in mind.

If you haven't already made a `git commit`, now is a good time to do so.

### File and Folder Structure

To make your Flask project much more organized, take a look at the file and folder structure below:

```
flask-webdev/
├───app/
│   ├── main/
│   │   ├── __init__.py
│   │   ├── errors.py
│   │   ├── forms.py
│   │   └── views.py
│   ├── static/
│   ├── templates/
│   │   ├── base.html
│   │   ├── error.html
│   │   ├── index.html
│   │   └── user.html
│   ├── __init__.py
│   └── models.py
├── env/
├── migrations/
├── config.py
├── ragtime.py
└── requirements.txt
```

[//]: # (Alternatively, show a picture of the folder structure)
[//]: # (Later:
├── tests/
│   ├── conftest.py
│   ├── unit/
│   │   ├── test_password.py
│   │   └── user.html
)

You will notice that there are several new files and folders.


#### Top-Level Directories

- *`app/`*: A package for your application! The package is made by creating a new folder and an `__init__.py` file inside. This is the to-be-created Flask application lives.
- *`migrations/`*: Just like before, this contains the database migration scripts.
- *`env/`*: Your virtual environment, silly.

#### New Files

- *`config.py`*: This is where your configuration settings will live, and contain some configuration classes. They were foretold about a bit in the last lesson.
- *`ragtime.py`*: This is where you'll make an instance of your Flask application. It'll also contain a few helper functions that define tasks to manage the application
- *`requirements.txt`*: Think of this file as a courtesy to your fellow programmer peers, or even yourself. If you or someone else wants *regenerate* your own virtual environment, they can do so with this. It lists the package dependencies of your project.

[//]: # (https://imgflip.com/i/3y9rj9)
![](https://i.imgflip.com/3y9rj9.jpg)

[//]: # (Below will probably be taught in a video)

### What To Do Now

Go ahead and make your project look as close to the structure above.

<div class="alert alert-warning" role="alert"><strong>Note: </strong>Make sure you use <code>git mv</code> to move your files so you can keep better history of your file changes!</div>
