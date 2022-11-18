
"""
- Author: Sharif Ehsani
- Date: September 2020
- https://github.com/sharifehsani

Algorithm workbench
5. Write a function that accepts a list as an argument (assume the list contains integers)
and returns the total of the values in the list.
"""

# main function to start the program
def main():

	# initialize number list with 5 odd integer elements
	numbers = [1, 3, 5, 7, 9]

	# call the total function and pass the list as argument
	sum = total(numbers)

	# print the total
	print("Sum of all the elements of the list = ", sum)

# function to recieve a list as argument and return the total
def total(numbers):

	# initialize an accumulator
	total_of_all_numbers = 0

	# loop through the elements of the list 
	for num in numbers:
		# add up all the elements of the list and assign to the accumulator
		total_of_all_numbers += num

	return total_of_all_numbers

# call the main function
main()
