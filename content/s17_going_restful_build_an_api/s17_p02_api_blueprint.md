To get you started with developing your API in Flask, you'll first need to create a blueprint for your API, which this lesson will task you with.

### API Blueprint Instructions

#### Create and Register

The API blueprint will live in `app/api`. Create this directory and create a blueprint `api`. 

Register your blueprint just like you did for your other ones. **Important:** set your new blueprint's `url_prefix` as `/api/v1`.

<div class="alert alert-info" role="alert"><b>Info: </b>Commonly, an API has different versions as the API goes through updates and enhancements, with the old API version still in place so that other peoples' apps that interface with the API don't immediately break. The <code>v1</code> just means this is version one of your API. If you come out with a new one, you can keep the old version in place and also have a new, fancier version.</div>

#### Add Other Modules

While you're at it, make these other files as part of your API blueprint:

```
api/
├── __init__.py (your blueprint creation)
├── authentication.py
├── comments.py
├── compositions.py
├── decorators.py
├── errors.py
└── users.py
```

Then, import all but `decorators.py` within your blueprint.

___

Once you've done that, you can move onto Step 2 of the prepwork for your API: error handling.
