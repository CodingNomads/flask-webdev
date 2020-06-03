Alright so let's make your very first Flask-WTF form! This one's gonna be simple so you know what's going on. You'll be asking the user a *very difficult* question: "What is your name?"

In your `hello.py` file, you'll import a few objects and define a form class which is derived from `FlaskForm`:

```python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")
```

"Wow, that's it?!" I think I heard you say as you finished typing that. Yes, you've already defined your form and its fields! The fields are defined as *class* variables, and their values are various `*Field` classes, the `*` just being a convenient way of saying `StringField`, `SubmitField`, `SelectField`, `DateField`, etc. The `*Field` classes are imported from the `wtforms` module, and you could of course <a href="https://wtforms.readthedocs.io/en/stable/fields.html#basic-fields" target="_blank">import more of those</a> if your form needs additional kinds of fields.

Let's break it down a little further. Your form, `NameForm`, has a text field called `name`. It also has a submit button called `submit`. A fancy web form wouldn't be as fancy without validators, and Flask-WTF makes checking inputs easy. Validators can be declared within a list inside `*Field` constructors, and one example is the `DataRequired` validator. The `name` field has this validator, and it means that the information in a `NameForm` cannot be submitted without putting a name in that field. There are also <a href="https://wtforms.readthedocs.io/en/stable/validators.html#built-in-validators" target="_blank">plenty more validators</a> should you need them.

___

What's that? You want to see the form really bad, huh? You want to see it work before your eyes? To do that, you'll have to render it first, but that part might be easier than the above! Nevertheless, head on over to the next lesson for your next mission.
