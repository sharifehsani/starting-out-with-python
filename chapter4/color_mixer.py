"""
- Author: Sharif Ehsani
- Date: June 2020
- https://github.com/sharifehsani

5. Color Mixer
The colors red, blue, and yellow are known as the primary colors because they cannot be
made by mixing other colors. When you mix two primary colors, you get a secondary color,
as shown here:
When you mix red and blue, you get purple.
When you mix red and yellow, you get orange.
When you mix blue and yellow, you get green.
Design a program that prompts the user to enter the names of two primary colors to mix.
If the user enters anything other than “red,” “blue,” or “yellow,” the program should display
an error message. Otherwise, the program should display the name of the secondary
color that results.
"""

# function main to start the program
def main():
	print()
	print("This color mixer program displays a secondary color mixed of two primary color.")
	get_input()

# function to get user input
def get_input():
	primary_one = input("Please enter the first primary color name: ")
	primary_two = input("Please enter the second primary color name: ")
	if ((primary_one == "red" or primary_one == "blue" or primary_one == "yellow") and (primary_two == "red" or primary_two == "blue" or primary_two == "yellow")):
		color_mixer(primary_one, primary_two)

	else:
		print("Error! you did not enter the primary color names.")	

# color mixer function
def color_mixer(primary_one, primary_two):
	if ((primary_one == "red" and primary_two == "blue") or (primary_one == "blue" and primary_two == "red")):
		print('red and blue makes "purple"')
	elif ((primary_one == "red" and primary_two == "yellow") or (primary_one == "yellow" and primary_two == "red")):
		print('red and yellow makes "orange"')
	elif ((primary_one == "blue" and primary_two == "yellow") or (primary_one == "yellow" and primary_two == "blue")):
		print('blue and yellow makes "green"')
	else:
		print(primary_one, " and ", primary_two, " does not make any secondary color.")


# call the main function
main()
