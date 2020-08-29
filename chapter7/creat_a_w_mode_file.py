"""
- Author: Sharif Ehsani
- Date: August 2020
- www.gitbuh.com/ehsanis

This program creats a file named "test_file.txt" in the same directory as the program in 'w' mode
Open a file for writing. If the file already exists, erase its contents. If it
does not exist, create it.
"""

# function to start the program
def main():

	# pass the name of the file 'test.txt' and access mode 'w' write and assign it to file variable 
	my_test_file = open("test_file.txt", 'w')

	# open a python format file in the same directory and name it 'creat_a_w_mode_file_in_another_location.py'
	phthon_file = open('creat_a_w_mode_file_in_another_location.py', 'w')



# call the main function
main()

