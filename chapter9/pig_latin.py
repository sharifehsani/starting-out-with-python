"""
- Author: Sharif Ehsani
- Date: November 2020
- https://github.com/sharifehsani

12. Pig Latin
Write a program that accepts a sentence as input and converts each word to “Pig Latin.” In
one version, to convert a word to Pig Latin you remove the first letter and place that letter at
the end of the word. Then you append the string “ay” to the word. Here is an example:
English: I SLEPT MOST OF THE NIGHT
Pig Latin: IAY LEPTSAY OSTMAY FOAY HETAY IGHTNAY
"""

# main function to start the program
def main():

	# get user input
	my_string = input("Enter a sentence and I return it in pig latin back: ")

	#initialize a variable and assign "AY" to it
	ay = 'AY'
	new_string = ''
	# split the words from space
	data = my_string.split()
	# in a for loop iterate through the list
	for word in data:
		word = word.upper()								# conver the word to uppercase
		first_char = word[0]							# extact the first char
		rest_of_th_word = word[1:]						# extract the resto the word
		new_word = rest_of_th_word + first_char + ay 	# concatinate the rest of the word with first char and ay
		new_string = new_string + new_word + ' '		# concatinate the words to make sentence and space in between

	new_string = new_string[0:-1]						# remove the last space character from the end of the sentnce
	print(new_string)




# call the main function
main()
