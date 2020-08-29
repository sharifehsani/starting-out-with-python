"""
- Author: Sharif Ehsani
- Date: August 2020
- www.gitbuh.com/ehsanis

Algorithm Workbench
1. Write a program that opens an output file with the filename my_name.txt, writes your
name to the file, and then closes the file.
"""
# function to start the program
def main():
	
	# open an output file called my_name.txt
	file_out = open('my_name.txt', 'w')

	# get user input
	name = input("Enter your name: ")

	# write the name on the file
	file_out.write(name + "\n")

	# close the file
	file_out.close()

	# print a message
	print("Your name is recorded.")


# call the main function
main()



