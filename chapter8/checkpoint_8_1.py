"""
- Author: Sharif Ehsani
- Date: August 2020
- www.gitbuh.com/ehsanis

Checkpoint
8.1 What will the following code display?
numbers = [1, 2, 3, 4, 5]
numbers[2] = 99 
print(numbers)

"""

# main function to start the program
def main():

	# this line initializes the numbers variabe as a list and assigns [1, 2, 3, 4, 5] to it
	numbers = [1, 2, 3, 4, 5]

	# this line inserts 99 to index position 2, so basically changes the value of index position 2 to 99
	numbers[2] = 99

	# this should print [1, 2, 99, 4, 5]
	print(numbers)



# call the main function
main()