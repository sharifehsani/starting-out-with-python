"""
- Author: Sharif Ehsani
- Date: September 2020
- www.gitbuh.com/ehsanis

Checkpoint
9.8 What will the following code display?
mystring = 'abcdefg'
print(mystring[3:])

"""

# NOTE: this program slices the string from index position 3 inclusive to the end of the string

# main function to start the program
def main():

	# 9.8 What will the following code display? defg
	# in line 19 the string 'abcdefg' is assigned to string variable mystring
	mystring = 'abcdefg'
	# in line 22, mystring is sliced from index position 3 to the end of the string inclusiv
	# and prints the result which will be defg
	print(mystring[3:])


# call the main function
main()