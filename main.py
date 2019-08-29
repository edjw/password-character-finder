#!/usr/bin/env python
import click

@click.command()

def main():
	"""Banks often ask for 3 characters from a password. It can be hard to work this out. This program makes it easy."""
	pwd = click.prompt("What's the password?", type=str, hide_input=True)
	first_character = click.prompt("First requested character?", type=click.IntRange(0, len(pwd)), hide_input=True) - 1
	second_character = click.prompt("Second requested character?", type=click.IntRange(0, len(pwd)), hide_input=True) - 1
	third_character = click.prompt("Third requested character?", type=click.IntRange(0, len(pwd)), hide_input=True) - 1
	click.echo(pwd[first_character] + ", " + pwd[second_character] + ", " + pwd[third_character])

if __name__ == '__main__':
	main()