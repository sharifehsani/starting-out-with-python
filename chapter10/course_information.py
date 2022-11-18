"""
- Author: Sharif Ehsani
- Date: December 2020
- https://github.com/sharifehsani

Programming Exercises
1. Course information
Write a program that creates a dictionary containing course numbers and the room numbers
of the rooms where the courses meet. The dictionary should have the following keyvalue
pairs:
Course Number (key)			 Room Number (value)
CS101 						3004
CS102 						4501
CS103 						6755
NT110 						1244
CM241 						1411
The program should also create a dictionary containing course numbers and the names of
the instructors that teach each course. The dictionary should have the following key-value
pairs:
Course Number (key)			Instructor (value)
CS101 						Haynes
CS102 						Alvarado
CS103 						Rich
NT110 						Burke
CM241 						Lee
The program should also create a dictionary containing course numbers and the meeting
times of each course. The dictionary should have the following key-value pairs:
Course Number (key) 		Meeting Time (value)
CS101 						8:00 a.m.
CS102 						9:00 a.m.
CS103 						10:00 a.m.
NT110 						11:00 a.m.
CM241 						1:00 p.m.
The program should let the user enter a course number, and then it should display the
course’s room number, instructor, and meeting time.
"""

# main functon to start
def main():

	# create a dictonary with course numbers and room numbers as key-value pairs
	course_name_number = {"CS101":3004, "CS102":4501, "CS103":6755, "NT110": 1244, "CM241":1411}

	# create a dictonary with course numbers and instructor name as key-value pairs
	course_instructor = {"CS101":"Hayness", "CS102":"Alvarado", "CS103": "Rich", "NT110": "Burke", "CM241":"Lee"}

	# create a dictonary with course numbers and lecture time as key-value pairs
	course_time = {"CS101":"8:00 a.m.", "CS102":"9:00 a.m.", "CS103": "10:00 a.m.", "NT110": "11:00 a.m.", "CM241":"1:00 p.m."}

	# ask the user to enter a course number
	print("Course Names: CS101, CS102, CS103, NT110, CM241")
	user_input = input("Enter a cours number.")
	if (user_input in course_name_number and user_input in course_instructor and user_input in course_time):
		room = course_name_number.get(user_input)		# use get method to get the value for number
		instructor = course_instructor.get(user_input)	# use get method to get the value(instructor)
		time = course_time.get(user_input)				# use the get method to get the value(time)

		# display the result
		print("Coure Name:", user_input)
		print("Lecture room:", room)
		print("Instructor:", instructor)
		print("Time:", time)
	else:
		print("Course does not exist.")

	

# call the main function
main()
