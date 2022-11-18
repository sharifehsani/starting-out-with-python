"""
- Author: Sharif Ehsani
- Date: August 2020
- https://github.com/sharifehsani

Algorithm Workbench
2. Write a program that opens the my_name.txt file that was created by the program in
question 1, reads your name from the file, displays the name on the screen, and then
closes the file.
"""

# a function to start the program
def main():

	# open the input file in 'r' access mode to read data
	file_in = open("my_name.txt", 'r')

	# read the name or the first (the only) line
	name = file_in.readline()

	# strip the new line from the end of the line
	name = name.rstrip('\n')

	# close the input file
	file_in.close()

	# print the name
	print("Your name is: ", name)


# call the main function
main()
