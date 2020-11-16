"""
- Author: Sharif Ehsani
- Date: October 2020
- www.gitbuh.com/ehsanis

Algorithm Workbench
7. Write a function that accepts a string as an argument and displays the string backwards.
"""

# main function to start the program
def main():

	# initialize a string variable and assign string to it
	my_string = "Step on no pets"


	print("This string is a palindrome: ", '"', my_string, '"')

	print(len(my_string))

	for i in range(len(my_string)):
		for j in range(i):
			print('i')
		print('\n')

# call the main function
main()