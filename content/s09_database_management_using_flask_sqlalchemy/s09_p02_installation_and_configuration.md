This lesson will get you started with Flask-SQLAlchemy so you can start working with relational databases for your app.

### Install Flask-SQLAlchemy

Just like the other extensions, you'll use pip to install Flask-SQLAlchemy:

```bash
(env) $ pip install flask-sqlalchemy
```

### Specifying a Database

With Flask-SQLAlchemy, databases are specified as a URL. While there are different URL formats for different database engines, like MySQL vs Postrges vs SQLite, for your database you'll use SQLite. The URL looks like this:

```
sqlite:////absolute/path/to/database
sqlite:///c:/absolute/path/to/database (For Windows Only)
```

Many database engines require a server hostname and sometimes username and password for authentication, but for SQLite, all you need is a path to a filename on disk. Because you're dealing with a *Flask* extension, you can specify the database URL the *Flask* way buy setting some configuration keys.

In your `hello.py` file, add near the top:

```python
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = "keep it secret, keep it safe"
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ...
```

In this snippet, there's a couple new imports added, including `SQLAlchemy` which represents the database and gives access to all the SQL goodness that Flask-SQLAlchemy provides. To get Flask-SQLAlchemy setup with URL, you must set the `SQLALCHEMY_DATABASE_URI` key to the database file on your server. For you, this is your development computer and if you're following along, the database file is located in `~/Documents/CodingNomads/projects/flask-webdev/`. Of course you probably don't have a database file just yet. If it doesn't exist, SQLAlchemy will create one for you.

<div class="alert alert-warning" role="alert"><strong>Note: </strong>Notice the key is <code>SQLALCHEMY_DATABASE_<b>URI</b></code>, not <code>SQLALCHEMY_DATABASE_<b>URL</b></code>!</div>

The `SQLALCHEMY_TRACK_MODIFICATIONS` key is already `False` by default, but it's set explicitly so that SQLAlchemy doesn't alert with an annoying message. Tracking modifications of the database isn't usually necessary and it eats up a lot of memory when enabled.

Once that's all done, Flask-SQLAlchemy is initialized just like any other Flask extension.

And with that, you should be good to go! Next you'll learn about models and relationships. No no, not like Angelina Jolie and Brad Pitt. Anyway, you'll see what that means in the next lesson.
