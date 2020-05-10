You just learned about Flask-Login and user mixins and how they make logins a little easier. In this lesson, you'll make your own login form and the template to display it. Here's what you'll need to do:

### Login Form

Make a `LoginForm` class derived from `FlaskForm`. Put it in `auth/forms.py`.

#### Fields

To make the login form, you'll need these fields:

1. `email`
   - To make the email field, just use a `StringField`. It will need validators `DateRequired()`, `Length()`, and `Email()`. Allow length to be anywhere from 1 to 64 characters.
2. `password`
    - For the password field, you can use just that, a `PasswordField`. Input is required for the form to be submitted.
3. `remember_me`
    - This is to indicate if the website should remember the user for a while or not. Use a `BooleanField` with just a label.

#### Template

Define the template in `templates/auth/login.html` that will display the form. Remember to inherit from `base.html`!

#### View Function

Don't worry about that yet! You'll learn about logging users in and out in a later lesson. You'll implement the view function then.

___

Once you're done, you'll have a login form ready to go when you need it! And with that you're ready to learn about logging in with Flask-Login.