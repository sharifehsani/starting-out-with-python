"""
- Author: Sharif Ehsani
- Date: December 2020
- https://github.com/sharifehsani

Programming Exercises
4. Unique Words
Write a program that opens a specified text file and then displays a list of all the unique
words found in the file.
Hint: Store each word as an element of a set.
"""

# main function to start the program
def main():

	# open the text file created for programmin exercise 3 called text_to_be_encrypted
	file_in = open('text_to_be_encrypted.txt', 'r')

	# iterate through the text and find words that are part of the body listed below
	# if the unique words found add it to a set that is declared below
	unique_word_set = set()
	body_parts = ['head', 'eye', 'limb', 'nerve', 'heart', ]

	#iterate through the text and through the elements o the list and match the words
	#with the elments of the lest, if found add them to the set
	for line in file_in:
		word = line.split()
		for key in word:
			if key in body_parts:
				unique_word_set.add(key)
			
	# display the set
	print("The elements of the following set was found in the file")
	#print(unique_word_set)
		
# call the main function
main()
