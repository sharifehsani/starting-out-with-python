"""
- Author: Sharif Ehsani
- Date: September 2020
- www.gitbuh.com/ehsanis

Algorithm Workbench
2. Write a loop that counts the number of space characters that appear in the string referenced
by mystring.
"""

# main function to start the program
def main():

	# initialize a vriable to hold the count
	count = 0
	# initialize a variable string and assign some string to it
	mystring = 'Roses are red, Violets are blue.'

	# in a loop counts the number of spaces that appear in the string 
	for ch in mystring:
		if (ch == ' '):
			count += 1

	# print the result
	print(count, "space characters appear in the string: ", '"', mystring, '"', sep='')


# call the main function
main()