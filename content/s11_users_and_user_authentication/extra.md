
User Authentication
==========================

Will not use login_required decorator in this section, doesn't make sense to restrict users to plain pages (you don't have fan page yet, let's say)

##### how flask-login works
1. user clicks "Log in" to navigate login page and is presented (by the handler for the URL) with the form
2. User enters info. Upon Submit, same handler is invoked again, but now as a POST instead of GET
    a. Handler validates the creds, then invokes `login_user()` to log user in
    b. login_user() func writes ID of user to USER SESSION (not a const) as a string
    c. view func returns with redirect to homepage
3. browser receives the redirect and requests home page
    a. view func for home is invoked, triggers main Jinja2 template
    b. during rendering of template, a reference to current_user appears for the first time
    c. current_user context variable then invokes `_get_user_()` to find who current user is
    d. `_get_user()` function checks if there's a userID stored in user session. If there's none, returns instance of AnonymousUser. If there is an ID, the `user_loader` decorated function
    e. user_loader handler reads the user from the database and returns it
    f. template receives the newly assigned value of current_user

I'm thinking "Fan" will be confusing at first so I might want to use User for everything else...


##### for testing
Made a tests/ folder for pytest tests. Only had to use `python -m pytest tests/` and then fix the import/module errors to get it to work

NOTE cannot really use `pytest` as the above works well

Fixtures go in conftest.py. Their scope can be defined using `@pytest.fixture(scope='function')` or "module/session/class"

##### more notes on user auth

Password security is no joke because if a breach occurs on your app, you could expose your users' passwords to the attackers. Lots of users use the same password for multiple sites, so that's trouble. So how can you protect your users easily, but effectively?

Need to explain why the development vs production setup is the way it is

brief intro on testing? at this point?

Password hashing is a common solution to this problem. a hashing function takes a plaintext password as input, applies some randomness to it (the salt), then applies several one-way crypto transformations to it. What comes out is a new sequence of characters that look nothing like the original. you use werkzeugs functions for hashing