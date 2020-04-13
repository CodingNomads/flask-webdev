Now that you know what kinds of errors people encounter, you're ready to define your own error handlers. You've been told about handlers previously, but **error handlers** in Flask are a little different from the ones you've seen so far.

With these handlers, you'll use the Flask `errorhandler` decorator instead of `route`. This new decorator requires one argument, which is the status code it is tasked with handling. Go ahead and whip out your code editor to `hello.py` and type this in.

```python
@app.errorhandler(404)
def page_not_found(e):
    error_title = "Not Found"
    error_msg = "That page doesn't exist"
    return render_template('error.html',
                           error_title=error_title,error_msg=error_msg), 404


@app.errorhandler(500)
def internal_server_error(e):
    error_title = "Internal Server Error"
    error_msg = "Sorry, we seem to be experiencing some technical difficulties"
    return render_template("error.html",
                           error_title=error_title,
                           error_msg=error_msg), 500
```

Now obviously you can't just go to your browser now and type in `localhost:5000/500`. That won't work like it did with `route`! (You'll get yet another error, go figure.) But do notice that like with a `route`, it still needs to return a response. and the one here passes in a couple keyword arguments to the template. What's different here is that there's also the status code, again, as a second return value.

Responses in Flask by default return 200, but if you explicitly need to return a different status code, it can be passed as a second argument. Yes, that means your error handlers have to return the number they are supposed to handle.

You're anxious to be able to see the result of your new handlers, aren't you? Of course, of course. You'll need to define that missing `error.html` template.