"""
- Author: Sharif Ehsani
- Date: July 2020
- https://github.com/sharifehsani

1. Feet to Inches
One foot equals 12 inches. Write a function named feet_to_inches that accepts a number
of feet as an argument, and returns the number of inches in that many feet. Use the
function in a program that prompts the user to enter a number of feet and then displays the
number of inches in that many feet.
"""

# main function to start the program
def main():
	print()
	print("This program converts feet to inches.")

	# call the function to get user input and assign the value to feet variable
	feet = get_input()

	# call the feet_to_inches function to convert the feet passed to it as an argument and assign it to inches variable
	inches = float(feet_to_inches(feet))

	# print the returned value
	print(feet, " feets equal ", inches, " Inches.")

# function to get user input
def get_input():
	# get user input
	number_of_feet = float(input("Enter number of feet: "))
	# return the number of feet to the caller
	return number_of_feet


# function to convert feet to inches and return the calue
def feet_to_inches(foots):
	# convert feet to inches
	total_number_of_inches = foots * 12
	# return the converted value
	return total_number_of_inches


# call the main function
main()
