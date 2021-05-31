Once you get your authentication blueprint in place, it's time to get your `User` model even more ready for authenticating users. This lesson will teach you about the Flask-Login module and how it helps you with managing users.

### Flask-Login

Flask-Login is a lightweight Flask extension that makes working with authentication with respect to the user session a piece of cake.

![](https://images.unsplash.com/photo-1559329373-78f77851b979?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=700&q=80)
Pictured is the unit of effort required to use Flask-Login to manage user logins

What Flask-Login does in technical speak is it records and updates, as needed, the user's authenticated state in the user session. The user session was talked about in Section 8 on forms, in terms of how information recorded in forms is remembered. Updating the user session with the user's state of authentication means you can know when the user is signed in or not, which you can use to give access to certain pages, or not. There are of course other extensions to manage the user session when it comes to authentication, but Flask-Login is probably the most simple.

To install it, it's another simple pip:

```bash
(env) $ pip install flask-login
```

### User Model Prep for Authentication

It's a good thing you have a user model, because Flask-Login needs one of those in order to help with the user session. But as your `User` model exists now, it's not enough for Flask-Login to work well. The good news is you'll only need a few properties and a function to get everything ready:

- `is_authenticated`: Must be `True` if the user has valid login credentials and is currently logged in, otherwise `False`.
- `is_active`: Must be `True` if the user is allowed to log in or `False` if not. Basically it means that if an account is not disabled, `is_active` will return `True`.
- `is_anonymous`: This must always be `False` for regular users who login and is only `True` for any user that is not logged in
- `get_id()`: This function returns a unique identifer for user

And now for the fun part: Mixins! While those brownie mixes you get might as well be called "mixins" themselves, this is not that. Flask-Login gives you a very convenient class to help you with authenticated-or-not users. You can "tack on" this `UserMixin` class to the `User` model. Once you do, you have all those properties and the `get_id()` function handled for you!

#### Using UserMixin In The User Model

To use the `UserMixin` in the `User` Model, all you need to do is add the `UserMixin` as a base class:

```python
from flask_login import UserMixin

class User(UserMixin, db.Model):
    # ...
```

___

That's it! You're all done, and all of those properties and function above are implemented for you. In the next lesson, you'll learn all you need to know about the Flask-Login login manager, which will use your user mixin.
