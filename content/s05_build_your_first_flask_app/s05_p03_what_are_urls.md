[//]: # (Source https://www.youtube.com/watch?v=4r6WdaY3SOA)
[//]: # (Source https://en.wikipedia.org/wiki/URL)

### What's A URL?

URL. Does it stand for Unilateral Reasonable Logic? Underwater Respiratory Loophole? ...Unicycle Redundancy League?

Well, maybe. Who knows? However, when we're talking about the web, URL stands for Uniform Resource Locator. Honestly that sounds somewhat cooler than those other things, but really it's the same as a *web address*, say, like this one:

```http://example.com/```

That web address let's you see what *web resources* the server has that it can show you. That is, assuming of course that you have a connection to that server.

Let's think of a simple website, our imaginary *example.com*. The website has two main parts: the "front end," which is the part of the website that the user sees, and the "back end," which is everything else behind the scenes. As Flask web developers, we are mostly concerned with the back end because ultimately it's the server that must determine what the user gets to see.

### Requests and Responses

So when a user navigates to a webpage, like *example.com*, a *request* is sent from the user to the web server which basically says, "Hey web server for *example.com*, I'd like to see what information you have for me at this web address!" The request then gets *processed* by the server, which then provides the user (their browser, likely) with a *response*. Think of it like that game you used to play as a kid with the two tin cans and a string; one of your friends would send a *request* and you'd give them back a *response* after you thought about it.

[//]: # (diagram here)

![](../images/request_response.png)

The first part of the address, `https://` or `http://`, is the protocol and tells the server whether the request is encrypted or not, respectively. The next part, `example.com`, is the *domain name* or *host* and tells the Internet which server to send the request *to*; in other words, the server the handles requests for website `example.com`. But neither of those really have much effect in *how* a user request is responded to by a server. Wait a sec, so what's left of our web address that *does* have an effect? There's nothing left in our example!

Well, it turns out there is, and we saw it in the last lesson. The  *path* is the part of the URL that points to the actual location of the web resource. It's like a path on your computer, where */home/you/Pictures/corn_flakes* is the album of your corn flake collection (everyone has one of those, right?). If we go to *http://example.com/about*, the path is `/about`. For our original example, *htpp://example.com/*, the path is just `/` which indicates the root path.

So then what's the `route` stuff that Flask uses? Tune in next time for another episode of "Flask Web Development" to find out! Or just click to go to the next lesson. That works, too.