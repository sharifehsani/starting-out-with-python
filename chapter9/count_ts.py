"""
- Author: Sharif Ehsani
- Date: September 2020
- https://github.com/sharifehsani

This program get a user input, a string and checks if letter t or T appears in the string.
If it does apear, how many times

"""

# main function to start the program
def main():

	# initialize an accumulator variable to hold the number of t's in the string
	total_t = 0
	# initialize a boolean variable to use if condition is true or false
	fount = False

	# get user input
	text = input("Please enter some text: ")

	# in a loop iterate through the characters of the string
	for letter in text:
		# match every character with t or T
		if ( letter == 't' or letter == 'T'):
			# count the number of ts
			total_t += 1
			# the boolean variable found is assigned to True if t found in text
			fount = True
	
	# print the result after processing the text
	if (fount == True):
		print(total_t, "number of 't' found in the text.")
	else:
		print("No 't' was found in the text")

# call the main function
main()
