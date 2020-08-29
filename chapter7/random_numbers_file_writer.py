"""
- Author: Sharif Ehsani
- Date: August 2020
- www.gitbuh.com/ehsanis

Programming Exercises
7. Random Number File Writer
Write a program that writes a series of random numbers to a file. Each random number should be in the range of 1 through 100. 
The application should let the user specify how many random numbers the file will hold.
"""
# make sure to import the random maodule from the standard python library
import random

# function to start the program
def main():

	# creat / open a file called 'random_numbers.txt' as 'w' access mode
	file_out = open("random_numbers.txt", 'w')

	# get user input on how many random number to write on the file
	random_number_count = int(input("How many random numbers do you want the fild to hold: "))

	# in a loop generate as many random numbers between 1 and 100 inclusive as the user specify
	for num in range(1, random_number_count + 1):
		# generate random number between 1 and 100
		rand_num = random.randint(1, 100)
		# write the generated number to the file
		file_out.write(str(rand_num) + '\n')


	# print a message
	print("Writting is done.")

	# close the file
	file_out.close()
	
# call the main function:
main()