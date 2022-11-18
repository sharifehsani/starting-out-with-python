"""
- Author: Sharif Ehsani
- Date: August 2020
- https://github.com/sharifehsani

Checkpoint
8.12 What will the following code display?
numbers = [1, 2, 3, 4, 5] 
my_list = numbers[:] 
print(my_list)
"""

# function to start the program
def main():
	numbers = [1, 2, 3, 4, 5] 			# a list with 5 elements is assigned to numbers variable
	my_list = numbers[:] 				# the list is slice from position 0 to the end inclusive
	print(my_list)						# print the content ofthe list [1, 2, 3, 4 , 5]


# call the main function
main()
