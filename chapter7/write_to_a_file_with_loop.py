"""
- Author: Sharif Ehsani
- Date: August 2020
- https://github.com/sharifehsani

This program uses a loop to write data on a file asking the user to enter the name of animals
"""

# function to start the program
def main():

	# creat a new text file to store names of animals called 'animal_names.txt'
	file_animal_names = open('animal_names.txt', 'w')

	# get user input and the counter for the loop
	counter = int(input("How many animals do you want to name? "))

	# using a loop write to the file
	for count in range(1, counter + 1):
		# get the name of the animal
		name_of_animal = input("Enter the name of the animal: ")
		# write the anme of the animal with a new line
		file_animal_names.write(name_of_animal + '\n')

	# close the file
	file_animal_names.close()


# call the main function
main()
