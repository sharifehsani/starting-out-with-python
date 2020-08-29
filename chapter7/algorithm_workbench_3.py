"""
- Author: Sharif Ehsani
- Date: August 2020
- www.gitbuh.com/ehsanis

Algorithm Workbench
3. Write code that does the following: opens an output file with the filename
number_list.txt, uses a loop to write the numbers 1 through 100 to the file, and then
closes the file.
"""

# function to start the program
def main():

	# open an output file named number_list.txt in 'w' mode
	file_out = open('number_list.txt', 'w')

	# make a for loop run 100 times
	for num in range(1, 101):

		# in the loop write number 1 through 100 to the file with a new line at the end
		# conver the int into string before writting it to the file
		file_out.write(str(num) + '\n')

	# close the file
	file_out.close()

# call the main function
main()