"""
- Author: Sharif Ehsani
- Date: September 2020
- https://github.com/sharifehsani

The repetition operator (*) works with string the same way it worked with lists
lets use some examples

"""

# main function to start the program
def main():

	# initialize a string variable
	my_string = 'Hello'

	# use the repetiotion operator to print the string 5 times
	print(my_string * 5)

	# using the repetition operator (*) print a shape, a triangle of x's

	for num in range(1, 10):
		print ("X" * num)

	# print another shape
	for num in range(10, 1, -1):
		print("x" * num)

# call the main function
main()
