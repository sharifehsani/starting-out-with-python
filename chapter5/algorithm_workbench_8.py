"""
- Author: Sharif Ehsani
- Date: July 2020
- https://github.com/sharifehsani

8. Write code that prompts the user to enter a positive nonzero number and validates the input.
"""

# function to start the progam
def main():
	# get user input
	number = int(input("Enter a nonzero number: "))

	# validate the input
	while (number == 0):
		print("ERROR!, number must be nonzero.")
		number = int(input("Enter a nonzero number: "))

	# once the valid number is entered we display it to the user
	print("Thank you, you entered ", number)


# call the main function
main()
