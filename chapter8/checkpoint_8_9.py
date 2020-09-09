"""
- Author: Sharif Ehsani
- Date: August 2020
- www.gitbuh.com/ehsanis

Checkpoint
8.9 What will the following code display?
numbers = [1, 2, 3, 4, 5] 
my_list = numbers[1:3] 
print(my_list)
"""

# function to start the program
def main():
	numbers = [1, 2, 3, 4, 5] 				# a list with 5 elments is assigned to numbers variable
	my_list = numbers[1:3] 					# numbers list is sliced from index 1 through 2 inclusive and assigned to my_list variable
	print(my_list)							# prints th elements of the my_list variable [2, 3]


# call the main function
main()
