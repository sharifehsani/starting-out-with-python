"""
- Author: Sharif Ehsani
- Date: November 2020
- www.gitbuh.com/ehsanis

9. Vowels and Consonants
Write a program with a function that accepts a string as an argument and returns the number
of vowels that the string contains. The application should have another function that accepts a string as an argument
and returns the number of consonants that the string contains.
The application should let the user enter a string and should display the number of
vowels and the number of consonants it contains.

"""


# function that counts the number of vowels in the text. It recieves a string as parameter and returns the 
# number of vowels in the text
def count_vowels(st):
	# initialize vowel variables and assign them their values as character
	a = 'a'
	e = 'e'
	i = 'i'
	o = 'o'
	u = 'u'

	# initizlize counter to hold the number of vowels
	num_of_vowels = 0
	# in a loop iterate through the text and compare each character with the vowel variables
	for ch in st:
		
		if ((ch == a) | (ch == e) | (ch == i) | (ch  == o) | (ch == u)):
			num_of_vowels += 1

	return num_of_vowels


# function that counts the number of constants in the text. It recieves a string as parameter and returns the 
# number of constants in the text
def count_consonants(st):
	# initialize vowel variables and assign them their values as character
	a = 'a'
	e = 'e'
	i = 'i'
	o = 'o'
	u = 'u'

	# initizlize counter to hold the number of consonants
	num_of_consonants = 0
	# in a loop iterate through the text and compare each character with the vowel variables
	for ch in st:
		if ((ch != a) & (ch != e) & (ch != i) & (ch  != o) & (ch != u) & (ch != '.') & (ch != ' ')):
			num_of_consonants += 1

	return num_of_consonants

# main function to start the program
def main():
	# get user input for the string
	my_string = input("Please enter some string and the programs tells you the number of vowels and consonants: ")

	# call the function that counts the number of vowels and passs the string as a paramter
	# assign the result of the returned value to the num_of_vowels variable
	num_of_vowels = count_vowels(my_string)

	# call the function that counts the number of consonants and passs the string as a paramter
	# assign the result of the returned value to the num_of_consonants variable
	num_of_consonants = count_consonants(my_string)

	# print the returned values
	print("Number of vowels in the text: ", num_of_vowels)
	print("Number of consonants in the text: ", num_of_consonants)

# call the main function
main()