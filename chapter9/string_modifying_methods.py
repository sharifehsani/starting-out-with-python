"""
- Author: Sharif Ehsani
- Date: September 2020
- https://github.com/sharifehsani

# in this exercise we work a bit with the string modifying methods
"""

# NOTE: even though strings are immutable (not modifyable), but there are some methods that returns
# modified version of themselves. 

# main function to start the program
def main():

	# initialize a string variable
	my_string = '	$Roses are red, Violets are blue, Honey is sweet, And so are you. '

	print(my_string)

	# lower() Returns a copy of the string with all alphabetic letters converted to lowercase. Any
	# character that is already lowercase, or is not an alphabetic letter, is unchanged.
	print("lower() =", my_string.lower())


	# upper() Returns a copy of the string with all alphabetic letters converted to uppercase. Any
	# character that is already uppercase, or is not an alphabetic letter, is unchanged.
	print("upper() =", my_string.upper())

	# lstrip() Returns a copy of the string with all leading whitespace characters removed.
	# Leading whitespace characters are spaces, newlines (\n), and tabs (\t) that
	# appear at the beginning of the string.
	print("lstrip() =", my_string.lstrip())

	# lstrip(char) The char argument is a string containing a character. Returns a copy of the string
	# with all instances of char that appear at the beginning of the string removed.
	print("lstrip(char) =", my_string.lstrip('	$R'))

	# rstrip() Returns a copy of the string with all trailing whitespace characters removed.
	# Trailing whitespace characters are spaces, newlines (\n), and tabs (\t) that
	# appear at the end of the string.
	print("rstrip() =", my_string.rstrip())

	# rstrip(char) The char argument is a string containing a character. The method returns a copy of
	# the string with all instances of char that appear at the end of the string removed.
	print("rstrip(char) =", my_string.rstrip('. '))

	# strip() Returns a copy of the string with all leading and trailing whitespace characters removed.
	print("strip() =", my_string.strip())

	# strip(char) Returns a copy of the string with all instances of char that appear at the
	# beginning and the end of the string removed.
	print("strip(char) =", my_string.strip(' 	$.'))


# call the main function
main()
