"""
- Author: Sharif Ehsani
- Date: August 2020
- https://github.com/sharifehsani

Checkpoint
7.12 Write a short program that uses a for loop to write the numbers 1 through 10 to
a file.
"""

# function to start the program
def main():

	# creat and open a file called 'number_1_through_10.txt' in 'w' access mode
	file_out = open('number_1_through_10.txt', 'w')

	# creat a loop to run 10 times
	for count in range(1, 11):
		# write count to the file with a new line at the end
		file_out.write(str(count) + '\n')

	# close the file
	file_out.close()


# call the main function
main()
