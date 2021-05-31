Some secrets are meant to stay secret. For your Flask app, these are first and foremost your aptly named `SECRET_KEY`. You've already set this in your own app and as you may remember, it's used to protect your app's user sessions, and it also generates your app's tokens. However, you need to make sure that the `SECRET_KEY` you will be using in production is **not visible** in your code base, especially if you are pushing your code to public version control such as GitHub.

<div class="alert alert-warning" role="alert">
  <strong>Note:</strong> If you accidentally pushed sensitive information to your GitHub account you need to <strong>assume that it is compromised</strong>, even if you notice it right away. There are bots that constantly scrap public GitHub repositories for such information. That means you will need to <strong>change the information</strong>. If it's your password or API key - change it. There's no way around that if you want to stay safe.
</div>

To avoid having to pull your hair and go through stressful damage-control actions, let's rather make sure that your sensitive information stays off the web.

### Local Solutions

To avoid committing sensitive information to version control _in general_, you would take it out of the code that you will register in version control, and instead leave it in a separate file. As always, there are different solutions to this. For example:

[//]: # (environment variables are what you've been doing)

- `secrets.py`: A Python file that declares the variables you use that you import from in your main code. That file is excluded from version control via `.gitignore`.
- **Environment Variables**: You register the variables inside of your virtual environment, most conveniently by exporting them directly inside of your `activate` script. If you do this, they will automatically be loaded every time you activate your virtual environment and are accessible in your code via `os.environ`.
- <a href="https://github.com/theskumar/python-dotenv" target="_blank">`dotenv`</a>: A similar approach, but as a package. It allows you to specify environment variables as simple key-value pairs and load them into your environment to use. It requires installing a separate package, however, and some extra lines of code.

___

These solutions work locally to keep your sensitive bits of information from the prying public eye, but what about your deployed application? Let's see what solution Heroku has come up with for you.
