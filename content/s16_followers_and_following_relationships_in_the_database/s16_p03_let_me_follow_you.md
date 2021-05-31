While you might have the models, relationships, and helper methods in place allow users to follow others, you still need to build the view functions and templates to give your users the means to do it. In this lesson, you'll define the various view functions needed for following, unfollowing, and everything in between.

### (Un)Following Other Users

Your view functions are what actually allow your users to do things on your webapp, and that includes following other users. The `follow()` view function is defined below:

```python
@main.route('/follow/<username>')
@login_required
@permission_required(Permission.FOLLOW)
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash("That is not a valid user.")
        return redirect(url_for('.home'))
    if current_user.is_following(user):
        flash("Looks like you are already following that user.")
        return redirect(url_for('.user', username=username))
    current_user.follow(user)
    db.session.commit()
    flash(f"You are now following {username}")
    return redirect(url_for('.user', username=username))
```

The requested user to follow, specified in the URL, is loaded and verified 1) to exist and 2) they are already being followed. Given those checks pass, the user is followed and the session is finally committed to the database.

<div class="alert alert-info" role="alert"><b>Task: </b>Implement the <code>unfollow()</code> view function. This is very similar to the <code>follow()</code> view function.</div>

### View Functions To Display Users

It's also useful to display the list of users that follow a particular user. The view function to get and paginate that list of users is shown below:

```python
# Who my followers are
@main.route('/followers/<username>')
def followers(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash("That is not a valid user.")
        return redirect(url_for('.home'))
    page = request.args.get('page', 1, type=int)
    pagination = user.followers.paginate(
        page,
        per_page=current_app.config['RAGTIME_FOLLOWERS_PER_PAGE'],
        error_out=False)
    # convert to only follower and timestamp
    follows = [{'user': item.follower, 'timestamp': item.timestamp}
               for item in pagination.items]
    return render_template('followers.html',
                           user=user,
                           title="Followers of",
                           endpoint='.followers',
                           pagination=pagination,
                           follows=follows)
```

First thing to do is to get the user in question. If the user doesn't exist, the user is told so through a notification. A pagination object is then created from the user's followers. Since the query for followers returns a list of `Follow` instances, only the follower users are needed as you already know they follow the user in question. Another list is created instead that gives only the follower users and the timestamp to keep rendering simple.

<div class="alert alert-info" role="alert"><b>Task: </b>Create a <code>following()</code> view function. This is similar to the <code>followers()</code> view function except you will show the users a particular user follows using the <code>user.following</code> relationship. It will also pass variables to the <code>followers.html</code> file.</div>

___

You are so close to having a real social media app! Especially one where users can, y'know, be social and keep up with those they follow. Onto the next lesson to get those templates made!
