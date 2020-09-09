"""
- Author: Sharif Ehsani
- Date: August 2020
- www.gitbuh.com/ehsanis

Checkpoint
8.4 What will the following code display?
numbers = list(range(1, 10, 2)) 
for n in numbers:
print(n)
"""

# function to start the program
def main():

	# in this statement range() function generates integers from 1, 10 with 2 apart from each other
	numbers = list(range(1, 10, 2)) 
	# this for loop runs through the list numbers and prints the elements
	for n in numbers:
		# this print statement the elements of the list 1, 3, 5, 7, 9
		print(n)


# call the main function
main()