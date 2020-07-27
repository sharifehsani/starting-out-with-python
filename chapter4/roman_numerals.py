"""
- Author: Sharif Ehsani
- Date: June 2020
- www.gitbuh.com/ehsanis

1. Roman Numerals
Write a program that prompts the user to enter a number within the range of 1 through 10.
The program should display the Roman numeral version of that number. If the number is
outside the range of 1 through 10, the program should display an error message. The following
table shows the Roman numerals for the numbers 1 through 10:
Number Roman Numeral
1 ---> I
2 ---> II
3 ---> III
4 ---> IV
5 ---> V
6 ---> VI
7 ---> VII
8 ---> VIII
9 ---> IX
10 ---> X
"""
# main function to start the program
ONE = "I"
TWO = "II"
THREE = "III"
FOUR = "IV"
FIVE = "V"
SEX = "VI"
SEVEN = "VII"
EIGHT = "VIII"
NINE = "IX"
TEN = "X"
def main():
	print("This program promts the user to enter a number between 1 - 10 and then the programs displays the Roman numbral Vrsion of the number.")
	get_input()

# function to get user input
def get_input():
	number = int(input("Please enter a number between 1 - 10 inclusive: "))
	if (number in range(1,11)):
		display_roman_numeral(number)
	else:
		print("Wrong entry. ")
		get_input()

# function to display roman numberal
def display_roman_numeral(number):
	if (number == 1):
		print(number, "in roman numeral is :", ONE)
	elif(number == 2):
		print(number, "in roman numeral is :",TWO)
	elif(number == 3):
		print(number, "in roman numeral is :",THREE)
	elif(number == 4):
		print(number, "in roman numeral is :",FOUR)
	elif(number == 5):
		print(number, "in roman numeral is :",FIVE)
	elif(number == 6):
		print(number, "in roman numeral is :",SEX)
	elif(number == 7):
		print(number, "in roman numeral is :",SEVEN)
	elif(number == 8):
		print(number, "in roman numeral is :",EIGHT)
	elif(number == 9):
		print(number, "in roman numeral is :",NINE)
	else:
		print(number, "in roman numeral is :",TEN)

# call the main function
main()

