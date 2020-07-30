"""
- Author: Sharif Ehsani
- Date: July 2020
- www.gitbuh.com/ehsanis

- This program prints a traingular pattern of asterisks using nested for loop
"""

# function to start the program
def main():
	print() # print a blank line to seperate the command line from the prorgram for readablity
	print("This program prints a traingular pattern of asterisks using nested for loop.")
	# call the get_input() function
	get_input()

# function to get user input
def get_input():
	# ask the user to enter the number of rows (size) of the triangl
	rows = int(input("Enter the number of rows in the trainagle: "))

	# validate the input to make sure the input is not negative number or zero
	while (rows <= 1 ):
		print("ERROR! number of rows must be greater than one.")
		rows = int(input("Enter the number of rows in the trainagle: "))

	# call the make_pattern()function and pass rows as parameter
	make_pattern(rows)

# function to make triangular pattern
def make_pattern(rows):
	asterisks = "*"
	cols = 1
	for r in range(rows):
		for c in range(cols):			# we could also use this code: for c in range(r + 1) instead of making extra variable cols
			print(asterisks, end='')	# use end='' so the program does not print the next asterisks in the new line
		cols = cols + 1					# inceament the number of columns after each iteration of the loop

		print() # print a new line after each row


# call the main function
main()