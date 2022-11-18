"""
- Author: Sharif Ehsani
- Date: October 2020
- https://github.com/sharifehsani

Algorithm Workbench
10. Look at the following statement:
mystring = 'cookies>milk>fudge>cake>ice cream'
Write a statement that splits this string, creating the following list:
['cookies', 'milk', 'fudge', 'cake', 'ice cream']

"""

# define the main function to start the program
def main():

	# initialize a string variable and assing a text to it
	mystring = 'cookies>milk>fudge>cake>ice cream'

	# initialize a list to hold the splited strings
	

	# split the string from where > occures and append it to the new_list variable
	new_list = mystring.split('>')

	# print the list
	print(new_list)


# call the main function
main()

