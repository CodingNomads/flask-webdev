Your application factory is ready to churn out applications, but there's but one problem: they don't have routes! In this lesson, you'll learn about Blueprints.

### No More Routes

With the application factory you made in the last lesson, it's become more complicated to define routes and even error handlers. Once you get an application with `create_app()`, by that point it is too late! There *is* actually a way to use the `app.route` decorator to define routes directly inside your `create_app()` function. However, it's not pretty, and kind of defeats the purpose of having modularity.

Luckily, the developers of Flask thought ahead and came up with **blueprints**. Think of a blueprint as a "mini-app". Just like a Flask application, you can define routes to implement the behavior of your application, with view functions that get called whenever certain requests are received. However, a blueprint will do *nothing* until it is **registered** with an actual Flask application. In this respect, blueprints get "activated" as part of the application once they get registered, and only then. Think of a blueprint like a mouse or a keyboard you plug into a computer. They don't work if they aren't plugged in, but once they do and "register" with the computer, they work!

Another great thing about blueprints is that they can implement separate bits of functionality to keep your code clean and organized. For example, you can have one that implements most of the user-facing pages, another that handles authentication and registration of accounts, and yet another that defines the Application Programming Interface (API) for your app. You can define a blueprint in a single file, or better yet, inside a package.

Opting for blueprints defined in packages makes for better flexibility, so that's what you're gonna do. In fact, you'll make a subpackage inside the `app/` package. Head over to the next lesson to start making your first one!
