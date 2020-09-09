
"""
- Author: Sharif Ehsani
- Date: September 2020
- www.gitbuh.com/ehsanis

Algorithm workbench
8. Write a statement that creates a two-dimensional list with 5 rows and 3 columns. 
Then write nested loops that get an integer value from the user for each element in the list.
"""

# main function to start the program
def main():

	# initialize a list variable with 5 rows and 3 columns with repetition operator
	numbers = [ [0, 0, 0],		# row 1 with 3 columns
				[0, 0, 0],		# row 2 with 3 columns
				[0, 0, 0],		# row 3 with 3 columns
				[0, 0, 0],		# row 4 with 3 columns
				[0, 0, 0]]		# row 5 with 3 columns

	# loop through the elements in a nested loop and get the user input and populate the list
	# the outer loops run 5 times
	for r in range(5):
		# ther inner loop runs 3 times
		for c in range(3):
			print("Enter an integer value for row ", r + 1, 'and column ', c + 1, end='')
			# get user input
			num = int(input(": "))
			# populate the rth row and cth columns of the list
			numbers[r][c] = num

	# print the list
	print("here is the list: ", numbers)


# call the main function
main()