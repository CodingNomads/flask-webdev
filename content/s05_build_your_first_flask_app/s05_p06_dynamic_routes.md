How'd you feel about the basics of routes? There's much more, but for now let's introduce you to dynamic routes, then you can take a shot at making a few more yourself for some practice. Haven't you ever noticed that when browsing SoundCloud or Facebook, whenever you checked out some random guy's profile that you could see something like these in the address?

```
www.example.com/user/random_guy
www.example.com/user/someones_grandma
www.example.com/user/Tom
```

All those users pages have a similar structure, where you can see the user's pic, a bit of info, and some stuff they decided to upload or share. In these types of pages, the underlying *template* contains that *static* structure, and then loads the content *dynamically* based on the user (random_guy, someones_grandma, or Tom). There are other kinds of dynamic pages, too.

Now here's something for you to play around with. To make a *dynamic route* in Flask, you surround the dynamic part of the **path** in angle brackets. Let's see an example:

```python
@app.route('/user/<username>')
def user(username):
    return f"Hello, {username}!"
```

Go ahead and try this in your `hello.py`. So what's going on here? When Flask determines that there's angle brackets surrounding part(s) of the path, it expects to see the same token in the list of arguments for the view function. For this example, when you navigate to `localhost:5000/user/Tom`, you'll see "Hello, Tom!"

Now try a few of your own dynamic routes. Try these suggestions:

- Use two dynamic arguments in a view function (ex: name and age)
- Make another view function that takes a numeric dynamic argument. Return the square of the number in the response
- Try a dynamic argument with spaces and see what happens

[//]: # (I have no idea what would happen for number 3 lol yet)

---

<div class="alert alert-warning" role="alert"><strong>Note: </strong>Some of the examples in this course won't be part of the main app, but you'll make it clear when it is or isn't.
</div>
