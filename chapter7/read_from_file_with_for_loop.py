"""
- Author: Sharif Ehsani
- Date: August 2020
- www.gitbuh.com/ehsanis

This program reads content of a file using for loop
"""

# function to start the program
def main():

	# open the file with 'r' access mode
	animal_names_file = open('animal_names.txt', 'r')

	# read all the lines from the file
	for line in animal_names_file:
		line_read = line
		line_read = line_read.rstrip('\n')	# remove the new line from the end of each line
		print(line_read)

	# close the file
	animal_names_file.close()

# call the main function
main()