In this lesson, you'll learn about the benefits of application factories, configuration files, and blueprints.

### Growing Pains

Having one Python file for your web application can be really nice because all you need to do is go to that file to make your changes. It's very convenient and goes to show the power of Flask, that you can fit everything in one file. The problem is though that it may be harder and harder to figure out where you need to plug in any new functionality, and it becomes harder and harder to maintain.

But another great thing about the Flask web framework is that it doesn't limit you to any specific organization for large projects. That's up to *you* as the developer. It is ultimately your choice for how you want to structure your application. You have spent the time up to now getting used to Flask, how it works, and how you can make it work for you, but now is the time to start thinking of organizing your project to better maintain it. In this section, you will learn just one of many possible structures for organizing your growing web application.

[//]: # (### Why Separating Functionality is Important ### Example of Separating Functionality)

### Application Factory and Configs and Blueprints (Oh My!)

Have you seen the old film, the Wizard of Oz? That's where the line, "lions and tigers and bears, oh my!" comes from. A lost girl named Dorothy, the tin man without a heart, and the scarecrow without a brain met the lion who had no courage. Dorothy wanted to go back home, the tin man wanted a heart, the scarecrow wanted a brain, and the lion wanted courage. So they all worked together to travel to the Wizard of Oz and try to get their wishes granted. Each one had their own strengths that helped them all work together to get to the Wizard. By themselves they couldn't do much, but together they formed a synergy.

![](https://barbarah.files.wordpress.com/2014/12/oz.gif)

As a Flask developer, you'd be remiss not to know about application factories, configuration files, or blueprints. (We've got you covered in this course! ;) ) These things are a lot like the story in the Wizard of Oz film. As individual components of a Flask application, they can't form a complete app. However, when they are used together, they ease *a lot* of the problems you may face as developers. You will learn much more about these components in this section, but to give you an idea of what's to come, let me tell you a story.

Ahem...

>&nbsp;&nbsp;&nbsp;&nbsp;Once upon a time, a developer was met with a deadline. "Oh what am I to do? I have to make a full featured web application for my boss's pickle business in only two weeks! I wish I didn't watch so much Stranger Things." Just then he sees a new file magically pop onto his screen.
>
>&nbsp;&nbsp;&nbsp;&nbsp;"Hi, I'm `config.py!`" said the file, in a notification bubble. "I can help you configure your application with all kinds of options through configuration classes! But without a Flask application instance that can import my classes, I'm of no use." So, the developer and the file got to work, and bring up a Flask application, but they ran into a problem. It was too much work to switch between production and development configurations!
>
>&nbsp;&nbsp;&nbsp;&nbsp;Just when the developer is about to close his laptop in defeat, his screen suddenly glows bright and an application factory shows itself. "Did I hear a lonely, overworked configuration file? Mr. `config.py`, please come work for me! I treat my configs with the utmost respect." Mr. `config.py` was relieved, and the app factory had a new worker, but there was something missing. While applications could be made, they were all lifeless! No routes could be made with the `route()` decorator! All that work the developer did to define routes using the `route()` decorator was for naught.
>
>&nbsp;&nbsp;&nbsp;&nbsp;It was just two days before D-Day (demo day), and the developer was worried. Unexpectedly, several blueprints slipped under the developer's bedroom door. "We heard your routes were global and incompatible with the factory, so we copied your routes into ourselves! Will you accept our business?" The application factory was thrilled to have plans for routes that it could build before the final applications were built.
>
>&nbsp;&nbsp;&nbsp;&nbsp;And with minimal effort from that point on, they all lived happily ever after. Oh, and the developer got a great raise.

___

If you have children, read this to them because I'm sure it will put them to sleep. While they may fall asleep from the story, you've sure learned it's morals! That's why you're ready to learn more about scaling up your application to deal with complexity, so with that, head over to the next lesson.
