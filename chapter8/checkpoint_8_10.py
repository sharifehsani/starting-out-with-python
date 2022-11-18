"""
- Author: Sharif Ehsani
- Date: August 2020
- https://github.com/sharifehsani

Checkpoint
8.10 What will the following code display?
numbers = [1, 2, 3, 4, 5] 
my_list = numbers[1:] 
print(my_list)
"""

# function to start the program
def main():
	numbers = [1, 2, 3, 4, 5] 			# a list with 5 elements is assigned to numbers variable
	my_list = numbers[1:] 				# the numbers list is sliced from index position to the end
	print(my_list)						# prints the elments of the my_list variable [2, 3, 4, 5]


# call the main function
main()
