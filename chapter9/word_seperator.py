"""
- Author: Sharif Ehsani
- Date: November 2020
- www.gitbuh.com/ehsanis

11. Word Separator
Write a program that accepts as input a sentence in which all of the words are run together
but the first character of each word is uppercase. Convert the sentence to a string in which
the words are separated by spaces and only the first word starts with an uppercase letter. For
example the string “StopAndSmellTheRoses.” would be converted to “Stop and smell the
roses.”
"""

# main function to start the program
def main():

	# get user input
	my_string = input("Enter a sentence with first char of words in capital without space between words: ")
	start = 0
	new_string = ''
	last = my_string[-1:]
	# in a for loop iterate through the string
	for i in range(len(my_string)-1):				# loop as much as of the lenght-1 of the string to iterate through all
		ch = my_string[i]							# assign character positin to be th ith position
		if (ch.isupper()):							# compare each character for uppercase
			data = my_string[start:i]				# if uppercase letter found slice from zero to that index position
			start = i 								# now the start position will be updated to the next uppercase index position
			last = my_string[i:]					# slice the text, get the last word from the position of Uppercase to the end
			new_string =  new_string  + data + " "  # concatinate each word to get all the words
			
			#print(data)
			#print(last)
	new_string = new_string + last 					# concatinate the last word with the rest
	new_string = new_string.strip()					# strip any whitespace from the front of the text
	new_string = new_string.lower()					# convert all the letters to lowercase
	first_char = new_string[0].upper()				# get the first character of the text and make it uppercase
	rest_char = new_string[1:]						# get the rest of the characters and assign it to a variable
	new_string = first_char + rest_char				# concatenat the first char with the rest
	print(new_string)								# print the new string




# call the main function
main()