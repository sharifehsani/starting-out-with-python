"""
- Author: Sharif Ehsani
- Date: September 2020
- https://github.com/sharifehsani

Short Answer
4. What does the following code display?
numbers = [1, 2, 3, 4, 5, 6, 7]
print(numbers[4:6])

"""

# main function to start the program
def main():

	# initialize a list ariable and assign 1, 2, 3, 4, 5, 6, 7 to it
	numbers = [1, 2, 3, 4, 5, 6, 7]

	# slice the list from position 4 to 5 inclusive
	print(numbers[4:6])		# [5, 6]

# call the main function
main()
