"""
- Author: Sharif Ehsani
- Date: October 2020
- www.gitbuh.com/ehsanis

Algorithm Workbench
6. Write code that makes a copy of a string with all occurrences of the lowercase letter
't' converted to uppercase.
"""

# main function to start the program
def main():

	# initialize a string variable and assign to it some string
	my_string = "letter t has occured seven times in this string"
	new_string = ''
	my_char = ''

	# loop throught the text and chcek each character
	for ch in my_string:
		# if the checking character equals to t convert it to uppercase and assign it to new_char variable
		# else leave it is lower
		# afte these two statements concatinate the characters to new_string variable
		if ch == 't':
			new_char = ch.upper()
		else:
			new_char = ch.lower()
		new_string = new_string + new_char

	# print the new string
	print(new_string)



# call the main function
main()