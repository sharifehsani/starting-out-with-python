"""
- Author: Sharif Ehsani
- Date: July 2020
- https://github.com/sharifehsani

7. Write a set of nested loops that display 10 rows of # characters. There should be
15 # characters in each row.
"""

# main function to start the program
def main():
	print()
	print('This program prints 10 rows of # characters with 15 # in each row. ')

	for rows in range(10):
		for columns in range(15):
			print('#', end='')

		print()


# call the main function
main()
