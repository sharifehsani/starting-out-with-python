"""
- Author: Sharif Ehsani
- Date: September 2020
- https://github.com/sharifehsani

Checkpoint
9.7 What will the following code display?
mystring = 'abcdefg'
print(mystring[2:5])
"""

# NOTE: this program will print: cde

# main function to start the program
def main():

	# 9.7 What will the following code display? cde
	# line 19 initializes a string variable and assigns 'abcdefg' string to it
	mystring = 'abcdefg'
	# line 21 slices the string from index 0 inclusive to index position 5 not inclusiv and prints
	print(mystring[2:5])


# call the main function
main()
