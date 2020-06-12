"Email: the way of the future!" -1980's
"Spam. Spam. Spam. Oh, cool, it's from Hobby Lobby!" -Nowish

While email was invented decades ago, it's still around...

The technology behind most email sending and receiving is called Simple Mail Transfer Protocol (SMTP). To keep your life simple, you don't have to get too technical with sending emails via your app. *Behold!* Flask-Mail is an extension that does most of that work for you.

To install it, yet another simple pip command:

```bash
(env) $ pip install flask-mail
```

To add email support to your app, you'll only need two things:

1. An SMTP server
2. Settings configured for that server

As for the SMTP server, you *could* host one yourself. However, for development, it's *much* easier to use an external server. In the next lesson, you'll be guided through the steps to setup a Google Gmail account so you can start playing around with emails right away. You'll learn about the settings in the lesson after that. But first, let's start with getting you set up with a secondary email account!

![](https://images.unsplash.com/photo-1534803522048-835d05301b08?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=700&q=80)
