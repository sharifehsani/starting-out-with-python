"""
- Author: Sharif Ehsani
- Date: August 2020
- https://github.com/sharifehsani

4. Write code that does the following: opens the number_list.txt file that was created
by the code you wrote in question 3, reads all of the numbers from the file and displays
them, and then closes the file.
"""

# function to start the program
def main():

	# open the input file in 'r' access mode
	file_in = open("number_list.txt", 'r')

	print("The content of the file is as follows: ")
	# in a loop read all the lines
	for line in file_in:

		# read the lines and conver it to int value
		# since int function ignores the new line, you don't need to remove the new line from the
		# end of the line
		number = int(line)
		print(number)

	# close the file
	file_in.close()

# call the main function
main()
