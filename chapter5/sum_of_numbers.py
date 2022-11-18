"""
- Author: Sharif Ehsani
- Date: July 2020
- https://github.com/sharifehsani

8. Sum of Numbers
Write a program with a loop that asks the user to enter a series of positive numbers. The
user should enter a negative number to signal the end of the series. After all the positive
numbers have been entered, the program should display their sum.
"""

# main function to start the program
def main():
	print()
	print("This progra sums up all the positive numbers entered by the user. ")
	get_input()			# call the input function()

# function to get user input
def get_input():

	number = 0
	sum_of_numbers = 0
	while (number >= 0):
		sum_of_numbers = sum_of_numbers + number
		number = int(input("Enter a series of positive number and enter a negative number when you are done: "))
		# end of the loop)

	# display the sum of the series of numbers
	print("Sum of all the numbers entered = ", sum_of_numbers)

# call the main function
main()
