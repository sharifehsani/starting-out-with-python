"""
- Author: Sharif Ehsani
- Date: August 2020
- https://github.com/sharifehsani

Algorithm Workbench
6. Write code that opens an output file with the filename number_list.txt, but does not
erase the file’s contents if it already exists.
"""

# function to start the program
def main():

	# open the 'number_list.txt' file in 'a' append mode
	file_out = open("number_list.txt", 'a')

	# write 0 to the file to double check
	file_out.write(str(0))

	# close the file
	file_out.close()

# call the main function
main()
