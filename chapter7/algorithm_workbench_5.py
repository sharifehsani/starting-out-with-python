"""
- Author: Sharif Ehsani
- Date: August 2020
- https://github.com/sharifehsani

Algorithm Workbench
5. Modify the code that you wrote in question 4 so it adds all of the numbers read from
the file and displays their total.
"""

# function to start the program
def main():

	# open the file in 'r' access mode
	file_in = open("number_list.txt", 'r')

	# an accumulator variable to hold the sum
	sum = 0

	# creat a for loop to read the whole file
	for line in file_in:

		# convert the data read to int value and since int() function ignores the new line, don't worry rstriping it
		number = int(line)
		sum = sum + number

	# close the file
	file_in.close()

	# print the total
	print("The sum of number 1 through 100 is: ", sum)

# call the main function
main()
