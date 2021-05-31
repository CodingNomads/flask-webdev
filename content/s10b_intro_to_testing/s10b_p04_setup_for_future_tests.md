
In the last lesson, you learned that there are a few tasks that may be common across tests. This lesson will get you set up for future testing of your Flask app, and will also introduce you to the concept of test fixtures.

___

### Test Setup

While there's not a whole lot in your app to test right now, it's still important that you know where you'll put your tests in your project. Here's what your `tests/` folder setup will look like:

[//]: # (TODO: Might include "functional" folder later)

```
app/
└── ...
migrations/
└── ...
tests/
├── conftest.py
└── unit/
    ├── __init__.py
    └── test_app.py
# all your other files...
```

The `unit` folder holds all your unit test files. You can have as many files in this folder as you want or need. The `unit` folder has an `__init__.py` file to make it package, which is generally a good practice when using multiple test folders with pytest. From Pytest official <a href="https://docs.pytest.org/en/stable/goodpractices.html#choosing-a-test-layout-import-rules" target="_blank">documentation</a>:

> If you need to have test modules with the same name, you might add `__init__.py` files to your tests folder and subfolders, changing them to packages.

Also notice that your `test_app.py` file will be moved to the `unit/` folder.

Then the `conftest.py` file is the place to *configure* your test setup with things like test fixtures. You'll learn more about `conftest.py` in a bit; for now it's fine if it's empty. Let's first talk about how you'll start your tests with this new file structure.

#### Starting Your Tests

While it takes little effort for pytest to do its magic, it still needs a little help sometimes. But now you will have all your test code in one folder called `tests/`. In a way it makes things easier, but there's still a bit of a challenge. Because of your file structure with tests in the top-level `tests/` folder and `app/` containing most of your app's logic, it takes some up-front configuration to get pytest working properly.

Generally, all you need to do in this case is to give pytest the name of the directory where the tests are, e.g. `tests/`, from the top level directory:

```bash
(env) $ python -m pytest tests/
```

#### VSCode Launch Configuration

If you're using VSCode, you can use this as a launch configuration for running tests:

```json
{
    "name": "Python: Test All",
    "type": "python",
    "request": "launch",
    "module": "pytest",
    "env": {
        "DATABASE_TEST_URL": "sqlite:///${workspaceFolder}/data-test.sqlite",
        "PYTHONPATH": ". tests"
    },
    "args": [
        "${workspaceFolder}/tests/",
        "--show-capture=stdout",
    ]
}
```

The `${workspaceFolder}` is a variable set by VSCode that holds the location of folder you're working in. If you have your project folder open in VSCode, then this is the location of your project folder. So the `DATABASE_TEST_URL` environment variable is set to the location of your `data-test.sqlite` file. If the file doesn't exist yet, it will be created when your test database's tables are first created.

You'll notice that `PYTHONPATH` is set here as well. This sets it to current directory and additionally your `tests` directory.

<img alt="PYTHONPATH" title="PYTHONPATH" class="img-responsive cn_image" src="https://github.com/CodingNomads/static/blob/main/flask-webdev/imgs/path.png?raw=true">

___

You should be good to launch your tests if you've made it this far. In the next lesson, you'll learn about how to use fixtures to create reusable chunks of test code.
