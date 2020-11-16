"""
- Author: Sharif Ehsani
- Date: November 2020
- www.gitbuh.com/ehsanis

6. Average Number of Words
If you have downloaded the source code from this book’s companion Web site, you will
find a file named text.txt in the Chapter 09 folder. The text that is in the file is stored
as one sentence per line. Write a program that reads the file’s contents and calculates the
average number of words per sentence.
(You can access the book’s companion Web site at www.pearsonhighered.com/gaddis.)
66
"""

# main function to start the program
def main():

	# open the text file as read only
	file_in = open("text.txt", 'r')

	# initialize number of words variable
	number_of_words = 0
	# initialize a counter variable to count the number of sentenses.  a senctence ends with '.'
	number_of_sentence = 0
	# initialize an average variable to calculate the average number of words per sentence
	average_word_count = 0
	# read the content of the file
	data = file_in.read()
	# split the data everytime an space occures
	words = data.split()
	# get the length of words and print
	number_of_words = len(words)
	
	# in a loop iterate through the text and increment the number of sencentse at each occurance of '.'
	for word in data:
		#iterate through each word and find the occurance of dot
		for letter in word:
			if (letter == "."):
				number_of_sentence += 1
	
	# calculate the average number of words per sentence by deviding number of words by number of sentence
	average_word_count = float(number_of_words / number_of_sentence)
	print("Number of words:", number_of_words)
	print("Number of sentences:", number_of_sentence)
	print("Average number of words per sentences:", average_word_count)
	
	# close the file
	file_in.close()

# call the main function
main()
