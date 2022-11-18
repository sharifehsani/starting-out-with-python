"""
- Author: Sharif Ehsani
- Date: September 2020
- https://github.com/sharifehsani

Checkpoint
9.13 Write an if statement that displays “Digit” if the string referenced by the variable
ch contains a numeric digit. Otherwise, it should display “No digit.”

"""


# main function to start the program
def main():

	# initialize a string variable that references a string
	ch = 'ab3cd'

	# initialize a boolean variable to test condition
	found = False

	# loop through the index of the string and check if the string has digit in it

	for c in ch:
		if (c.isdigit()):
			found = True

	# print the result
	if (found == True):
		print("Digit")

	else:
		print("No digit")
		

# call the main function
main()
