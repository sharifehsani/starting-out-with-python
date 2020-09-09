"""
- Author: Sharif Ehsani
- Date: September 2020
- www.gitbuh.com/ehsanis

Short Answer
1. Look at the following statement:
numbers = [10, 20, 30, 40, 50]
a. How many elements does the list have? 5 
b. What is the index of the first element in the list? 0 
c. What is the index of the last element in the list? 4
"""

# main function to start the program
def main():

	# a list variable is created and initialized
	numbers = [10, 20, 30, 40, 50]

	# lets check the number of elements using the len() mehtod
	print('a. How many elements does the list have? ', end='')
	print('The list has ', len(numbers), 'number of elements:')

	# b. What is the index of the first element in the list?
	# lets find out using the index mehtod
	print('b. What is the index of the first element in the list? ', end='')
	print(numbers.index(10))

	# c. What is the index of the last element in the list?
	# lets find out using the index method
	print('c. What is the index of the last element in the list? ', end='')
	print(numbers.index(50))



# call the main function
main()