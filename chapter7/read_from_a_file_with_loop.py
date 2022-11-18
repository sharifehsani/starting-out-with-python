"""
- Author: Sharif Ehsani
- Date: August 2020
- https://github.com/sharifehsani

This program uses a loop to read data from a file since we don't know how many lines are ther and display
"""

# function to start the program
def main():

	# open the existing file named 'animal_names.txt'
	file_input = open('animal_names.txt','r')

	# read the first line 
	# make a condition for the loop to continue until there is an empty string read (no more line to read)
	end_line = file_input.readline()

	# read the data with a loop
	while (end_line != ''):
		# remove the new line from the end of the line
		end_line = end_line.rstrip('\n')
		# print each line read
		print(end_line)
		end_line = file_input.readline()

		
		

	# close the file
	file_input.close()

# call the main function
main()
