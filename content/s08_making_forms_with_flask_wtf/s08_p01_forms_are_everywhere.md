### Forms Are Everywhere

[//]: # (Note about "user", "client", and "browser" may be used interchangeably in this section/course?)

Forms, those blank bits of information you fill in once in a while. They are everywhere! Each year, I have have to fill out tax forms and give them to the Internal Revenue Service. Definitely not as fun as web forms, which are on pretty much all of the websites you visit.

You've been getting familiar with how to make new routes in Flask, how to flesh out those routes with templates, and how to present any errors should something go wrong. But all of those things are the *user* getting information from the *server*. Obviously, there is use in telling the website *some* information about you, right? Like getting your email and password to login, or getting your search terms, or sharing what your favorite K-Pop band is.

That's where **web forms** come in. These things are as old as the internet and you can even make them with basic HTML. A user enters their information and once they submit it, the data goes from the web browser to the server in the form of a **POST request**. The POST request contains the user information and gives the server access to that information. In your case, the server will be Flask. These POST requests will contain things like login info and personal details and favorite flavor of ice cream. POST requests will be covered more later in this section, but think of a POST request like the user sending a postcard (submitting the form) to a mailbox (the server).

![Mailboxes](https://images.unsplash.com/photo-1521575107034-e0fa0b594529?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1948&q=80)

Making form components with HTML is straightforward, but then there's validating. For example, "wood" isn't exactly a flavor of ice cream... and hang on, how do we get all this functionality using Python?

For that there is Flask-WTF! Don't let the name fool you, as it makes the making of forms pretty darn easy and painless. You'll learn about this tool in the next lesson.
