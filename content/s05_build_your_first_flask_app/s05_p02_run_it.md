### Running The Code Again, With A Twist

You now have your 7-or-so line `hello.py` file and I'm sure you're wondering what to do with it and how to get it running as a web app. It's not quite as simple as using an online development tool like Repl.it, since now you're in a real web development scenario, but this page will get you on your way!

You may even be thinking, "Hey wait a sec, didn't you leave something out in that file? That `app.run()` thing?" (Thinking in code, I love it!)

Ah, you'd be right. There was such a `app.run()` function in the example a couple sections ago, but you don't actually need it this time. Isadora might be a fortune teller, but can she see why developers love web development using Flask?

<iframe width="560" height="315" src="https://www.youtube.com/embed/rieerSvSYWM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Well one, it's because Flask can get them up and running lickety-split (as you've seen), but another is because Flask makes it *convenient* to develop with. You truly have a working app inside `hello.py`, but for now it is just text. Even running `python hello.py` will do seemingly nothing. But in fact, it has its very own development web server hidden inside, all waiting to come out with a simple command! Not even a fortune teller could've figured that out at first glance.

To be able to kick off this web server, all that Flask needs from you is for you to set the `FLASK_APP` environment variable. This setting let's Flask know the name of the file where the application instance lives. In other words, the file specified is one you want to test, debug, or otherwise just appreciate. With that said, in your CLI, type and execute the following (keeping the spacing as it is):

```bash
(env) $ export FLASK_APP=hello.py
```

Now hold your breath, you're about to launch your web app as if by magic. Next, type in these two words and imagine they have the same effect as the words "hocus pocus":

```bash
(env) $ flask run
 * Serving Flask app "hello.py"
 ...
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
If you see output similar to the above, your magic trick... er, the command worked! Open up your favorite browser and navigate to `localhost:5000` and you'll be greeted with a "Hello Web World!"

### Running Flask for Development

You might see an ominous warning regarding production deployment; that's because Flask by default runs in "production" mode, but that's not what should usually be used for development. Instead, you can set another environment variable:

```bash
(env) $ export FLASK_ENV=development
```

With that set, the next time you try `flask run`, it will show as running in a development environment. This will also automatically enable debug mode. Regardless of the environment, debug mode can be set separately with:

```bash
(env) $ export FLASK_DEBUG=1
```

With debug mode enabled, you'll get to utilize two very convenient modules:

- **Reloader** - It's pretty nifty. With this, Flask will scan all your source files for changes and will automatically restart the server if it detects that any of them have been modified. That means whenever you have a server running and you modify a line or two in a file and save it, you'll see from your terminal that your server will restart, which means it has already accounted for the changes you made. Told ya it was nifty!
- **Debugger** - Whenever one of those changes might break your web app, Flask has this other cool feature that will display whatever error it encountered *right in your webpage*. That is, instead of an ugly page that gives you nothing to go by to fix the error. Even more swell is the fact that you can interact with this page and see the source code that may have caused the problem.

<div class="alert alert-warning" role="alert"><strong>Note: </strong>All this boring command line stuff is actually pretty important. Flask's debug modes even screwed me up when I was developing! So if it helps you, definitely write some of this down to commit it to memory. It may be helpful to bookmark this page, too.
</div>

You can also get some documentation for Flask commands with `--help`, for example, `flask --help` or `flask run --help`

<div class="alert alert-warning" role="alert"><strong>Note: </strong>While you <i>can</i> still use <code>app.run()</code> for bringing up your Flask app, keep in mind that setting <code>FLASK_APP</code>, <code>FLASK_DEBUG</code>, and <code>FLASK_ENV</code> environment variables won't have any effect if you go that route (pun intended).
</div>


Now that you've learned the nitty-gritty of development using Flask, and since you already have the grit it takes to be a Flask developer, you're set to keep going with your app. But first, an existential question... what are URLs, anyway?