"""
- Author: Sharif Ehsani
- Date: July 2020
- www.gitbuh.com/ehsanis

8. Prime Numbers
A prime number is a number that is only evenly divisible by itself and 1. For example, the
number 5 is prime because it can only be evenly divided by 1 and 5. The number 6, however,
is not prime because it can be divided evenly by 1, 2, 3, and 6.
Write a Boolean function named is_prime which takes an integer as an argument and
returns True if the argument is a prime number, or False otherwise. Use the function in a
program that prompts the user to enter a number and then displays a message indicating
whether the number is prime.
"""

# main function to start the program
def main():
	print()
	print("This program determines if a number entered by the user is prime number or not.")
	# call the get_input function to get the number from the user and assign it to number variable
	number = get_input()

	# call the is_prime function and pass the number as parameter and assign it to result variable
	result = is_prime(number)

	# print the result
	if (result == True):
		print(number, 'is prime.')
	else:
		print(number, 'is not prime.')


# function to get user input
def get_input():

	the_number = int(input("Enter a positiv integer number greater than 1: "))		# get user input
	# prime numbers are alway positiv numbers so we make sure the input is greater than 1
	while (the_number < 2):
		print("ERROR!, wrong input, number must be positive whole number greater than 1.")
		the_number = int(input("Enter a positiv integer number greater than 1: "))
	
	return the_number												# return the number to the caller
	# end of function


# function to determine if the number entered by the user is prime
def is_prime(num):
	
	# check if the num is prime by using the mod operator
	# We are dividing the input number by all the numbers in the range
	#  of 2 to (number – 1) to see whether there are any positive divisors other than 1 and number itself.
	#is_prime = False

	for i in range(2, num):
		if (num % i) == 0:
			return False
			break
	else:
		return True
	
		# end of function


# call the main function
main()