[//]: # (microblog uses routes.py not views.py, which might be important later)

Now give you an idea of just how lightweight Flask can be, let's go ahead and open up the <a href="https://github.com/miguelgrinberg/microblog/" target="_blank">source code</a> of Microblog. Remember, don't feel too worried about knowing anything about how it works yet! You will learn all of it (and probably more!) in this course.

Once you click the link above, you won't have to focus on anything more than the list of files and folders. In case you're not familiar with Github, they start below Miguel's thumbnail picture and have dates associated with them.

Now you might be looking at all those files and folders, and you're wondering where to start. That will be left up to you! However, here are some guideposts to help you get a feeling for what you're looking at:

- `app` folder - this is where the entirety of the web app lives!
  - `api` folder - The files here define how the site can be interacted with, like for grabbing data from the site
  - `auth` folder - Files that determine how the users of Microblog login and register, and what they can and can't do
  - `errors` folder - Definition of possible HTTP errors encountered on Mi
  - `main` folder - As you can probably tell, this is where the most of the important functionality goes
  - `static` folder - This is where images for the site go, but some CSS styling and JavaScript files could also go here
  - `templates` folder - Basically this is all the HTML that defines the structure of the website
- `deployment` folder - This defines how microblog is configured for when it gets deployed (to the site you just tried out previously!)
- `migrations` folder - This folder contains scripts for upgrading (and downgrading) the database as the site gets developed
- `config.py` - Where configuration options for the Microblog app get set, like database and email options
- `microblog.py` - The web app gets instantiated here and becomes the Flask application instance

So go ahead, be curious. But don't get too lost, because remember, all of it will be addressed in the course. As you explore, make sure you click the link to the file or folder itself, and not the commit message to the right of it.

![Pic to show just that](../images/code_folder_circled.png)

That's it! Right here in the __ folders and __ files is an entire web app. The amazing part? You can actually go much smaller: an app in only *one* file. In the next section, you'll actually build this web app yourself!