
Not sure where this goes
-----
(Me going on a tangent)


```bash
$ flask db migrate
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
ERROR [root] Error: Target database is not up to date.
```

Oh my. Probably because I changed the name of my models, or as it says my database not "up to date." If this happens to you, you may have to delete your migrations folder and try again with `flask db init`. I also deleted my database or dropped all tables or something, so obviously you'd only migrate if you're *running* the website in production from epoch 0

I will keep my old on in source control but will do `db init`

```bash
$ flask db migrate
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
ERROR [root] Error: Target database is not up to date.
```

Oh my. Probably because I changed the name of my models, or as it says my database not "up to date." If this happens to you, you may have to delete your migrations folder and try again with `flask db init`. I also deleted my database or dropped all tables or something, so obviously you'd only migrate if you're *running* the website in production from epoch 0

I will keep my old on in source control but will do `db init`
Also, I forgot `lazy='dynamic'` and I don't know how to explain. And I think in general I'll have to keep the same users as before like john because it'll get confusing which ones you have or not

Now that you've updated User Profile, migration

"ERROR database is not up to date" WHAT?!

https://stackoverflow.com/a/53593914 THIS ANSWER YAY!