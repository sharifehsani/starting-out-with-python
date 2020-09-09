"""
- Author: Sharif Ehsani
- Date: September 2020
- www.gitbuh.com/ehsanis

Programming Exercises
2. Lottery Number Generator
Design a program that generates a seven-digit lottery number. The program should generate seven 
random numbers, each in the range of 0 through 9, and assign each number to a list element. 
(Random numbers were discussed in Chapter 6.) Then write another loop that displays the contents of the list.
"""

# import the random module from the python standard library
import random

# main function to start the program
def main():

	# make sure you import the random module from the python standard library
	# initialize a list variable
	lottery_number = [0] * 7

	# run a loop for 7 times
	for num in range(7):
		# generate randome number between 0 and 9 inclusive and assign the each index of the list
		lottery_number[num] = random.randint(0, 9)

	
	# in a loop print the elements of the lottery numbers list
	for num in lottery_number:
		print(num)


# call the main function
main()


