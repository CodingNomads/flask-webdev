[//]: # (Steps a student would take to build a Flask app in repl.it)

Now, let's get to building your first Flask app. You'll be using an online coding tool called <a href="https://www.repl.it/" target="_blank">Repl.it</a>, where you can write and run your own code from within the browser. If you've never used it before, you type your code in one window, click the run button, then watch it work! You can also pop out your pre-made website address; that address is where you'll be able to see your own Flask app.

Type the following into Repl.it, then try running it and see if you get a "hello" back! Or you can go <a href="https://repl.it/@gigabot/nanoblog" target="_blank">here</a> and try to run it.

```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Web World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```

[//]: # (TODO: Explain basic parts)

<iframe height="800px" width="100%" src="https://repl.it/@gigabot/nanoblog?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

Did it work? If so, then _HOLY FLASK_ you just make your first Flask website! If you haven't already, you could even try making the page say something else. ;)

![](../images/placeholder.png)

[//]: # (Hmm, I know I probably shouldn't just skip over this, but I'll cover it again in section 5 (or I won't and I could skip over it there? Hmmmm.))

But I'm sure you're anxious to get to the *real stuff*. No problem, but you'll have to do just a bit of setup first, but then after that, you'll be all set to start the real training, so let's move on!