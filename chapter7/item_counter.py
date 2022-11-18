"""
- Author: Sharif Ehsani
- Date: August 2020
- www.gitbuh.com/ehsanishttps://github.com/sharifehsani

Programming Exercises
4. Item Counter
Assume that a file containing a series of names (as strings) is named names.txt and exists on the computer’s disk.
Write a program that displays the number of names that are stored in the file. (Hint: Open the file and read every string
stored in it. Use a variable to keep a count of the number of items that are read from the file.)
"""

# NOTE: lets first creat the file in the first portion of the file and in the second portion we executed the item counter exerciese

# function to start the program
def main():

	# creat a text file called 'my_names.txt'
	# lets use context manager for openig the file. context manager is an easier way to manipulate file
	# context manager closes the file automatically

	with open('my_names.txt', 'w') as f:

		# lets input the content of the file from keyboard
		name_count = int(input("How many names do you want to add?: "))

		for count in range(1, name_count + 1):
			name = input("Enter name: ")
			f.write(name + '\n')


	# _________________ second part of the program _____________________________

	# open the created file 'names.txt'
	print("now lests read the content")
	counter = 0

	# open the file with context manager which closes the file automaticaly
	with open('my_names.txt', 'r') as f:
		# in a loop read the content of file
		for line in f:
			# remove the new line character from the end of the line
			line = line.rstrip('\n')
			# increment the counter
			counter += 1
		print("Number of names read: ", counter)
		


# call the main function
main()

