"""
- Author: Sharif Ehsani
- Date: August 2020
- www.gitbuh.com/ehsanis

Algorithm Workbench
7. A file exists on the disk named students.txt. The file contains several records,
and each record contains two fields: (1) the student’s name, and (2) the student’s
score for the final exam. Write code that deletes the record containing “John Perz”
as the student name.
"""
# import os for file remove and file rename
import os

# function to start the program
def main():

	# since the file 'students.txt' does not exist, we first creat this file in this
	# code and creat a few records then do the rest of question 7

	# open the file named 'students.txt' in 'w' mode
	file_out = open('students.txt', 'w')

	# get a few records from the user and add to the file
	# ask the user how many records wants to add
	number_of_records = int(input("How many student records do you want to add: "))

	# creat a loop and get the records fields
	for num in range(1, number_of_records + 1):
		print("Enter name and score for student # ", num)
		# get user's name
		student_name = input("Name: ")
		# get user's score
		final_score = int(input("Score: "))

		# write the name and score fileds to the file
		file_out.write(student_name + '\n')
		# convert the float value to string before writting
		file_out.write(str(final_score) + '\n')

	# close the file 
	file_out.close()

	# The main part of the code
	# ________________________________________________________________________________________

	# creat a boolean value to to set a flag
	match_found = False

	# creat a temporary file to write the fields over
	temp_file = open('temporary_student_file.txt', 'w')

	# get the record search from the user
	name = input("Which student's record do you want to delet: ")

	# open the file again to delete one of the records
	file_in = open('students.txt', 'r')

	# read the first line
	student_name = file_in.readline()

	# in a while loop read until there is not line to be read
	while (student_name != ''):

		# read the next line and convert it to int
		student_score = int(file_in.readline())

		# strip the new line from the end of the line
		student_name = student_name.rstrip('\n')
		

		# check if the searched record matches
		# if the name searched does not match the records write them to the temporary file
		if (name != student_name):
			# write the fields to the temp file
			temp_file.write(student_name + '\n')
			temp_file.write(str(student_score) + '\n')	# make sure to covert to string before writting to file

			# set bollean variable to true
			match_found = True

		# read the next field
		student_name = file_in.readline()

	# close the original file
	file_in.close()
	# close the temporary file
	temp_file.close()

	# print a message
	if (match_found == True):
		print('Match not found.')
	else:
		print("Record updated.")

	# delet the original file and make sure import os is done
	os.remove('students.txt')

	# rename the temporary file to original name
	os.rename('temporary_student_file.txt','students.txt')



# call the main function
main()









