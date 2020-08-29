"""
- Author: Sharif Ehsani
- Date: August 2020
- www.gitbuh.com/ehsanis

This program appends date to an existing file with some data using the 'a' access mode.
'a' mode will not erease the content of a file, but appends to the end of it
lets add number of courses and school year to the 'student_info.txt' file
"""

# function to start the program
def main():

	# get user input for number of courses and school year
	number_of_course = input("Enter Number of Courses: ")
	school_year = input("Enter school year: ")

	# open the file 'student_info.txt' in 'a' append access mode
	file_input = open('student_info.txt', 'a')

	# append the new user input to the end of the file with new line at the end
	file_input.write(number_of_course + '\n')
	file_input.write(school_year + '\n')

	# close the file
	file_input.close()

	# lets now open the file again in 'r' read mode to check if the data is added
	file_input_again = open('student_info.txt', 'r')

	# now read the lines one by one as we know there should be 8 lines now
	
	first_name = file_input_again.readline()
	last_name = file_input_again.readline()
	date_of_birth = file_input_again.readline()
	student_id = file_input_again.readline()
	faculty = file_input_again.readline()
	major = file_input_again.readline()
	num_of_course = file_input_again.readline()
	school_y = file_input_again.readline()

	# now that the lines are read remove the new lines from the end of the lines
	first_name = first_name.rstrip('\n')
	last_name = last_name.rstrip('\n')
	date_of_birth = date_of_birth.rstrip('\n')
	student_id = student_id.rstrip('\n')
	faculty = faculty.rstrip('\n')
	major = major.rstrip('\n')
	num_of_course = num_of_course.rstrip('\n')
	school_y = school_y.rstrip('\n')

	# print the data read from the file
	print()
	print("The following infor was read from the file.")
	print("First name: ", first_name)
	print("last name: ", last_name)
	print("date of birth: ", date_of_birth)
	print("student_id: ", student_id)
	print("faculty: ", faculty)
	print("major: ", major)
	print("Number of courses: ", num_of_course)
	print("School_year: ", school_y)

# call the main funcion
main()