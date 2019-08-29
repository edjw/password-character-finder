# Password Digit Finder

You're logging into your online banking and they ask for the 3rd, 9th, and 15th character of your password.

But your password manager generated a password like `LX9s*N_43sCzb4b2U6vyYRvF` for your account so it takes you ages to work it out.

This script asks you for your password and the 3 Xth characters they're asking for then returns those characters. You'll have to adapt the script if your bank asks you for anything other than 3 characters.

All input is hidden so isn't visible to anyone looking at the screen.

## Installation and running it

Requires Python to be installed.

1. `pip install click` to get [Click](https://click.palletsprojects.com) for some command line nice things like type checking.

2. `cp password-digit-finder /usr/local/bin`

3. You might have to run `chmod a+x password-digit-finder`.

4. Run `password-digit-finder` in a terminal.