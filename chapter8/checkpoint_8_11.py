"""
- Author: Sharif Ehsani
- Date: August 2020
- https://github.com/sharifehsani

Checkpoint
8.11 What will the following code display?
numbers = [1, 2, 3, 4, 5] 
my_list = numbers[:1] 
print(my_list)
"""

# main function to start the program
def main():
	numbers = [1, 2, 3, 4, 5] 				# a list with 5 elements is assigned to numbers variable
	my_list = numbers[:1] 					# the lit numbers is sliced from position zero to position 1 position 1 is not included
	print(my_list)							# print the elements of the list [1]

# call the main function
main()
