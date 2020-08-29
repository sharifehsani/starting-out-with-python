"""
- Author: Sharif Ehsani
- Date: August 2020
- www.gitbuh.com/ehsanis

Programming Exercises
3. Line Numbers
Write a program that asks the user for the name of a file. The program should display the contents of the file with each line
preceded with a line number followed by a colon. The line numbering should start at 1.
"""

# function to start the program
def main():

	# open the file. We use the file we created for exercise 2 "file_head_display.py" and it is called 'file_head_display.txt'
	# we open in 'r' access mode
	f = open("file_head_display.txt", 'r')

	# creat a variable to take line counts and starts from line 1
	line_number = 1

	# in a loop read the al the lines of the file
	for line in f:
		# strip the new line from the end of each line
		line = line.rstrip('\n')
		# print the lines
		print("line number ", line_number, ": ", line)
		line_number += 1

	# close the file
	f.clsoe()

# call the main function
main()

