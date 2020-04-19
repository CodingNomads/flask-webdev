Great, you've just *defined* your form and it's fields, but as you may have realized, that doesn't equate to *seeing* it on the screen as a real, live, breathing form. It's now time to create the template that will *show* your new form on a webpage.

### Rendering Forms using Jinja

First things first, it's best to know how to render forms "the hard way" in HTML. This particular quick lesson in rendering forms will be a little easier than starting from scratch as it will include how to use Jinja placeholders render parts of your `NameForm`. If you want, you can follow along by putting this code in your `index.html` template file. Note that later in this lesson, you'll replace your form rendering "the hard way" into a much easier way.

Let's assume a few things to set the stage.

1. You've defined your form along with a few fields.
   - You did this in the last lesson.
2. You have a view function that passes in your form to a template via `render_template()`. The argument passed in to Jinja is called `form`.
   - You will make this view function in the next lesson.
   - The argument containing the form doesn't have to be named `form`, but it's used in the following examples.
3. The template that you rendered the form to exists.
   - In your case this might be `index.html`.

These steps apply generally to any `FlaskForm` you want to render using HTML and Jinja. So with that, let's dive in!

```jinja2
<form method="POST">
	{{ form.hidden_tag() }}
	{{ form.name.label }} {{ form.name() }}
	{{ form.submit() }}
</form>
```

The first part of rendering a form in HTML is to start with a `<form>` tag, with a `method` attribute. You know a little about POST, so this shouldn't be too much of a surprise. Remember the long spiel about security? There's a little more to do than just render the form. The `form.hidden_tag()` is needed for Flask-WTF to implement CSRF protection, even though it's invisible on the page when the form is rendered. You'll want to include it because it's important!

To actually show the form and not render just the invisible parts, next is to display the fields. For fields that have labels, you'd start with rendering the label first, then the field itself is rendered by calling the field. Yes, form fields are callable! When called, they do whatever is needed to render themselves to HTML. For the submit button, all that's needed is to simply render the button.

You can even define HTML `id` attributes for fields in your form so that you can define CSS styles for them. For example, to do this for the `name` field, you'd add a keyword argument to its call.

```jinja2
{{ form.name.label }} {{ form.name(id="my-field-id")}}
```

### Bootstrapping Your Forms

Doing it this way may have you thinking, "Gee whiz! I don't want to spend all this time to render a form, *especially* if it's for something like an extensive questionnaire about accordions!", as you cover your face with your hands in fear.

Presented to you here is the antidote, which you can use as a complete replacement for all that tedious rendering above. Just add water!... I mean, Flask-Bootstrap!

```jinja2
{% import "bootstrap/wtf.html" as wtf %}
{{ wtf.quick_form(form) }}
```

Bootstrap once again saves the day with its own slick form styles, but even more noteworthy here is that Flask-Bootstrap gives you a sweet helper function called `quick_form()` which renders an entire Flask-WTF in one go. No more rendering the form fields individually! Makes life easy, doesn't it?

To make our life easier, we're gonna use Flask-Bootstraps predefined CSS styles. That way, we don't have to cringe at a form that looks like it came from the Internet of the 90's, we can have a cool modern look right outta the box (`import "bootstrap/wtf.html" as wtf`, `wtf.quick_form(form)`, `form` is a variable, and we don't have to define the form fields individually)

### Putting It All Together

Whether or not you already tried rendering your `NameForm` from "the hard way" to using the Flask-Bootstrap `quick_form()` helper function, go ahead and pull up `index.html`. To include the `NameForm` for the Ragtime app, it will look something like this:

```jinja2
{% extends 'base.html' %}
{% import "bootstrap/wtf.html" as wtf %}

{% block title %}Ragtime{% endblock %}

{% block page_content %}
<h1>Welcome to Ragtime, {% if name %}{{name}}{% else %}Anonymous{% endif %}!</h1>
<p>Enjoy your stay.</p>
{{ wtf.quick_form(form) }}
{% endblock page_content %}
```

Whenever this template is rendered for the first time, it will show a message "Welcome to Ragtime, Anyonymous!" plus a nice little greeting. It will also show your newly rendered form you defined! Coolio.

[//]: # (Of course the form can't be shown yet because there's no view function...)

![](../images/placeholder.png)

The only thing that looks a little fishy is the conditional starting with `{% if name %}`. Where did that `name` come from? It's not the same as `form.name`, and how can you possibly show a name if you haven't even entered one into the `form.name` field yet? This is a mystery that will have to be solved in the next lesson!
