"""
- Author: Sharif Ehsani
- Date: August 2020
- https://github.com/sharifehsani

Programming Exercises
1. File Display
Assume that a file containing a series of integers is named numbers.txt and exists on the
computer’s disk. Write a program that displays all of the numbers in the file.
"""

# _______________________________________________________________________________________
# NOTE: lets write a code at the beginning of this program to creat the 'numbers.txt' file
# why? lol, cause it does not exist and it is a good exercise right???

# function to start the program
def main():

	# _____________This part creates the 'numbers.txt' file and writes some numbers to it___________________
	# creat the file
	numbers_file = open('numbers.txt', 'w')

	# in a loop write number 1 through 15
	for num in range(1, 16):
		# convert the int value to string before writting it to the file
		# and add the new line after each line
		numbers_file.write(str(num) + '\n')

	# close the file
	numbers_file.close()


	# _______________in this part read the file content and display all the numbers______________

	# open the file for reading
	file_in = open('numbers.txt', 'r')

	# in a for loop read all the lines
	print("Here is the content of the file: ")
	for line in file_in:
		# display the line, but before remove the new line from the end
		line = line.rstrip('\n')
		print(line)


	# close the file
	file_in.close()


# call the main function
main()
