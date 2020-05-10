You're in the know about a secure but easy way of protecting users with hashing. In this section, you'll get to see it in action, then apply it to your webapp.

### Give Hashing a Spin

To help you with all that complicated cryptography, we'll bring in the help of a library called <a href="https://palletsprojects.com/p/werkzeug/" target="_blank">Werkzeug</a>, which is a WSGI web application library. Fun fact: "Werkzeug" actually a German word that means "tool." But that's not what you're here for, you're here to do some hashing!

Werkzeug has all you'll need in order to perform password hashing with its `security` module. It provides two important functions:

- `generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)`
  - Remember all that complicated stuff in the last lesson? This function does all the work of taking a password in plain-text and giving you its hash version as a string. You can also change the hashing method and salt length but for your webapp, it isn't necessary.
- `check_password_hash(hash, password)`
  - This one is the reverse, in a way. Once you have a hash, you can check it against any password to see if they "match" and if they do, it returns `True`. (Hint: there's only one password that works.) So for you, you'll use this to verify that a password entered by a user is indeed the one that will let them sign in. The whole point of a *pass*word!

### Adding Changes to the User Model

To make a use of these functions, you can encapsulate them in your `User` model.

```python
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    # ...
    password_hash = db.Column(db.String(128))
    # ...
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
```

The first thing you'll do is add the `password_hash` column. Again, this is the only "password" you need to keep around in order verify that someone's password is the correct password. As such, there's no password column and no need to even be able to access a user's password, so the `password` property throws an `AttributeError` This makes it clear to anyone with a `User` object, mainly you, that the password is a secret! However, a new password can be *set*, and once set a new password hash is calculated with the `generate_password_hash()` function.

Next is the `verify_password()` function, which uses the `check_password_hash()` function. It takes a password, likely that the user entered to login, then compares it with the hash in the database. If the two line up, it returns `True`.

### Try It Out

What's one way you can give this a spin? If you guessed `flask shell` you'd be right! While there are other ways to try your new functionality out, all you need to do is see hashing in action. Create a new `User` and play around:

```python
(env) $ flask shell
>>> u = User()
>>> u.password = 'corn'
>>> u.password
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/user/Documents/CodingNomads/projects/flask-webdev/app/models.py", line 173, in password
    raise AttributeError('password is not a readable attribute')
AttributeError: password is not a readable attribute
>>> u.verify_password('corn')
True
>>> u.verify_password('cork')
False
>>> u.password_hash
'pbkdf2:sha256:150000$d9qSdlno$e54fe56f649a845662a414f600791463281be18226c8a8f507fbc287809af199'
>>> u2 = User(password="tom")
>>> u2.password_hash
'pbkdf2:sha256:150000$Kfiq5Qh1$b4c922ede4424b1fb8248fccdf33a1b8a7239168ddc94a1f0a000c3cd3c2d700'
```

You can see how reading the `password` attribute throws an error. You'll also notice that the password hashes from users `u` and `u2` are very different despite being based on the same password. That's due to the salting of the passwords, which adds that random component.

One way to ensure your password functionality is working is by writing a unit test! (coming soon)

Well done, your very own password hashing and checking functionality is now complete! Now it's time to put them to use. But first, it's a good idea to make `Blueprint` just for authentication. That'll be your job! Details are in the next lesson.
