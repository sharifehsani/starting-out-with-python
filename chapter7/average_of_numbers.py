"""
- Author: Sharif Ehsani
- Date: August 2020
- https://github.com/sharifehsani

Programming Exercises
6. Average of Numbers
Assume that a file containing a series of integers is named my_numbers.txt and exists on the computer’s disk. 
Write a program that calculates the average of all the numbers stored in the file.
"""


# function to start the program
def main():

	# NOTE: we created a file named my_numbers.txt in the previous exercise. lets use that
	# that file containes numbers from 5 through 12

	# create variable to hold the sum of the numbers
	sum = 0
	# another variable to hold the count of the numbers
	count = 0

	# open the file
	file_in = open('my_numbers.txt', 'r')

	# in a loop read the content of the file line by line
	for line in file_in:
		# convert the string to int value
		line = int(line)

		# add the numbers up
		sum = sum + line

		# increment the count
		count += 1

	# close the file
	file_in.close()

	# calculate the average
	average = sum / count

	# print the result
	print("Total of numbers from 5 through 12 is: ", sum)
	print("Count of numbers from 5 through 12 is: ", count)
	print("The average of numbers from 5 through 12 is: ", average)


# call the main function
main()


