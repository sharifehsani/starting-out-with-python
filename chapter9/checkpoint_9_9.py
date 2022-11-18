
"""
- Author: Sharif Ehsani
- Date: September 2020
- https://github.com/sharifehsani

Checkpoint
9.9 What will the following code display?
mystring = 'abcdefg'
print(mystring[:3])

"""

# NOTE: this program slices a string from index position 0 inclusive to the third index not inclusive

# main function to start the program
def main():
	# What will the following code display? abc
	# in line 19, the string 'abcdefg' is assigned to string variable mystring
	mystring = 'abcdefg'
	# in line 22 mystring is sliced from 0th position inclusive to 3rd index position not inclusive and printed
	print(mystring[:3])


# call the main function
main()

