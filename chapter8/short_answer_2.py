"""
- Author: Sharif Ehsani
- Date: September 2020
- https://github.com/sharifehsani

Short Answer
2. Look at the following statement:
numbers = [1, 2, 3]
a. What value is stored in numbers[2]?
b. What value is stored in numbers[0]?
c. What value is stored in numbers[-1]?
"""

# main function to start the program
def main():

	# the number variable is initialize to some numbers
	numbers = [1, 2, 3]

	# a. What value is stored in numbers[2]? 3
	# lets print and find out
	print('a. What value is stored in numbers[2]? ', end='')
	print(numbers[2])

	# b. What value is stored in numbers[0]? 1
	print('b. What value is stored in numbers[0]? ', end='')
	print(numbers[0])

	# c. What value is stored in numbers[-1]? 3
	print('c. What value is stored in numbers[-1]? ', end='')
	print(numbers[-1])

# call the main function
main()
