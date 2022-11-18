
"""
- Author: Sharif Ehsani
- Date: August 2020
- https://github.com/sharifehsani

this program reads the content of an existing file named 'student_info.txt' with 'r' mode access
"""

# function to start the program
def main():

	# creat a file variable and open the file, since we know there are 6 lines in that file
	# so we read that 6 lines one by one
	student_info = open('student_info.txt', 'r')
	f_name = student_info.readline()
	l_name = student_info.readline()
	date_of_birth = student_info.readline()
	student_id = student_info.readline()
	faculty = student_info.readline()
	major = student_info.readline()

	# close the file after done reading
	student_info.close()

	# print the data read
	print()
	print("The following infor was read from the file.")
	print("First name: ", f_name)
	print("last name: ", l_name)
	print("date of birth: ", date_of_birth)
	print("student_id: ", student_id)
	print("faculty: ", faculty)
	print("major: ", major)


# call the main function
main()
