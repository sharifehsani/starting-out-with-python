"""
- Author: Sharif Ehsani
- Date: August 2020
- https://github.com/sharifehsani

Programming Exercises
2. File Head Display
Write a program that asks the user for the name of a file. The program should display only the first five lines
of the file’s contents. If the file contains less than five lines, it should dis- play the file’s entire contents.
"""

# function to start the program
def main():

	# ask the user for the name of the file. creat a file before hand to check your program runs and works
	# I have created a file named 'file_head_display.txt'
	file_name = input("Enter the name of the file: ")

	# open the file that the name was given by the user
	file_in = open(file_name, 'r')

	# creat a loop to read the content of the file and the loop runs 5 times
	for x in range(1, 6):
		# read the lines
		line = file_in.readline()
		# strip the new line from th end of the file
		line = line.rstrip('\n')
		print(line)

	# close the file
	file_in.close()

# call the main function
main()




