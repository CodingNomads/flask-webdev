Now that you've done a whole bunch of template stuff, what if something goes wrong? If you type in a bad address or misspelled one of your routes, you probably got an ominous "Not Found" error. Or even an "Internal Server Error." Let's demystify all that stuff, plus you'll get to make your own template for errors. It will show up whenever you, your Flask server, or some user runs into a mini-mishap.

### HTTP Errors

Although you may not want to admit it, you've seen them. Errors. Even some you've made yourself. Well that's okay, because the internet is full of **HTTP errors**, but the internet (usually) still works just fine. Websites have all kinds of ways to show you when an error has occurred on their site. But what are these "errors?" Turns out they are just numbers, at least to a server, and your app will be no different. Here's a table of the **status codes** you've probably come across.

| Error                 |   HTML Status Code |
|-----------------------|--------------------|
| Forbidden             |    403             |
| Not Found             |    404             |
| Internal Server Error |    500             |

When you hit a "Not Found" error, that just means you went to a page that the server can't give you because, well, it can't find it! Whenever that happens, the HTTP response includes a status code of 404. "Internal Server Error" means the server got into a mess on its own and can't show you whatever you wanted to see, and the HTTP response includes status code 500. The "Forbidden" error? That's forbidden to talk about... but if you really must know, it means you don't have the ability to see it, and the HTTP status code is 403.

___

In the next sections, you'll build the routes needed to process these errors and the templates to show them. No one likes ominous messages like "404 not found"! Yikes. We can fix those easily with just a few more with templates and routes.
