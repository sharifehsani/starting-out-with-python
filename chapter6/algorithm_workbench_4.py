"""
- Author: Sharif Ehsani
- Date: July 2020
- https://github.com/sharifehsani

4. Write a function named times_ten that accepts a number as an argument. When the
function is called, it should return the value of its argument multiplied times 10.
"""

# function to start the program
def main():
	print()
	print("This program gets an int from the user times it by 10 and returns the value.")

	# get user input
	number = int(input("Enter an int value: "))

	# call the times_ten() function, pass the number as argument and assign the value to result variable
	result = times_ten(number)

	# print the returned value = result
	print('The number ', number, 'multiplied times 10 is: ', result)


# function to multiply number by 10 and return the resulf
def times_ten(num):
	return num * 10


# call the main function
main()
