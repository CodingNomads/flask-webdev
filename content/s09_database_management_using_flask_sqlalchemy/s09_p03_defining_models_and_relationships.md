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

After `__tablename__` are the attributes of the model, which are instances of the `db.Column` helper class. Every `db.Column` has a type, and Flask SQLAlchemy gives you helper classes for those, too. The `Integer` and `String` column types have been defined here, but there are many others. Here are the most common:

| Type name    | Python type        | Description                                                  |
| :----------- | :----------------- | :----------------------------------------------------------- |
| Boolean      | bool               | True or False value                                          |
| DateTime     | datetime.datetime  | Date and time value                                          |
| Float        | float              | Floating-point number                                        |
| Integer      | int                | Regular integer                                              |
| LargeBinary  | str                | Binary blob                                                  |
| PickleType   | Any                | Python object Automatic Pickle serialization                 |
| String       | str                | Variable-length string                                       |
| Text         | str                | Variable-length string, better for very long strings         |

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

Because relational databases are *relational*, they gotta have **relationships**. Relationships are connections between rows of different tables. In the next code snippet, you'll establish a **one-to-many** relationship between `Role` and `User`. Each user of *many* will have *one* role in the application, meaning a user could a normal user, a moderator to manage comments, or a site admin to delete or edit certain content. This relationship between models can be defined with another column in the user table and a `relationship` in the role table. To establish a one-to-many relationship from `Role` to `User`, you do this:

```python
class Role(db.Model):
    # ...
    users = db.relationship('User', backref='role')

class User(db.Model):
    # ...
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
```

First, let's go backwards and look at the `User` model. Why would you want to add a column? Since each user has one role, to know which role that corresponds to, you can add a **foreign key** with the `db.ForeignKey()` helper class that references a row in the `roles` table. That was a mouthful, but just think of it this way.

We are CodingNomads, right? When you think of a *foreigner*, or say a tourist, that is a person who is in a country that he or she is not originally from. This person brought a ID or passport from the person's home country to the new country. It's similar in a database with foreign keys. In this case, the `role_id` is like that tourist's ID. It *references* a `Role` in the `roles` table, but `role_id` is an *attribute* of `User`, like the person in the new country. The `db.ForeignKey()`'s argument is the column in the `roles` table that contains the primary key.

[//]: # (Dunno if I coulda skipped explaining about what foreign keys ^^^)

The `users` attribute of `Role` represents all the users that have a particular role. With an instance of `Role`, you can see the "many" side of the relationship with the `users` attribute. It's simply the list of all users with that role! The `db.relationship()`'s purpose is to tell the application what model is on the other side. Here's the really cool part about it that you should read twice: the `backref` keyword argument allows you to specify `role` as an attribute of a `User` instance *in addition to* the `role_id` attribute. So instead of `a_user_instance.role_id` to get the ID of the role, you can use `a_user_instance.role` to get the actual `Role`.

There are a few other relationship options:

[//]: # (TODO: put relationship options in a table)

Really cool stuff, right?! If it still hasn't sunken in, that's no problem, with practice you will get the hang of it. One thing to note is that in there's a somewhat rare chance that `db.relationship()` won't be able locate the foreign key by itself. For example, it could happen when you define two `Role` foreign keys in the `User` model. It can't be sure which one you might mean, so giving it additional arguments to remove any ambiguity should solve the problem.


You just got through the basics models and relationships! Does it feel like boot camp? Good, that means your learning. Now gimme 20 pushups, then carry on to the next lesson.
