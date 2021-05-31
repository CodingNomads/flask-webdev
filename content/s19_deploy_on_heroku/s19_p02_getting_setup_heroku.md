There are only a few things you need to do in order to get started with Heroku. Check out their tutorials and:

- <a href="https://signup.heroku.com/dc" target="_blank">Create a free account</a>
- <a href="https://devcenter.heroku.com/articles/getting-started-with-python#set-up" target="_blank">Install the Heroku CLI</a>
- <a href="https://devcenter.heroku.com/articles/creating-apps" target="_blank">Create your app on Heroku</a>

After you have created your free account and <a href="https://devcenter.heroku.com/articles/heroku-cli" target="_blank">installed the Heroku CLI</a>, e.g. via:

```bash
# macOS
$ brew install heroku/brew/heroku
# Ubuntu
$ sudo snap install --classic heroku
```

you can then log in to your account through the CLI:

```bash
$ heroku login
```

It will prompt you to login through your browser. One last thing, if you have already been committing your code through `git`, then you can connect your repo to Heroku. This is done with:

```bash
$ heroku create <appname>
```

The `<appname>` can be anything that isn't already taken, as it must be unique all across Heroku. A couple ideas for you: `flask-webdev-<your initials>`, `ragtime <your name>`

Even if you aren't quite ready to do that last step, there's still plenty of time to learn the basics in the next few lessons. You are already well on your way to deploying your Flask app to Heroku. But first let's talk about **secrets**.
