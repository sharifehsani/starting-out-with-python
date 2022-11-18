"""
- Author: Sharif Ehsani
- Date: August 2020
- https://github.com/sharifehsani

this program gets user input and writes it on to a file with 'w' mode. w mode erease all the content of an existing
file, if it does not exist it will creat one. so lets creat a new file to not overwrite other files
"""

# function to start the program
def main():

	# get student's information from the user
	f_name = input("Enter your first name: ")
	l_name = input("Enter your last name: ")
	date_of_birth = input("Enter your date of birth. MM/DD/YYYY: ")
	student_id = input("Enter your 5 degit student ID: ")
	faculty = input("Enter your faculty: ")
	major = input("Enter your field of study: ")

	# open or creat new file named 'student_info.txt' with 'w' extension

	student_info_file = open('student_info.txt', 'w')

	# now that the file is created and opened write the user input to the file each info in a seperate line
	# add \n new line after each write
	student_info_file.write(f_name + '\n')
	student_info_file.write(l_name + '\n')
	student_info_file.write(date_of_birth + '\n')
	student_info_file.write(student_id + '\n')
	student_info_file.write(faculty + '\n')
	student_info_file.write(major + '\n')

	# now that all the entries are written to the file, close the file
	student_info_file.close()


# call the main function
main()
