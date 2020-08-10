import random 		# import random module from the python standard library
"""
- Author: Sharif Ehsani
- Date: July 2020
- www.gitbuh.com/ehsanis

7. Odd/Even Counter
In this chapter you saw an example of how to write an algorithm that determines whether
a number is even or odd. Write a program that generates 100 random numbers, and keeps
a count of how many of those random numbers are even and how many are odd.
"""

# main function to start the program
def main():
	print()
	print("This program generates 100 random numbers and keeps count of how many of these 100 numbers are even.")
	
	odd_or_even = ''
	even_count = 0
	odd_count = 0

	# in a for loop thar runs 100 times generate the radom number and also check if the number is odd or even
	for number in range(1, 101):
		random_number = random.randint(1,100)		# generate random number in range of 1 to 100 inclusive
		if (random_number % 2 == 0):				# check if the generated random number is even or odd by taking mod of the number
			odd_or_even = 'even'
			even_count += 1
		else:
			odd_or_even = 'odd'
			odd_count += 1

		# print the result
		print('random number ', random_number, ' is:', odd_or_even)
		print('Total even numbers =', even_count)
		print('Total odd numbers = ', odd_count)
		
	# print the total result
	print('Total even numbers =', even_count, ' and total odd numbers = ', odd_count)


# call the main function
main()




