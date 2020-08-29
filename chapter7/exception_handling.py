"""
- Author: Sharif Ehsani
- Date: August 2020
- www.gitbuh.com/ehsanis

Programming Exercises
9. Exception Handing
Modify the program that you wrote for Exercise 6 so it handles the following exceptions:
• It should handle any IOError exceptions that are raised when the file is opened and data is read from it.
• It should handle any ValueError exceptions that are raised when the items that are read from the file are converted to a number.

exerice 6
____________________
6. Average of Numbers
Assume that a file containing a series of integers is named my_numbers.txt and exists on the computer’s disk. 
Write a program that calculates the average of all the numbers stored in the file.
____________________

"""

# function to start the program
def main():

	# create a variable to hold sum of all the numbers
	sum = 0

	# create a vaiable to count the number of ints
	counter = 0

	# open the file 'my_numbers.txt' for read in a try and exception hander
	try:
		# open the file
		file_in = open('my_numbers.txt', 'r')

		# read the content of the file
		for line in file_in:

			# convert the string to int
			line = int(line)

			# increment the counter
			counter += 1
			sum = sum + line

		# close the file
		file_in.close()

		# calculate the average
		average = sum / counter

		# print the result
		print("The average of all the numbers is: ", average)


	# handle the exceptions raised by the try suite
	# this exception clause handles th file input error
	except IOError:
		print("An error occured trying to open the file.")

	# this exception clause handles the wrong value error
	except ValueError:
		print("None numeric data found in the file.")



# call the main function
main()



