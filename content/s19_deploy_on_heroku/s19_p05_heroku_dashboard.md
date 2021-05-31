As you've seen in the previous exercise, Heroku provides a convenient Graphical User Interface that allows you to set, control, and monitor many aspects of your deployed application.

<img alt="heroku dashboard app screenshot" title="heroku dashboard app screenshot" class="img-responsive cn_image" src="https://github.com/CodingNomads/static/blob/main/flask-webdev/imgs/heroku_dashboard.png?raw=true">

This is one of the features of using a PaaS: Heroku picks and decides how to handle your deployment for you, and offers you pre-defined ways to interact with it. The GUI is another feature that makes these interactions more convenient.

Go ahead and access your <a href="https://dashboard.heroku.com/" target="_blank">Heroku Dashboard</a> if you haven't done so in the previous step, and take some time to explore what it has to offer.

Then check out Heroku's <a href="https://devcenter.heroku.com/articles/heroku-dashboard" target="_blank">official learning resource</a> about their dashboard.

---

### Secrets Saved!

Adding your `SECRET_KEY` variable to the config vars, either through the Dashboard or the Heroku CLI, is an important step to getting your Flask app deployed properly. However, there are a few changes you will need to make in order to avoid breaking your app when doing so. Let's look at those on the next page.
