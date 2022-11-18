"""
- Author: Sharif Ehsani
- Date: July 2020
- https://github.com/sharifehsani

3. Maximum of Two Values
Write a function named maximum that accepts two integer values as arguments and returns
the value that is the greater of the two. For example, if 7 and 12 are passed as arguments
to the function, the function should return 12. Use the function in a program that prompts
the user to enter two integer values. The program should display the value that is the
greater of the two.
"""


# function to start the program
def main():
	print()
	print("This program gets 2 integers from the user and tells which number is larger.")

	# get the two numbers from the users
	number_one = int(input("Enter the first number: "))
	number_two = int(input("Enter the second number: "))

	# call the maximum function and pass the two numbers as arguments
	result = maximum(number_one, number_two)

	# print the result
	print(result, " is the greater of the two numbers.")

# function to calculate the maximum
def maximum(one, two):
	# compare the 2 numbers and return the result
	if (one > two):
		return one
	else:
		return two


# call the main function
main()

