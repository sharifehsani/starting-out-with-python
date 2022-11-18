"""
- Author: Sharif Ehsani
- Date: September 2020
- https://github.com/sharifehsani

Checkpoint
8.21 Write a set of nested loops that display the contents of the numbers list shown in
Checkpoint question 8.19.
"""


# function to start the program
def main():

	# the following list was create earlier in checkpoint 8.21
	# with 4 rows and 2 colomns
	numbers = [[1, 2], 
				[10, 20], 
				[100, 200], 
				[1000, 2000]]



	# in a nested loop display the content of he numbers list
	for r in range(4):
		print('Row ', r + 1, ": ", end='')
		for c in range(2):
			print(numbers[r][c], end=' ')
		print(',')

	print(numbers[0][3])

# call the main function
main()
