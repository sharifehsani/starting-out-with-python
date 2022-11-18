"""
- Author: Sharif Ehsani
- Date: August 2020
- https://github.com/sharifehsani

Checkpoint
7.14 Assume that the file data.txt exists and contains several lines of text. Write a
short program using the while loop that displays each line in the file.
"""

# function to start the program
def main():

	# open the file, but since this file does not exist, open a file that was created earlier
	# in the exercise called 'number_1_through_10.txt' in 'r' access mode
	file_in = open('number_1_through_10.txt', 'r')

	# read the first line
	line = file_in.readline()

	# run the loop with the condition to run until there is an empty string
	print("this file includes the following content.")
	while (line != ''):
		line = line.rstrip('\n')
		print(line)
		line = file_in.readline()
	
	# close the file

# call the main function
main()
