"""
- Author: Sharif Ehsani
- Date: December 2020
- https://github.com/sharifehsani

Algorithm Workbench
4. Assume the variable dct references a dictionary. Write an if statement that determines
whether the key 'Jim' exists in the dictionary. If so, delete 'Jim' and its associated
value.
"""

# main function to start the program
def main():

	# declare a dictionary with key 'jim' and a value in it
	dct = {'jim': 403}
	print("dictoionary before delete:", dct)

	del dct['jim']

	print("dictoionary after delete:", dct)


# call the main function
main()
