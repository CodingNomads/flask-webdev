[//]: # (Source Flask-SQLAlchemy vs SQLAlchemy: https://stackoverflow.com/questions/14343740/flask-sqlalchemy-or-sqlalchemy)

You've gotten through forms and now you're ready to take on databases.

### Why Use A Database?

Most webapps these days have one or more databases that store website data in an organized way. As data continues to grow in this *base* of data, even if it's a lot of data, it can be parsed through with queries to present users with only partial data or even to do internal server bookkeeping. These queries can get specific chunks of data as needed, such as the users login info to verify them, hair drying products for sale and and price, or even images taken in the last year by certain photographers. The kinds of data and how you can search them all depend on what the underlying data represents and on the database technology use, but at the end of the day, databases store data to be uncovered at some unknown future time.

### Brief Introduction to SQL and Relational Databases

That might be a lot of *data* to take into your brain, but database technology has come a long way and it's rather easy to get started with. If you aren't already familiar with the technologies, there are two main kinds of databases: relational databases and document-oriented databases. They are often called SQL and NoSQL databases, respectively. SQL comes from Structured Query Language which is the industry-standard language used to query relational databases.

For your Flask webapp, you'll be using a **relational database**, which store data in **tables**. The tables model different entities in the domain, meaning that for a small online pet store business, its database tables might be Products, Customers, and Pet Categories, among other things. The tables each have a fixed number of columns, and each column has its own type and attributes that the data under it must conform to. The rows in each table can grow or shrink as data is added or deleted. Still, there's a lot more to learn about SQL and tables than just that, but for more do check out the link to our free mini-course on SQL.

### SQLAlchemy

Cool, alchemy? Does that mean, like, making potions and turning lead into gold, but with SQL? Often I think the same sort of thing when working in Python, that I made something magically work with just a few lines of Python code. SQLAlchemy brings that same feeling when working with SQL data, all with Python! According to its website:

> SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

The reason SQLAlchemy is used in this course is because it's probably the most popular Python SQL toolkit out there, and for good reason. SQLAlchemy lets programmers work at a higher level with standard Python objects instead of the tables or even a query language in order to work with data in the databases. It also supports many database backends and gives programmers access to low-level SQL functionality.

### Flask-SQLAlchemy

Because SQLAlchemy is so versatile, it didn't take herculean effort for someone to make a Flask-compatible extension that supports SQLAlchemy. Using SQLAlchemy by itself in a Flask application makes the process working with SQL databases in Flask much more difficult, as there is a lot of configuration that must happen first between the two. Flask-SQLAlchemy does almost all of that tedious work for you, meaning you don't have to configure engines and connections or any of that complicated stuff. To make the point clear, here are a couple photos of real objects to demonstrate an important concept:

![](https://images.unsplash.com/photo-1528724977141-d90af338860c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1385&q=80)
Life without Flask-SQLAlchemy

![](https://images.unsplash.com/photo-1554986334-ddb4be98f2f7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=634&q=80)
Life with Flask-SQLAlchemy

Make sense? Flask-SQLAlchemy only needs a few tweaks to get the power of SQL in the palm of your hands, but you still have the ability to make more complicated SQLAlchemy tweaks down the road if necessary.

Excited to hit the ground running with Flask-SQLAlchemy? In the next lesson, you'll install Flask-SQLAlchemy so you can get started with SQL in Flask in no time.
