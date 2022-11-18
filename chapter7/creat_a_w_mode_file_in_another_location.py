"""
- Author: Sharif Ehsani
- Date: August 2020
- https://github.com/sharifehsani

This program creates a file in a location other than the directory where the program is (like desktop)
"""

# function to start the program
def main():

	# pass file name, its location and its mode to open function and assign it to file variable

	test_file = open(r'C:\Users\Administrator\Desktop\test.txt', 'w')


# call the main function
main()
