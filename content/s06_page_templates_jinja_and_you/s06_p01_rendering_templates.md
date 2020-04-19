### Templates

Hopefully, you've gotten yourself comfortable with the basics of how to make a Flask app and how to go about making basic routes. But strap yourselves in, as you're about to go from 0 to 60 in this course. We'll be picking up the pace; there won't be full code examples, but there will be code snippets with enough information to guide you through to making a full Flask app. As long as you read carefully ask for guidance from your mentor, you should be just fine!

[//]: # (At this point, I imagine we can cut off the "free" access and start hiding this content for non-course purchasers)

How did you do with making your own routes? Did you try adding some flavor with HTML to make it look more professional? Did your wrists start getting sore reaching for those angle brackets all the time? Seems like a pain, right? Having to make a brand new HTML string every time you want to make a new route feels very tedious. But here's the great news with Flask: You don't have to do that all the time!

The only job of our view functions should to generate a response to a request, that's it. Having to also *make* the pages? What a pain! For that, the creators of Flask also built *Jinja2*, which is a template engine. I'll call it "Jinja" for short.

[//]: # (TODO: Might make below more clear)

*Templates* are files that contain the text of a response. You know, for pages that say things like, "Upload your corn flake collection here!" That's great, but that's only text. Aha! Well, templates also support placeholder variables for the dynamic parts of the page, meaning those that change depending on the context of a request (who's corn flake collection, if the corn flakes are gluten-free, etc). These variables get replaced with real values through a process called *rendering*. And that's what Jinja's job is, to take the values those variables should take on passed in from Flask, then to render those values in with the surrounding text. Let's try this thing out!

### Making a Template

Before you get started, you're gonna have to make a folder named `templates`, which will live right inside your `flask-webdev` directory. That's because, by default, Flask looks for your templates in a folder called just that, `templates`. Once you've done that, you're ready to go!

#### It's Just HTML!

First things first, let's just get a simple template rendered. Think of a template as just an HTML file. Make a new template file `templates/index.html`. Put in the following:

```jinja2
<h1>Hello Web World!</h1>
```

Now in your `hello.py`, you'll need to import `render_template`, then replace your `index()` function:

```python
@app.route('/')
def index():
    return render_template('index.html')
```

With the `render_template()` function, all you need to do is indicate the path to the template relative to you `templates` folder, which is simply `"index.html"`. When a request is received for the index page and `render_template()` is called, Flask will enlist the help of Jinja2 to render the template.

Let 'er rip! Run the app with `flask run` and watch as you get the same output. A little boring, huh? Just wait, we're gonna go *dynamic*.

#### HTML++

While a template is just HTML, it's also a little more than that with Jinja. To help demonstrate, let's make another route, this time a dynamic one. Feel free to use one you might have made before in order to complete this next part.

The `render_tempalate()` has more power than it might look. This function utilizes the well known Pythonism known as *keyword arguments*, often seen as `**kwargs` in the wild. To call the function in the previous `user()` function example and still get the same effect, you'd do this:

```python
@app.route('/user/<username>')
def user(username):
    return render_template("user.html", username=username)
```

In this example, we indicate which template we want Jinja to render and also pass in our `name` parameter along to Jinja. The `name` on the left side of the `=` is what Jinja will use as the placeholder name inside the template. The other `name` on the right side is the variable in the function scope. Now when we load the `user.html` template, we'll see—whah!? You say you haven't made such a template yet that can handle this passed-in variable? Oh dear, let's take care of that right away!
