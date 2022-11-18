"""
- Author: Sharif Ehsani
- Date: July 2020
- https://github.com/sharifehsani

3. Write a for loop that displays the following set of numbers:
0, 10, 20, 30, 40, 50 . . . 1000
"""

# main function to start the program
def main():
	print() 	# blanck line to seperate the program from the command line for readablity
	print('This program prints numbers from 0 to 1000 with increment of 10 using for loop.')

	for number in range(0,1010,10):		# 0 is the lower limit 1010 is the upper limit because range does not include 1000
		print(number)

# call the main function
main()
