
"""
- Author: Sharif Ehsani
- Date: September 2020
- https://github.com/sharifehsani

Checkpoint
9.17 Write a loop that counts the number of uppercase characters that appear in the
string referenced by the variable mystring.

"""

# main function to start the program
def main():

	# initialize a string variable
	my_string = 'Roses are red, Violets are blue, Honey is weet And so are you'

	# in a loop check how many uppercase letter in ther
	# initialize a counter variable
	count = 0

	for ch in my_string:
		if (ch.isupper()):
			count += 1

	print(count, "upper case letters exist in the string.")


# call the main function
main()
