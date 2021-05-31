### Accessing Content On The Web

By this point, you and your users will have the ability to create lots of content on your website! Users, compositions, and comments galore. Content means information, which may be valuable to people who use or interact with your website. However, right now the only way for someone to access all the information is by navigating to the site, logging in, and manually clicking around to get the information the user seeks. You and I are tech-minded people; we live in the 21st century, so there's gotta be a better way, a *programmatic* way, to get information from your site... right?

Of course there is! Most modern, well-known webapps have something called an **Application Programming Interface (API)** which allow developers, or *clients*, to query for information about the site's content, and even add or edit content as allowed by the webapp, or *server*. From the server side (that means you), there's a lot to consider in carefully providing this content from your own API, like permissions, error handling, and serializing the data. The good news is you've already done much of this in the course already, but there is a bit of extra work that must be done to integrate permissions, error handling, and the like with an API. You'll learn more about it in this section.

### API For Your Webapp

The next few lessons will show you how to implement your Flask app's **REST** API. REST is an architecture for accessing and providing *resources* in a stateless manner.

If you're not yet familiar with REST,interacting with APIs using Python, or API's in general, then please go through the first half of CodingNomad's free <a href="https://platform.codingnomads.co/learn/course/view.php?id=20" target="_blank">APIs and Databases in Python</a> online course. Once you do that, you'll be ready to make your own API for your webapp!
