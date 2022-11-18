"""
- Author: Sharif Ehsani
- Date: December 2020
- https://github.com/sharifehsani

Programming Exercises
5. Word Frequency
Write a program that reads the contents of a text file. The program should create a dictionary
in which the keys are the individual words found in the file and the values are the
number of times each word appears. For example, if the word “the” appears 128 times,
the dictionary would contain an element with 'the' as the key and 128 as the value.
The program should either display the frequency of each word or create a second file
containing a list of each word and its frequency.
"""
# main function to start the program
def main():

	# declare a list to hold the words and a dictionary variable to hold words and their count
	word_dict = {}
	my_list = []

	#declare a counter to hold the frequency of the word apperance
	word_count = 0

	# open the text file created earlier for exercise # 3 called text_to_be_encrypted.txt
	file_in = open('text_to_be_encrypted.txt', 'r')

	
	# iterate through the file and put each word in a list
	for line in file_in:
		for word in line.split():		# split the lines to get words
			word = word.lower()			# convert the words to lower case
			my_list.append(word)		# add the words to the list
			
	# in another for loop iterate throug the list items to get the count
	for word in my_list:
		word_count = my_list.count(word)
		key = word.lower()
		word_dict[key] = word_count		# add the key and value to the dictonary
	# display the dictinary
	print("The follwoing code shows how many times a word appeared in the text.")
	print(word_dict)



# call the main function
main()
