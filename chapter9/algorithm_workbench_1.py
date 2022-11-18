"""
- Author: Sharif Ehsani
- Date: September 2020
- https://github.com/sharifehsani

Algorithm Workbench
1. Assume choice references a string. The following if statement determines whether
choice is equal to ‘Y’ or ‘y’:
if choice == 'Y' or choice == 'y':
Rewrite this statement so it only makes one comparison and does not use the or operator.
(Hint: use either the upper or lower methods.)
"""

# main function to start the program
def main():

	# Assume choice references a string.
	choice = 'y'

	if (choice.lower() == 'Y'):
		print("Upper Y")
	else:
		print("Lower y")

# call the main function
main()	
