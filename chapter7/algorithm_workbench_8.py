"""
- Author: Sharif Ehsani
- Date: August 2020
- https://github.com/sharifehsani

Algorithm Workbench
8. A file exists on the disk named students.txt. The file contains several records, and each record contains two 
fields: (1) the student’s name, and (2) the student’s score for the final exam. Write code that changes Sharif Ehsani's final score to 100.
"""

# import os as it is needed to rename and remove files
import os

# function to start the program
def main():

	# create boolean variable to set flag
	match_found = False

	# the 'students.txt' file was created earlier so lets work with that
	# open the file to read data
	file_in = open("students.txt", 'r')

	# also creat a temporary file to write data on
	temporary_file = open("temporary_file.txt", 'w')

	# get user input
	student_name = input("Type the name of the student to change his/ her score: ")

	# read the first line
	name_field = file_in.readline()

	# in a loop read all the lines in the file until there is no line to be read
	while (name_field != ''):
		# read the score field of the record and convert to int value
		score = int(file_in.readline())


		# strip the new line from the end of the name field
		name_field = name_field.rstrip('\n')

		# check if the searched name matches the student name
		if (student_name == name_field):

			# if the record searched is found then get the new score
			new_score = int(input("Enter the new score: "))

			# write both fields to the temporary file
			temporary_file.write(name_field + '\n')
			temporary_file.write(str(new_score) + '\n')

			# change the boolean value to true
			match_found = True

		else:
			temporary_file.write(name_field + '\n')
			temporary_file.write(str(score) + '\n')

		# read the next line
		name_field = file_in.readline()


	# close both files
	file_in.close()
	temporary_file.close()

	# delet the original file
	os.remove('students.txt')

	# rename the temporary file to original file
	os.rename("temporary_file.txt", 'students.txt')

	# print message
	if (match_found == True):
		print("Record updated.")

	else:
		print("Record not found.")


# call the main function
main()











