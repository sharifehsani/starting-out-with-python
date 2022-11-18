"""
- Author: Sharif Ehsani
- Date: September 2020
- https://github.com/sharifehsani

# in this exercise we work a bit with the string testing methods
"""

# main function to start the program
def main():

	# in this exercise all the methods test strings
	# initialize a string variable and assing some text to it
	my_string = "abC123"
	print("String = ", my_string)

	# isdigit() method returns True if the string is digit only
	# check if the string is digit only. if it is digit only it will print True, False other wise
	# it should print False since the string has mix of text and digit
	print("isdigit() ", my_string.isdigit())

	# isalnum() method returns True if the string is alphanumeric meaning 0,1,2,...9 and a, b....z
	print("isalnum()", my_string.isalnum())

	# isalpha() Returns true if the string contains only alphabetic letters, and is at least one
	# character in length. Returns false otherwise.
	print("isalpha()", my_string.isalpha())

	# islower() Returns true if all of the alphabetic letters in the string are lowercase, and the
	# string contains at least one alphabetic letter. Returns false otherwise.
	print("islower() ", my_string.islower())

	# isupper() Returns true if all of the alphabetic letters in the string are uppercase, and the
	# string contains at least one alphabetic letter. Returns false otherwise.
	print("isupper()", my_string.isupper())

	# isspace() Returns true if the string contains only whitespace characters, and is at least one
	# character in length. Returns false otherwise. (Whitespace characters are spaces,
	# newlines (\n), and tabs (\t).

	print("isspace()", my_string.isspace())


# call the main function
main()
