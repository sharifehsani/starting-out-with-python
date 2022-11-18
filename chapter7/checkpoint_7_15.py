"""
- Author: Sharif Ehsani
- Date: August 2020
- https://github.com/sharifehsani

Checkpoint
7.15 Revise the program that you wrote for Checkpoint 7.14 to use the for loop
instead of the while loop.
"""

# main function to start the program
def main():

	# open the file 'number_1_through_10.txt' in 'r' access mode
	file_in = open('number_1_through_10.txt', 'r')

	# creat the for loop to run until there is no more line to read
	print("The content of this file is as follows: ")
	for line in file_in:
		line = line.rstrip('\n')		# remove the new line from the end of each line
		print(line)

	# close the file
	file_in.close()

# call the main function
main()
