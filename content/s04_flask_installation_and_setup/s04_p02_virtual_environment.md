Once you have Python installed, it's time to set up a virtual environment. It's important to keep the project's dependencies and libraries contained in a virtual environment, so that you can develop your first Flask app without worrying about those pesky library clashes. Throughout this course, you'll be using the `venv` python module to create virtual environments.

If you aren't already there, go ahead and change your directory to your `flask-webdev` project folder. It would look something like this if you followed the folder structure instructions up to this point:

```bash
$ cd ~/Documents/CodingNomads/projects/flask-webdev
```

Then in the command line use Python to create your virtual environment:

```python
$ python3 -m venv env
```

The choice is yours in what to name your virtual environment folder. In this case, the name `env` is used. Now all you'll need to do is "activate" the virtual environment. In your command line, type:

```bash
$ source env/bin/activate
```

_ACTIVATED!_

With your environment activated, you should see `(env)` at the beginning of your terminal input. Remember, you'll want to activate your virtual environment *every time you begin work on your project*! All the dependencies and packages you'll need will be packed in the virtual environment as you continue developing.

Now for the moment you've been (very patiently) waiting for: installing Flask! Just one more click to the next part...