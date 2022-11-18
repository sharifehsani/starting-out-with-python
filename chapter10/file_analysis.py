"""
- Author: Sharif Ehsani
- Date: December 2020
- https://github.com/sharifehsani

Programming Exercises
6. File Analysis
Write a program that reads the contents of two text files and compares them in the following
ways:
• It should display a list of all the unique words contained in both files.
• It should display a list of the words that appear in both files.
• It should display a list of the words that appear in the first file but not the second.
• It should display a list of the words that appear in the second file but not the first.
• It should display a list of the words that appear in either the first or second file but not both.
Hint: Use set operations to perform these analyses.
"""

# main function to start the program
def main():

	# declare two set variables 
	set_one = set()
	set_two = set()

	# NOTE. the twho text file are called text_one.txt and text_two.txt
	# open both text files
	file_one_in = open('text_one.txt', 'r')
	file_two_in = open('text_two.txt', 'r')

	# read the content of the first file and put them in the first set
	for line in file_one_in:
		for word in line.split():
			set_one.add(word)
	
	# read the content of the second file and put them in the second set
	for line in file_two_in:
		for word in line.split():
			set_two.add(word)

	# display the sets
	print()
	print("Words in file one: ")
	print(set_one)

	print()
	print("Words in file two: ")
	print(set_two)

	# take the intersection of the the two sets to display the unique words that apear in both files
	intersect_words = set_one.intersection(set_two)
	print()
	print("Words that are shared in both files: ")
	print(intersect_words)

	# take the union of both the files and display all the words of both files
	union_words = set_one.union(set_two)
	print()
	print("Words that appear in both files: ")
	print(union_words)

	# take the differnce of both the sets to show the words that appear in file one but not file two
	differnce_words = set_one.difference(set_two)
	print()
	print("Words that appear only in file one: ")
	print(differnce_words) 

	# take the differnce of both the sets to show the words that appear in file two but not file one
	differnce_words_one = set_two.difference(set_one)
	print()
	print("Words that appear only in file two: ")
	print(differnce_words_one)


	# take the symmetric differnce of both the sets to show the words that are not shared in both files
	sym_differnce_words = set_one.symmetric_difference(set_two)
	print()
	print("Words that not shared between the files: ")
	print(sym_differnce_words)


# call the main function
main()
