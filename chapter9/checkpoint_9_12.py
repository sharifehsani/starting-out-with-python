"""
- Author: Sharif Ehsani
- Date: September 2020
- https://github.com/sharifehsani

Checkpoint
9.12 Assume the variable big references a string. Write a statement that converts the
string it references to lowercase, and assigns the converted string to the variable
little.

"""

# main function to start the program
def main():

	# initialize string variable
	big = 'Roses are red, Violets are blue, Honey is sweet, And so are you.'

	# convert the string that is assigned to variable big to lowercase and assign the new string to variable little
	little = big.lower()

	# print the before and after string
	print("This is the original string: ", big)
	print("This is the new string converted to lowercase: ", little)

# call the main function
main()
