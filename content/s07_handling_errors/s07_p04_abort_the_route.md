Whenever you might need to signal to the browser that some mistake happened, you can use the `abort()` helper function. What this does is it essentially raises an exception. Think of it like throwing an exception in normal Python code, except an `abort()` is for doing it with a Flask webserver.

We don't need it for our project at this point, but it will become useful later. Here's a quick example: Let's say you have a user loader function called `load_user()` that takes an ID and gives back a user object. If that user doesn't exist, you can signal an error with an `abort()`:

```python
from flask import abort()

@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort()(404)
    return f"<h1>Hello, {user}!</h1>"
```

In the case that a user with that ID doesn't exist, the view function will skip returning a response. That's because the `abort()` function raises an exception. The number passed in is the status code. When the `abort()` is called, what ultimately happens is that control is passed to the error handler that handles that status code. If you were to use this code and hit the `abort()`, your code would then render your `error.html` template with a "Not Found" message because the `page_not_found()` view function would get called.