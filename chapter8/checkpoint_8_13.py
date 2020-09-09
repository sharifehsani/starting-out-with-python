"""
- Author: Sharif Ehsani
- Date: August 2020
- www.gitbuh.com/ehsanis

Checkpoint
8.13 What will the following code display?
numbers = [1, 2, 3, 4, 5] 
my_list = numbers[-3:] 
print(my_list)
"""

# function to start the program
def main():
	numbers = [1, 2, 3, 4, 5] 				# a list with 5 elements is assigned to numbers variable
	my_list = numbers[-3:] 					# this is a backward slicing. the list is sliced from position -3 to the end
	print(my_list)							# prints [3, 4, 5]

# call the main function
main()