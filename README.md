# Password Character Finder

**Log into your online banking faster**

## Use case
You're logging into your online banking and they ask for the 3rd, 9th, and 22nd character of your password.

But your password manager generated a strong, unique password like `LX9s*N_43sCzb4b2U6vyYRvF` for your account so it takes you ages to work out the right characters.

This script asks you for your password and the 3 Xth characters they're asking for then returns those characters.

(You'll have to adapt the script if your bank asks you for anything other than 3 characters.)

All input is hidden so isn't visible to anyone looking at the screen.

## Warning
You should be careful of any random script off Github that asks you to paste in your online banking password. This script doesn't do anything other than what I've explained above but take a look at the code before you use it to check.

## Installation and running it

Requires Python to be installed.

1. `pip install click` to get [Click](https://click.palletsprojects.com) for some command line nice things like hidden input and input validation. This isn't optional.

2. `cp password-character-finder /usr/local/bin`

3. You might have to run `chmod a+x /usr/local/bin/password-character-finder` if it doesn't run.

4. Run `password-character-finder` in a terminal.