This lesson will introduce you to database joins.

### Querying For Followed Compositions

The index page currently shows compositions from all users, but wouldn't it be nice to see compositions from a certain group of users, like those one follows? You can have two lists of compositions, one that shows the followed users compositions, and one that shows all user compositions.

But getting compositions done by followed users is not trivial. The obvious way to load them would be to get the list of followed users, then for each user, get their list of compositions. All of those compositions would get funneled and sorted into a single list. This, however, doesn't scale well. As the database grows, the effort to combine the compositions in this huge list won't be efficient at all, and things like pagination will slow to a crawl. Such a problem is known as the <a href="https://medium.com/web-performance-for-developers/n-1-problem-c8911bfd2577" target="_blank">N+1 problem</a>.

Instead of doing all that work for bad performance, why not just do a database query? You can do this kind of thing *really fast* with a database **join** operation. This database operation takes two or more tables and jams them together, finding all combinations of rows that satisfy a given condition. The resulting combined rows are inserted into a temporary table.

![How to make peanut butter and jelly sandwiches the right way](https://images.unsplash.com/photo-1557133285-a2b6b21f6e13?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1351&q=80)

Let's try an example to help it sink in. Say you have a table of `users`:

| id   | username |
| :--- | :------- |
| 1    | paul     |
| 2    | sven     |
| 3    | gwen     |

And these users have a few `compositions`. Here's an imaginary compositions table:

| id   | artist_id | title                               |
| :--- | :-------- | :---------------------------------- |
| 1    | 1         | Turkey Vulture Rap (by paul)        |
| 2    | 3         | Soap Opera Sonata (by gwen)         |
| 3    | 2         | Tangerine In My Olives (by sven)    |
| 4    | 3         | If I Only Had A Bear Trap (by gwen) |

And you have an imaginary `follows` table like this:

| follower_id | following_id |
| :---------- | :----------- |
| 1           | 3            |
| 2           | 3            |
| 2           | 1            |

So, to obtain a list of compositions by users followed by sven, you can do a join on the `compositions` and `follows` table. The first thing to do is to filter the `follows` table so that the `follower_id` matches sven only. Then, the temporary join table is created from every possible combination of rows from the `compositions` and `follows` tables where the `artist_id` of the composition is the same as the `following_id` of the follow. Then, you will have all the compositions of the users followed by sven!

| id   | artist_id | title                               | follower_id | following_id |
| :--- | :-------- | :---------------------------------- | :---------- | :----------- |
| 1    | 1         | Turkey Vulture Rap (by paul)        | 2           | 1            |
| 2    | 3         | Soap Opera Sonata (by gwen)         | 2           | 3            |
| 4    | 3         | If I Only Had A Bear Trap (by gwen) | 2           | 3            |

You'll notice the `artist_id` and `following_id` are identical. That's because they were the columns used to perform the join, and that's exactly what you'd want to get all compositions by users who sven follows.

### Flask-SQLAlchemy Code To Perform Joins

Of course, examples are nice, but what about real code that can perform a database join? That's next, so pay close attention. For the join that occurred above, you could write it as a query shown below. This would be done inside the `User` model:

```python
return db.session.query(Composition).select_from(Follow).\
    filter_by(follower_id=self.id).\
    join(Composition, Follow.following_id == Composition.artist_id)
```

That's a pretty huge mouthful of SQLAlchemy, but taking it apart bit by bit will help it make sense. The starting point for all queries you've seen starts with the `query` attribute of the model you want to query. But this time it is different. While you ultimately want `compositions`, the first operation that should be done is a filter to the `follows` table. So:

- `db.session.query(Composition)`: You specify that the query will return `Composition` objects, because at the end of the day, that's what you want.
- `select_from(Follow)`: This indicates that the query begins with the `Follow` model.
- `filter_by(follower_id=self.id)`: This does the filtering of the `follows` table by the follower user. In sven's case, that's him.
- `join(Composition, Follow.following_id == Composition.artist_id)`: This does the join operation on 1) the result of the filter and 2) the `Composition` objects. It matches whenever the user that's followed matches the artist who made the `Composition

However, this could be even simpler. There's all kinds of ways that database queries can be rearranged to produce the same results, and this query is no different. You can swap the order of the filter and join:

```python
return Composition.query.join(Follow, Follow.following_id == Composition.artist_id)\
    .filter(Follow.follower_id == self.id)
```

This query starts from the `Composition.query` query object. Using that object, you can perform a join, then filter the results.

Databases are efficient. You might think that doing the join first and the filtering second would be more costly, but thanks to the smart people who build database engines for a living, these two queries have exactly the same performance. SQLAlchemy first takes a look at all the filters that are to be applied, then rearranges the order of operations of the query to make it as optimized as possible. You can even confirm the queries are the same by doing a `print()` on the query command (remember that from the Database Management section?).

Now you can have access to this conveniently as a property from the `User` model:

```python
class User(UserMixin, db.Model):
    # ...
    @property
    def followed_compositions(self):
        return Composition.query.join(
            Follow, Follow.following_id == Composition.artist_id)\
            .filter(Follow.follower_id == self.id)
```

Don't worry too much if this is still difficult to understand. Joins are hard to keep track of sometimes. Even experienced database developers get turned around in how to do a complex join, like yours truly.

___

Well done! You're now all set to put those filtered compositions where they belong: on the home page. Head over to the next lesson.
