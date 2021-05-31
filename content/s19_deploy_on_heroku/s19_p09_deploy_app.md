Heroku has a seamless integration with Git, which gives you an easy way to deploy your app that works well with a normal development workflow. There's four things you need to do:

- Put your project code under version control with Git
- Create a Heroku app
- Add a remote named `heroku` to your repository
- Push your code to the `heroku` remote

Let's look at each of these steps one after another. You may not need to do some of them anymore, depending on how you set up your project so far. You can read more in Heroku's guide on <a href='https://devcenter.heroku.com/articles/git' target='_blank'>Deploying With Git</a>.

### Git Version Control

Assuming you've been closely following along, you already have your project under version control with git. But if you haven't yet put your project under version control, *now* is the time to do so. Go to the root folder of your project in your terminal, then type:

```bash
$ git init
```

Add and commit everything, *except* any files containing sensitive information. Your project is now under version control. Yay! If you need a Git refresher, check out the link in the Prerequisites section at the beginning of this course.

### Create A Heroku App

You might have done this a few pages back, but if not, you can either create a Heroku app <a href='https://dashboard.heroku.com/apps' target='_blank'>from your Heroku Dashboard</a>, or <a href='https://devcenter.heroku.com/articles/creating-apps' target='_blank'>from the Heroku CLI</a>. In this step, you can give your app a **name**.

<div class='alert alert-info' role='alert'>
    <strong>Info:</strong> The name you give to your Heroku app in this step will be part of the URL that your webapp will be accessible at: <code>https://your-app-name.herokuapp.com</code> Choose something you can remember, but keep in mind that the name must not be in use yet. Heroku will inform you if the app name is not available.
</div>

The easiest is to type the following command again from the root project folder that you moved into when initiating your Git repository:

```bash
$ heroku create your-app-name
```

Replace `your-app-name` with the name of the app you want to use. It needs to be available for the app to get created successfully.

### Add The `heroku` Remote

If you created the app via the Heroku CLI as described above, you can skip this step, as Heroku already completed it for you. To check, run the command `git remote -v` and you should see a remote called heroku:

```
heroku  https://git.heroku.com/<your-app-name>.git (fetch)
heroku  https://git.heroku.com/<your-app-name>.git (push)
```

<a href='https://devcenter.heroku.com/articles/git#for-an-existing-heroku-app' target='_blank'>Check the docs</a> for how to link a `heroku` remote of your Git repository to a Heroku app you created through the Dashboard instead.

### Push Your Code

The final step is pushing your code to the `heroku` remote in the same way you would push to the `origin` remote on GitHub:

```bash
$ git push heroku master
```

This will **push and deploy** your webapp on Heroku under the `https://your-app-name.herokuapp.com`. You can watch the deployment process take place in your command-line. Once it is finished, the CLI will also show you the URL that your webapp has just been deployed to. *But hold your Heroku horses!*

#### Run Deploy Tasks

By this point your app is *technically* deployed, however you need to initiate the `deploy` command that you created in the last lesson. To do that, you use the `heroku run` command:

```bash
$ heroku run flask deploy
```

Then to make sure you have a clean start with a newly created/upgraded database, you'll want to restart your deployed app:

```bash
$ heroku restart
```

Okay okay, yes, *now* you can try that link to your app, or copy-paste it into your browser, and you're finally ready to see your webapp live on the internet! You can share this link with anyone on the web, and they will now be able to access your page. Well done, your app is open for the world to see! :D

### *GAH!* Something Went Wrong

Is your app showing an error, acting weirdly, or just plain not showing up? Here are a few ways you can go about debugging your deployment:

1. **Check the logs**
    Heroku allows you to see your deployed app's log messages both directly from the terminal, or through the Heroku Dashboard on their website. To check the logs, use:

    ```bash
    # optional: use -t to continually receive incoming messages
    $ heroku logs [-t]
    ```

2. **Try running locally**
    The Heroku CLI comes with a neat feature: `heroku local` allows you to "dry run" your deployment by running the application locally in a similar way to how would Heroku run your app on its own servers. You'll need to set up the environment variables yourself, however, as Heroku won't grab them for you. This command will look for a top-level `.env` file that contains your environment variables and their values:

    ```
    FLASK_APP=ragtime.py
    FLASK_CONFIG=heroku
    MAIL_USERNAME=<your-gmail-username>
    MAIL_PASSWORD=<your-gmail-password>
    ```

    <div class="alert alert-warning" role="alert"><strong>Note: </strong>Remember not to commit this file to version control! You can add a line to your `.gitignore` to ignore the `.env` file.</div>

    But just like setting your app up on Heroku, you'll need to run the `deploy` command. Afterwards, you can then run it locally:

    ```powershell
    $ heroku local:run flask deploy
    $ heroku local
    ```

3. **Check (un)committed files**
    Perhaps you missed something and didn't push that *one* file needed for your app to work. Could it be you didn't commit your entire `migrations` folder? Or maybe you forgot that latest change to `app/__init__.py`.

___

If you've tried every feature of your Internet-facing app and it all works, great job! You've successfully deployed your app.

<img alt="rocket" title="rocket" class="img-responsive cn_image" src="https://github.com/CodingNomads/static/blob/main/flask-webdev/imgs/rocket.jpg?raw=true">
