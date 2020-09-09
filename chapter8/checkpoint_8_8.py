"""
- Author: Sharif Ehsani
- Date: August 2020
- www.gitbuh.com/ehsanis

Checkpoint
8.8 What will the following code display?
numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30] 
numbers2 += numbers1 
print(numbers1) 
print(numbers2)
"""

# main function to start the program
def main():
	numbers1 = [1, 2, 3]						# a list numbers1 is assigned 3 elements
	numbers2 = [10, 20, 30] 					# a list numbers2 is assigned 3 elements
	numbers2 += numbers1 						# the first list is concainated with second list and assigned to 2nd list
	print(numbers1)								# prints the elements of the first list [1, 2, 3]
	print(numbers2)								# prints the elements of the second list after concatination [10, 20, 30, 1, 2, 3]


# call the main function
main()