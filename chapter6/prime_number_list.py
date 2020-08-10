"""
- Author: Sharif Ehsani
- Date: July 2020
- www.gitbuh.com/ehsanis

9. Prime Number List
This exercise assumes you have already written the is_prime function in Programming
Exercise 8. Write another program that displays all of the prime numbers from 1 through 100.
The program should have a loop that calls the is_prime function.
"""

# function to start the program
def main():
	print()
	print("This program lists all the prime numbers from 1 through 100.")

	# creat a for loop to call the is_prime function 
	for num in range(2,101):
		is_prime(num)
		


# function to determine prime number
def is_prime(number):
	if (number > 1):					# prime numbers are positive greater than 1
		for i in range(2, number):		
			if (number % i) == 0:		# prime numbers are number that are not devisible by any number other than 1 and itself
				break					# as soon as it is devisible to one number other than the itself and 1 break the loop
		else:
			print("prime number = ", number)
	


# call the main function
main()