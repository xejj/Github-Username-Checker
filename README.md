### Github-Username-Checker ###

This python script checks for all the available 4 character usernames on Github and gives different types of output:

Yellow output means that the username is either recently deleted, deactivated or banned/flagged
Red output means that the username is fully unavailable and cannot be used. The account with that username is active
Green output means that the username is free to use and can be applied to your account and will be put into the claimable_names.txt file created in the folder where the python file is placed.

Before running the script on your device make sure to acquaire the PAT from github:

Step-by-Step Guide:

Go to Settings: Click your profile photo in the top right corner and select Settings.

Developer Settings: On the far left sidebar, scroll all the way to the bottom and click Developer settings.

Personal Access Tokens: Select this, then choose Tokens (classic).

Note: If the script I gave you is simple, "Classic" is usually easier to set up.

Generate New Token: Click the Generate new token dropdown and select Generate new token (classic).

Configure:

Note: Give it a name (e.g., "Username_Checker").

Expiration: Set it to 30, 60, or 90 days.

Scopes: For a username checker, you actually don't need to check any boxes. An un-scoped token still gives you the higher rate limit (5,000/hr) for public data.

Generate and Save: Click the green Generate token button at the bottom.


that is all...
