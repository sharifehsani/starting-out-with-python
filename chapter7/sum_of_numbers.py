"""
- Author: Sharif Ehsani
- Date: August 2020
- www.gitbuh.com/ehsanis

Programming Exercises
5. Sum of Numbers
Assume that a file containing a series of integers is named my_numbers.txt and exists on the computer’s disk. 
Write a program that reads all of the numbers stored in the file and calculates their total.
"""

# function to start the programs
def main():

	# ___________________First part of the program_________________________
	# NOTE: lets first creat a file named 'my_numbers.txt' in the first part of the program
	# creat 'my_numbers.txt' file and write a few integers on it
	# open the file with context manager
	with open("my_numbers.txt", 'w') as file_out:
		# add numbers 5 through 12 to the file
		for num in range(5, 13):
			# write the numbers to the file and add the new line character to the end
			# make sure to convert the int value to string before writting to file
			file_out.write(str(num )+ '\n')

	# the file is closed automatically

	# _________________Second part of the program__________________________

	# accomulator counter
	total = 0
	# open the file created in the first part of the program
	with open("my_numbers.txt", 'r') as file_in:
		# read the content of the file in a loop
		for line in file_in:
			# convert the string value to int value
			line = int(line)
			# add the numbers and assign the sum to total variable
			total = total + line

		# print the total
		print("The sum of numbers from 5 through 12 is: ", total)

	# the file is closed automatically

# call the main function
main()

