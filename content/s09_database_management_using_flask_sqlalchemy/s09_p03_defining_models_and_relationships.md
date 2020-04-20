Once you have Flask-SQLAlchemy installed and configured, you're ready to start playing with models and relationships, whether that be Barbie doll drama or SQL, and preferably it's the latter. The basics are described in this lesson.

### Defining Models

A **model** is an object that abstracts away much of the technical SQL functionality and that represents a persistent entity. The models are the objects that your webapp interacts with to get the data it needs and update data as needed. For you, that means it's just a Python object that has attributes which match the columns of a table. Simple, right?

Making a model in Flask-SQLAlchemy means defining a new class that represents a database table you want to make. The extension gives you a convenient way to do that by providing you a base class for models called `Model`. It also provides several helper classes and functions to make defining the structure of your models painless.

Let's think back to the theme of the app in this course for a second: a music-sharing social media webapp. That involves having users that can share content, so you'll want to make a `User` model that can represent each user's information. Give defining `Model`s a spin by putting this in your `hello.py` file:

```python
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return f"<Role {self.name}>"


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return f"<User {self.username}>"
```

Great, you've got a couple of nice looking models now! Roles will be talked about in a bit. For now, notice the `__tablename__` class variable, which defines the name of the table in your database. So, a `Role` class instance represents a row in the `roles` table, and a `User` represents a row in the `users` table. You won't need to do much with the table name, but it's defined here so that a default name isn't chosen instead. Using plural for the table name is popular, but unfortunately not what Flask-SQLAlchemy sets as the default.

### A Bit About Columns

After `__tablename__` are the attributes of the model, which are instances of the `db.Column` helper class. Every `db.Column` has a type, and Flask SQLAlchemy gives you helper classes for those, too. The `Integer` and `String` column types have been defined here, but there are many others:

| Type name    | Python type        | Description                                                  |
| :----------- | :----------------- | :----------------------------------------------------------- |
| BigInteger   | int                | Bigger integer value                                         |
| Boolean      | bool               | True or False value                                          |
| Date         | datetime.date      | Date value                                                   |
| DateTime     | datetime.datetime  | Date and time value                                          |
| Enum         | str                | List of string values                                        |
| Float        | float              | Floating-point number                                        |
| Integer      | int                | Regular integer                                              |
| Interval     | datetime.timedelta | Time interval                                                |
| LargeBinary  | str                | Binary blob                                                  |
| Numeric      | decimal.Decimal    | Fixed-point number                                           |
| PickleType   | Any                | Python object Automatic Pickle serialization                 |
| SmallInteger | int                | Short-range integer, typically 16 bits                       |
| String       | str                | Variable-length string                                       |
| Text         | str                | Variable-length string, better for very long strings         |
| Time         | datetime.time      | Time value                                                   |
| Unicode      | unicode            | Variable-length Unicode string                               |
| UnicodeText  | unicode            | Variable-length Unicode string, better for very long strings |

After the first argument, other configuration options can be specified for a column. Some of them are:

| Option      | Description                                                         |
| :---------- | :------------------------------------------------------------------ |
| default     | Default value for column                                            |
| index       | If True, create an index for this column for more efficient queries |
| nullable    | If True, allow empty values, otherwise don't allow empty values     |
| primary_key | If True, the column is the table’s primary key                      |
| unique      | If True, don't allow duplicate values                               |

For the new `User` model, `unique` is specified for the `username` attribute since you'd of course want your users to have something unique and unused from other users. It's also got the `index` option set to true to make username lookups much faster. You'll be querying for usernames quite often later in the course.

### Relationships

Because relational databases are *relational*, they gotta have **relationships**. Relationships are connections between rows of different tables. In the next code snippet, you'll establish a **one-to-many** relationship between `Users` and `Roles`. Each user of *many* will have *one* role in the application, meaning a user could a normal user, a moderator to manage comments, or a site admin to delete or edit certain content. This relationship between models can be defined with another column in the user table and a `relationship` in the role table. You'll see how that works in just a bit.


### The below needs editing

There are many relationship options you can use, and each has a different behavior/use case. (Try some in a lab)

create_all() can't be called again if the models need to be changed because the tables already have the old columns. To force a change in columns, you can call drop_all() and then create them all again with create_all(), but that removes any data you have!

But don't worry, there's a way to update your models without destroying all the information that exists! We'll discover this magical solution together later, but for now let's talk about how to get data in the tables in the first place.

