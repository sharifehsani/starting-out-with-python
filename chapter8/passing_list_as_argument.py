"""
- Author: Sharif Ehsani
- Date: August 2020
- https://github.com/sharifehsani

in this program a list passed as an argument to a funciton and the functionreturns the total of the list’s elements.
"""

# function to start the program
def main():

	# creat a list of numbers
	my_list = [1, 4, 19, 54, 13, 8]

	# pass the list to calculate_total function
	total = calculate_total(my_list)

	# print the result
	print("The sum of all the values in the list =", total)

# a function that recieves a list as an arguments sums up the elements of the list and returns the total to the caller
def calculate_total(my_list):

	# in a for loop step through the list and add the values to the accumulator
	sum = 0

	for elements in my_list:
		# add the values to the accumulator
		sum += elements

	# return the result to the caller
	return sum


# call the main function
main()

