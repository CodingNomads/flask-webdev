So what is this "microframework" buzzword that gets thrown around in the technical community? Before answering that question, let's first talk about web apps in general and how they work.

Much of the web apps you have probably used are full-fledged web apps with user authentication, forms with input validation, and database access. These are called full-stack frameworks, and are used by large enterprises like Twitter and Microsoft. These frameworks have both the frontend--what the user sees and interacts with--and a backend, which does all the work behind the scenes including data access.

In short, "microframework" really just means "minimalistic web application framework." A microframework is much simpler than a full-stack framework in that it does one thing and it does it very well, and that is to provide a server that users can access just like they would any other website, i.e. get a request from the user and return a response. However, these frameworks *don't* have all the bells and whistles like user authentication or a fancy user interface.

But for a developer like yourself, this is actually great news. With a microframework, you have full control over your app. You get to pick how the users will login, the inputs they can use, and which underlying database technology to use, all built around the microframework. It makes build a web app easy, but also allows you to scale up easily to provide more complex functionality.

Think of a microframework as a flat LEGO base plate and the basic rectangular bricks that might come with a set.

![alt_text](https://images.unsplash.com/photo-1577113398331-d843d3341a63?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1567&q=80)

You can put bricks on it, you can take bricks off of it, and you can build an ugly multicolored house; you have the basics to build basic things right off the bat. Now the fun begins when you get sets like knights and castles, spaceships and astronauts, or cowboys. You could just use one set on that base plate, *or* you could combine any or all of them as you want, like knights fighting cowboy astronauts in galactic castles.

Flask is a microframework, and you'll spend this whole course learning the ins and outs of Flask along with a few of these "bells and whistles" that allow us to build a pretty cool app.