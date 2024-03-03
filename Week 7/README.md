**Modify Authenticator.add_user() to require that passwords include at least one special character and one number.**

In auth.py create two new exceptions:

PasswordMissingNumber

PasswordMissingSpecialCharacter

These should extend AuthException.

Modify the code to require at least one number and one special character in your code.

For purposes of this assignment, a valid number is:

('0','1','2','3','4','5','6','7','8','9')

a valid special character is:

('!','@','#','$','%','^','&','*','(',')')

One challenge that will arise, is that you need to check for the occurrence of any of a set of characters in a string.

# **Here is a hint:**

```
def containsAny(str, set):
    """ Check whether sequence str contains 
```

```
    ANY of the items in set. """
    return 1 in [c in str for c in set]
```

There are other methods to accomplish this (regular expressions), but the above uses techniques that we have learned so far.
