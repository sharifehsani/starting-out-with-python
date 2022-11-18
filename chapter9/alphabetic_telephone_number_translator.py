"""

- Author: Sharif Ehsani
- Date: October 2020
- https://github.com/sharifehsani

5. Alphabetic Telephone Number Translator
Many companies use telephone numbers like 555-GET-FOOD so the number is easier for
their customers to remember. On a standard telephone, the alphabetic letters are mapped
to numbers in the following fashion:
A, B, and C = 2
D, E, and F = 3
G, H, and I = 4
J, K, and L = 5
M, N, and O = 6
P, Q, R, and S = 7
T, U, and V = 8
W, X, Y, and Z = 9
Write a program that asks the user to enter a 10-character telephone number in the format
XXX-XXX-XXXX. The application should display the telephone number with any alphabetic
characters that appeared in the original translated to their numeric equivalent. For
example, if the user enters 555-GET-FOOD the application should display 555-438-3663.
"""

# main function to start the program
def main():

	# get user input
	phone_number = input("Please enter a 10 degit phone number with area cod as a number and the rest alphabetic: ")
	# seperate the aread code (3 first digit) since the use enters it as a number anyways
	area_code = phone_number[0:3]
	# seperate the rest of of the number till the end
	the_number = phone_number[4:]
	# convert the user input (second part of the number to uppercase) just in case user enters as lower or uppercase
	the_number = the_number.upper()
	char = 0
	# initialize a variable called number to concatinate each number after matched
	number = str(area_code)

	# in a loop etirate through the characters and match with the number
	# if i matches with any letter assigne the number assocated to it to variable char
	# and concatinate char variable with number variable and keep doing it tille the end of the 
	# string and keep matching
	for i in the_number: 
		if (i == 'A' or i == 'B' or i == 'C'):
			char = 2
			number = number + str(char)

		elif (i == 'D' or i == 'E' or i == 'F'):
			char = 3
			number = number + str(char)
			
		elif (i == 'G' or i == 'H' or i == 'I'):
			char = 4
			number = number + str(char)

		elif (i == 'J' or i == 'K' or i == 'L'):
			char = 5
			number = number + str(char)

		elif (i == 'M' or i == 'N' or i == 'O'):
			char = 6
			number = number + str(char)

		elif (i == 'P' or i == 'Q' or i == 'R' or i == 'S'):
			char = 7
			number = number + str(char)

		elif (i == 'T' or i == 'U' or i == 'V'):
			char = 8
			number = number + str(char)

		elif (i == 'W' or i == 'X' or i == 'Y' or i == 'Z'):
			char = 9
			number = number + str(char)

	# slice the string to add the '-' between the numbers
	first_part_number = number[0:3]
	second_part_number = number[3:6]
	last_part_number = number[6:]
	all_number = first_part_number + '-' + second_part_number + '-' + last_part_number +'.'
	# print the result
	print(all_number)
	
	

# call the main function
main()
