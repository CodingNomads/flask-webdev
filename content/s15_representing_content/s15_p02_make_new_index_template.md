So by this point, creating your compositions works. Now you're ready to show them in all their glory on the index page. In this lesson, it's your chance to prove your templating capabilities once more. A friendly reminder about our <a href="https://forum.codingnomads.co/c/courses/flask-webdev" target="_blank">community forum</a>, a resource to get your questions answered! And if you have one, your mentor, too.

[//]: # (TODO: Styling stuff, css static)

### Showing Compositions

Since you have a `compositions` object passed through to the `index.html` template, you can put it to use to show compositions from any and all users. Display these compositions under your `CompositionForm`. To represent the compositions, you can use an unordered list tag, `<ul>`, for listing all compositions. Inside that you can use the list item tag, `<li>`, *per composition*. Then, show each bit of information about the composition as a `<div>`.

Here's what you'll want to show for each composition:

- **Artist's avatar** - Each composition has *someone* who made it. Display that user's avatar, and linkify it to go to the user's profile page. When showing an `<img>`, you can use the `"img-rounded"` and `"profile_thumbnail"` classes.
- **Date of submission** - Use `moment(composition.timestamp).fromNow()` similar to how you've seen it before to show the time relative to now that the composition was submitted.
- **Artist's username** - Like the avatar, show the user's username with a link to the user's profile page
- **Release type** - Display the release type as "Single", "EP", or "Album" according to the composition's release type integer value. Remember you can "inject" the `ReleaseType` class into your templates just like you did `Permissions`!
- **Title** - The composition's title.
- **Description** - Show the description provided for the composition.

Here's a suggested way to go about it in your template:

```jinja2
<ul> {# All compositions #}
    <li> {# Single composition #}
        <div> {# Avatar #} </div>
        <div> {# Composition content #}
            <div>{# date #}</div>
            <div>{# title #}</div>
            {# ... #}
        </div>
    </li>
</ul>
```

### Styling

It's okay if you're not a CSS styling expert. For this course, we don't expect you to make something that looks perfect and professional. As long as you can get the information in the page and make it readable, that is good enough!

With this in mind, here are some optional CSS classes you can include in your `app/static/styles.css` file:

```css
ul.compositions {
    list-style-type: none;
    padding: 0px;
    margin: 16px 0px 0px 0px;
    border-top: 1px solid #e0e0e0;
}
ul.compositions {
    margin: 0px;
    border-top: none;
}
ul.compositions li.composition {
    padding: 8px;
    border-bottom: 1px solid #e0e0e0;
}
ul.compositions li.composition:hover {
    background-color: #f0f0f0;
}
div.composition-date {
    float: right;
}
div.composition-artist {
    font-weight: normal;
}
div.composition-release-type {
    font-style: italic;
}
div.composition-title {
    font-weight: bold;
}
/* for showing user avatar */
div.composition-thumbnail {
    position: absolute;
}
/* the composition-content div surrounds the textual
   composition content (title, release type, etc) */
div.composition-content {
    margin-left: 72px;
    min-height: 72px;
}
```

### The Composition Form

Keep in mind that if the user doesn't have permission to publish compositions, then there is no point in showing them the form. So, *only* if the user can publish compositions should you let them see the `CompositionForm`.

### The Result

Once your index page is done, it should appear similar to this:

![new index page](../images/placeholder.png)

Don't worry if it doesn't look as pretty. The point of the course is for you to learn how to develop a web app in Flask, which you are doing. :)

___

Are there a few "unicorns" sharing their musical creations on your index page? Even if it's not quite that sophisticated, as long as your fake users compositions are visible and readable, you can call that a win! But isn't it a strain on your wrists to add all those fake users or compositions? What if you could generate a bunch of fake data just for quicker development...

![](https://images.unsplash.com/photo-1529078155058-5d716f45d604?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1349&q=80)