"""
- Author: Sharif Ehsani
- Date: September 2020
- https://github.com/sharifehsani

Checkpoint
9.19 Assume the following statement appears in a program:
values = 'one$two$three$four'
Write a statement that splits the string, creating the following list:
['one', 'two', 'three', 'four']
"""

# main function to start the program
def main():

	# initialize string variable 
	values = 'one$two$three$four'

	# Write a statement that splits the string, creating the following list:
	# ['one', 'two', 'three', 'four']

	new_values = values.split('$')

	# print before and after split
	print(values)
	print(new_values)

# call the main function
main()
