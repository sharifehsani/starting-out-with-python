"""
- Author: Sharif Ehsani
- Date: August 2020
- https://github.com/sharifehsani

Programming Exercises
8. Random Number File Reader
This exercise assumes you have completed Programming Exercise 7, Random Number File Writer. Write another program that reads the random 
numbers from the file, display the numbers, and then display the following data:
• The total of the numbers
• The number of random numbers read from the file
"""

# function to start the program
def main():
	
	# creat a counter variable to hold the count of integers in the file
	counter = 0

	# creat a variable to hold the sum of all the numbers
	sum = 0

	# open the file for read
	file_in = open("random_numbers.txt", 'r')

	# read the content of the file in a loop
	for line in file_in:

		#convert the string to int
		line = int(line)

		# increment the counter
		counter += 1

		# add the numbers together
		sum = sum + line

	# close the file
	file_in.close()

	# print the result
	print("Th total of the numbers = :", sum)
	print("The number random numbers read from the file = : ", counter)


# call the main function
main()





