"""
- Author: Sharif Ehsani
- Date: November 2020
- www.gitbuh.com/ehsanis

10. Most Frequent Character
Write a program that lets the user enter a string and displays the character that appears
most frequently in the string.
"""

# main function to start the program
def main():

	count = 0
	# get user input for the string
	my_string = input("Enter a string and I display the character that appears the most: ")
	
	# in a loop iterate through the string
	counter = 1
	for i in my_string:
		char_count = my_string.count(i)
		if char_count > counter:
			counter = char_count
			most_frequent = i
	print("Most frequent letter:", most_frequent)

# call the main function
main()