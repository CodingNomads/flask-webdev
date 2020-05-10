If you're reading this, then you're probably curious about Flask-WTF and why it's called that, or you just happen to be taking the CodingNomads Flask course and are about to learn how to make forms with the Flask-WTF framework, or both. Either way, you've come to the right place!

Flask-WTF did not get it's name from people screaming "WTF!" when working with it, instead it comes from the <a href="https://wtforms.readthedocs.io/en/stable/" target="_blank">WTForms</a> library, which is what the Flask-WTF extension is based on. Making forms will instead cause you to scream "Flask-WTF FTW (For the win)!" because it's actually quite a pleasant experience.

The days of tediously writing HTML code for generating forms is over. Flask-WTF gives you the ability to define forms *in Python* and instantly render them in a template. You can define various validators, including *custom* ones that can, for example, make sure you didn't type `2` + `2` = `chair`

To get you off to a running start, you'll obviously have to install Flask-WTF, but that's easy:

```bash
(env) $ pip install flask-wtf
```

Assuming that went without a hitch, you might be thinking about the next step. "Oh, now I have to initialize Flask-WTF, right? Like I did for that Bootstrap thing. Y'know, `Bootstrap(app)`"

Hold your horses, bucko. Flask-WTF doesn't actually need to be initialized! But there's still one quick thing we need to do. If you want complete secrecy as to your own favorite flavor of ice cream, to only confide it to the server and no one else, the framework has to make sure the data you send is *encrypted*. To enable that secrecy, you need a **secret key**. You can configure this right in your `hello.py` file:

```python
app = Flask(__name__)
app.config['SECRET_KEY'] = "keep it secret, keep it safe"
```

So what's this `app.config` thing? Your `Flask` application object has a built in, general-purpose dictionary to store all kinds of configuration variables. This dictionary is used by Flask, extensions, and you can even utilize it for your own application's purposes. You can define values in the `config` dictionary at the start of your program, or you can import values straight from a file or from the environment which you'll do later.

Did you type in that exact string, `"keep it secret, keep it safe"`? While it might be fine for your first Flask project, you should *never* use the same key for one of your more serious apps, nor should you upload your secret key to source control. More will be covered about how to keep your secret key *a secret*, but for now you can continue with this string or with another totally made up string, like `"T0mmy wrot3 a poem_about butterflies"` or even better, `"93c9fd51b6f68d8cf88185656b4f2eb3815819"`.

![Ssshhhhhh finger to mouth](https://images.unsplash.com/photo-1483706600674-e0c87d3fe85b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1382&q=80)

Why all this rambling about secrets and security? Well, it's important your or your users' information is safe. By defining your secret key, you will 1) make Flask-WTF happy and 2) protect your forms against nasty cross-site request forgery (CSRF) attacks. Flask-WTF uses that security key to generate security tokens for every form, which are then stored in the user session. That precious, private information in the user session is only accessible with the secret key, so that's why it's so secret! To learn more about secret keys in Flask, check out <a href="https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions" target="_blank">this link</a>.

How does one *form* a form with Flask-WTF? The answer to this question shall be answered in the next lesson!
