"""
- Author: Sharif Ehsani
- Date: September 2020
- www.gitbuh.com/ehsanis

# in this exercise we work a bit with the search and replace methods
"""

# main function to start the prgoram
def main():

	# initialize a string variable
	file_name = 'search_and_repace_methods.py'

	# endswith(substring) The substring argument is a string. The method returns true if
	# the string ends with substring.
	if (file_name.endswith('.py')):
		print("The file is of the python executable file.")
	else:
		print("File is not python executable type.")

	# find(substring) The substring argument is a string. The method returns the
	# lowest index in the string where substring is found. If
	# substring is not found, the method returns -1.

	print("the string 'methods' you are looking for is found at index #", file_name.find('methods'))

	# replace(old, new) The old and new arguments are both strings. The method returns
	# a copy of the string with all instances of old replaced by new.
	new_file_name = file_name.replace('.py', '.txt')
	print("The new file name =", new_file_name)


	# startswith(substring) The substring argument is a string. The method returns true if
	# the string starts with substring. 
	print(file_name.startswith('replace'))

# call the main function
main()