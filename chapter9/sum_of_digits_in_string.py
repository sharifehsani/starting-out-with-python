"""
- Author: Sharif Ehsani
- Date: October 2020
- https://github.com/sharifehsani

Programming Exercises
2. Sum of Digits in a String
Write a program that asks the user to enter a series of single-digit numbers with nothing
separating them. The program should display the sum of all the single digit numbers in the
string. For example, if the user enters 2514, the method should return 12, which is the sum
of 2, 5, 1, and 4.
"""

# main functin to start the program
def main():

	# ask th user to enter a series of single-degit numbers
	number_series = input("Enter a serise of single-degit numbers: ")

	# get each character of the string convert it to int and add them together
	sum = 0
	for ch in number_series:
		number = int(ch)
		sum = sum + number

	# print the result
	print("The sum of the digits is: ", sum)


# call the main function
main()
