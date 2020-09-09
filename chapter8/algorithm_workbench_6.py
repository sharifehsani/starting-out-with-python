"""
- Author: Sharif Ehsani
- Date: September 2020
- www.gitbuh.com/ehsanis

Algorithm workbench
6. Assume the names variable references a list of strings. Write code that determines whether 'Ruby' 
is in the names list. If it is, display the message 'Hello Ruby'. Otherwise, display the message 'No Ruby'.

"""

# main function to start the program
def main():
	# initialize an list variable and assign some string elements to it
	names = ['Sharif', 'Bani', 'Naz', 'Eli', 'Ruby']

	# check the elements of list and search for 'Ruby'
	# make sure you search for 'Ruby' no 'ruby'
	if 'Ruby' in names:
		print("Hi Ruby!")
	else:
		print("No Ruby")


# call the main function
main()


