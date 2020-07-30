"""
- Author: Sharif Ehsani
- Date: July 2020
- www.gitbuh.com/ehsanis

9. Write a program that uses nested loops to draw this pattern:
*******
******
*****
****
***
**
*
"""
astericks = '*'
# main function to start the program
def main():
	print()
	print("This program prints a triange pattern of astericks.")
	astericks = '*'
	for row in range(7,0,-1):
		print(astericks * row)


# call the main function
main()