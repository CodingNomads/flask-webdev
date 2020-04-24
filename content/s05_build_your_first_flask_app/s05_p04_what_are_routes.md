### More About Paths

Now that you know about requests and responses, it's time to understand what Flask routes are and how to use them. You learned about how paths are the determining factor in *how* a request is handled.

The path tells the server what the user *really* wants. Well, not what his or her inner desires are, but it does tell the server where it needs to go to get the user the right response. More specifically, it lets the server know which *section of code* should be run to return the correct response. When visiting our imaginary website and going to the "about" page in *example.com/about*, the server finds the code for `about` and runs it.

### Routes and View Functions in Flask

The same is true for a Flask web server, and every Flask application instance has an association between the path and the section of code a.k.a. the *handler* (mentioned previously) that will handle the request. Each mapping of a path to its associated handler is called a **route**. So when you use the `app.route` decorator, you're defining a mapping from a path to the **view function** (the decorated function) that will be called when a user visits that URL. If you happened to use Flask to make our example.com website, you could write the following to handle the request for the "about" page:

```python
@app.route('/about')
def about_us():
    return "<p>A blurb about this website</p>"
```

Pretty cool, huh? In fact, the `app.route` decorator is a "shorthand" way of using the `app.add_url_rule()` method that Flask also provides. This function takes 3 arguments. In order, they are: the path, the endpoint name, and the view function. The equivalent code using `add_url_rule` would be:

```python
def about_us():
    return "<p>A blurb about this website</p>"

app.add_url_rule('/about', 'about_us', about_us)
```

The endpoint name is simply the symbolic name you can use to reference the view function from other parts of your app. Flask by default will make the endpoint name the same as the name of the view function it references, as you can tell above.

Did you also notice the `<p>` HTML tags in the response? It's no surprise since that's what websites display for their users! A bunch of HTML.

For this course, you'll mostly be working with `localhost:5000` as your website (where 5000 is the port), so an about page would be at `localhost:5000/about`. Now, aren't you just itching to make some of your own routes with all the knowledge you now have? Go get 'em, tiger! Afterwards, you be fleshing out your pages with templates and Jinja.

[//]: # (TODO: At some point, may need to talk about application  and request contexts)
