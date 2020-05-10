Now that you know about why users need to authenticate, let's move on to another important topic: security. Your app will be on the internet, and attackers are always lurking in the depths. This lesson will teach you the basics of password security.

### Protecting Users' Information from Attackers

Your users are just normal people. Many of these normal people like the convenience of using the same or similar password on multiple websites. They might be people like your grandma or your quirky uncle Steve who has never gotten the hang of this "technology" thing. But *you* have better skills with technology, so you need to help them help you. That's right, help them help you because if one of your websites gets hacked, you don't all that user data to contain passwords.

Let's face it, attackers are out there. They always will be, looking to make a quick buck by stealing others information, and passwords can be a goldmine. Hackers can try those passwords on other sites and possibly steal even more information about the those users.

![](https://images.unsplash.com/photo-1510915228340-29c85a43dcfe?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80)
Better depiction of an attacker, no hoods or ski masks

"But I have to store passwords somewhere, right?", you might be thinking. Yep, you do, but there's a way to store passwords in a database in a way that doesn't represent the actual sequence of characters needed to unlock an account.

### Hashing

To store passwords in a database, you can store a **hash** of it instead of the password itself. A hash is the result of taking a password, putting it though a **hashing function**, adding some **salt**, and then adds some cryptographic transformations to it.

The hashing function gives something unrecognizable from the original password, but this can still be used to get the original password, and yes, hackers sometimes try to do that. The salt isn't real salt you might find on your kitchen counter top. Instead it's more digital, and can be thought of as some random component.

Recovering that password from the hash is nearly impossible, so hackers are stuck in that case. However, given the password and the salt to the same hashing function, the password can be recovered, and the user can be verified.

![diagram of hashing](../images/placeholder.png)

Hashing is cool and very complex, so it's a relief that all these computations can be done for you using state-of-the-art hashing libraries. You'll see one in the next lesson.