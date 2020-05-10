Up to this point, you have done some practicing with making database models, creating tables, adding rows, and querying your data. Your models are pretty simple, but because applications tend to grow naturally, their databases must grow with them. But what if you need to update your tables?

### What are migrations

Of course you need to add more columns to your database models so that you can build your app. But the problem is, so far, to do that you have to drop all tables and your data goes away. To fix that, you'll support "migration" which is a fancy way of saying, "Make scripts that can make the necessary changes to the database, and that can also _move_ the data you already have as needed." It keeps track of how the database schema changes, which is how all the data is organized collectively. In other words, a database migration framework allows incremental changes to the models to be applied.

Do you know who David Attenborough is? He's the one who narrates all those nature documentaries. Look him up if you don't know, and imagine him narrating about database migrations. Just like animals, databases have to do migrations, too! "See the data in its natural habitat, doing its migrations as usual."

### Flask-Migrate

<a href="https://flask-migrate.readthedocs.io/en/latest/" target="_blank">Flask-Migrate</a>is a Flask extension that is based on <a href="https://alembic.sqlalchemy.org/en/latest/" target="_blank">Alembic</a>, which is a migration framework for SQLAlchemy. Flask-Migrate is an Alembic wrapper built for Flask, and integrates with the `flask` command. Just like any other flask extension, it can be installed like so:

```bash
(env) $ pip install flask-migrate
```

Initialization works a bit differently from other flask extensions. The reason is because Flask-Migrate needs to know what database models it should be helping to migrate! Go ahead and put this in your `hello.py` file:

```python
from flask-migrate import Migrate

# ...

migrate = Migrate(app, db)
```

Now you're ready to get *your database* ready for migration support. Use this CLI command whenever you start work on a new project:

```bash
(env) $ flask db init
```

This command will create a `migrations` directory. You will want to add this directory to your git repository, as it will store all the migration scripts needed to get your database models up to date as you continue with this project.

### When To Perform Migrations

The bottom line is this: you should perform a migration whenever you make changes to your database models. Mainly, this means when you add or remove columns, or if you change the names of tables or add new models and relationships. You can perform a migration from the command line, which will generate a script, but this script may not be completely accurate. You will here more about this, but first, let's talk about **migration scripts**.

Because Flask-Migrate is an Alembic wrapper, the migration scripts it generates are Alembic migration scripts. Each script has two functions called `upgrade()` and `downgrade()`, which apply and remove the database changes that are part of the migration, respectively. Theoretically, you can apply and remove changes means you can reconfigure a database to any point in its change history.

The procedures that one must follow in order for a successful migration:

1. Make whatever changes you need to the model classes
2. Create an automatic migration script with `flask db migrate`
3. Review the script and make any adjustments necessary so that it accurately reflects changes made to models
4. Add the script to source control
5. Finally, run the `flask db upgrade` to apply the migration

The `flask db migrate` command creates a migration script automatically:

```bash
(venv) $ flask db migrate -m "initial migration"
INFO [alembic.migration] Context impl SQLiteImpl.
INFO [alembic.migration] Will assume non-transactional DDL.
INFO [alembic.autogenerate] Detected added table 'roles'
INFO [alembic.autogenerate] Detected added table 'users'
INFO [alembic.autogenerate.compare] Detected added index
'ix_users_username' on '['username']'
Generating /home/yourname/Documents/CodingNomads/projects/flask-webdev/5f15cbadc711_initial_migration.py...done
```

Now for the warning: make sure *ALL* changes to your models are reflected in your migration scripts! Otherwise any `upgrade()` commands won't reflect what changes you ultimately made, and the result might look strange. Automatic migrations aren't always 100%. They can miss some things. If, say, you rename a column, that may not show up in the migration script as a renaming, but rather a deleted column and an added column. That means the migration will delete your original column, and you'll lose all data within it!

### Upgrading Your Database

You have your migration script. It's been review and accepted and checked for any inconsistencies, and now you're ready to upgrade! The `flask db upgrade` command applies the migration script to the database:

```bash
(env) $ flask db upgrade
INFO [alembic.migration] Context impl SQLiteImpl.
INFO [alembic.migration] Will assume non-transactional DDL.
INFO [alembic.migration] Running upgrade None -> 5f15cbadc711, initial migration
```

So what's the difference between an upgrade versus nuking the database and starting fresh with a `db.create_all()`? Well, the difference is with an upgrade, you still have your data, because it makes all the changes like adding columns without removing any content.

You've made it to the end of your primer on databases in a webapp, congratulations! While this section only covered the basics, databases and migrations can get pretty complicated pretty quickly, so don't worry if you get stuck. There's always help on our forums and if you have a mentor, you can ask them, too. Do you know what else can get complicated? Webapps themselves, and in the next section, you will discover how to mitigate some of that challenges that complexity will inevitably bring.
