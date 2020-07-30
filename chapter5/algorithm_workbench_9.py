"""
- Author: Sharif Ehsani
- Date: July 2020
- www.gitbuh.com/ehsanis

9. Write code that prompts the user to enter a number in the range of 1 through 100 and validates the input.
"""

# main function to start the program
def main():
	print() 	# blanck line to seperate the program from the command line for readablity
	print('This program prompts the user to enter a number in the range of 1 through 100 and validates the input.')

	# get user input
	number = int(input("Enter a number between 1 and 100: "))

	# validate the input
	while (number < 1 or number > 100):
		print('ERROR!, Number should be between 1 and 100.')
		number = int(input("re-enter a number between 1 and 100: "))

	# print the result one it a valid number is entered.
	print("Thanks, you entered a valid number and it is: ", number)


# call the main function
main()