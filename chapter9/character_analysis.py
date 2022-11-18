"""
- Author: Sharif Ehsani
- Date: November 2020
- https://github.com/sharifehsani

7. Character Analysis
If you have downloaded the source code from this book’s companion Web site, you will
find a file named text.txt in the Chapter 09 folder. Write a program that reads the file’s
contents and determines the following:
• The number of uppercase letters in the file
• The number of lowercase letters in the file
• The number of digits in the file
• The number of whitespace characters in the file
(You can access the book’s companion Web site at www.pearsonhighered.com/gaddis.)
"""

# main function to start the program
def main():

	# initialize uppercase_count variable, lowercase_count, is_digit_count and whitspace_count to
	# hold the number of uppercase, lowercase, digit an whitspace counts
	uppercase_count = 0
	lowercase_count = 0
	digit_count = 0
	whitespace_count = 0

	# open the text file
	file_in = open("text.txt", 'r')

	# read the content of the file
	data = file_in.read()
	#  in a loop iterate through each letter and words
	for words in data:
		for letters in words:
			# compare if the letter is uppercase, if so increment the counter
			if (letters.isupper()):
				uppercase_count += 1
			# compare if the letter is lowerercase, if so increment the counter
			if (letters.islower()):
				lowercase_count += 1
			# compare if the letter is digit, if so increment the counter
			if (letters.isdigit()):
				digit_count += 1
			# compare if the letter whitespace, if so increment the counter
			if (letters.isspace()):
				whitespace_count += 1

	print("Number of uppercase letters:", uppercase_count)
	print("Number of lowercase letters:", lowercase_count)
	print("Number of digits:", digit_count)
	print("Number of whitespace:", whitespace_count)


# call the main function
main()
