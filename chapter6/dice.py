import random 			# import random madule from python standard library
"""
- Author: Sharif Ehsani
- Date: July 2020
- https://github.com/sharifehsani

Dr. Kimura teaches an introductory statistics class, and has asked you to write a program
that he can use in class to simulate the rolling of dice. The program should randomly generate
two numbers in the range of 1 through 6 and display them. In your interview with Dr.
Kimura, you learn that he would like to use the program to simulate several rolls of the
dice, one after the other. Here is the pseudocode for the program:
While the user wants to roll the dice:
Display a random number in the range of 1 through 6
Display another random number in the range of 1 through 6
Ask the user if he or she wants to roll the dice again

"""

# function to start the proram
def main():
	print()
	print("This program simulate the rolling of dice by generating random numbers.")

	keep_going = 'y'
	while (keep_going == 'y'):
		for num in range(2):
			number = random.randint(1,6)
			print("random number = ", number)

		# ask the user if s/he wants to roll a dice again
		keep_going = input("Do you want to roll the dice again? 'y' for yes and 'n' for no: ")


# call the main function
main()
