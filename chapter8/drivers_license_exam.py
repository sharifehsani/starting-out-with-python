"""
- Author: Sharif Ehsani
- Date: September 2020
- www.gitbuh.com/ehsanis

Programming Exercises
6. Driver’s License Exam
The local driver’s license office has asked you to create an application that grades the written portion 
of the driver’s license exam. The exam has 20 multiple-choice questions. Here are the correct answers:
1. B 
2. D 
3. A 
4. A 
5. C
6. A
7. B 
8. A 
9. C 
10. D
11. B 
12. C 
13. D 
14. A 
15. D
16. C 
17. C 
18. B 
19. D 
20. A
Your program should store these correct answers in a list. The program should read the student’s answers 
for each of the 20 questions from a text file and store the answers in another list. (Create your own text file 
to test the application.) After the student’s answers have been read from the file, the program should display a 
message indicating whether the student passed or failed the exam. (A student must correctly answer 15 of the 20 
questions to pass the exam.) It should then display the total number of correctly answered questions, the total 
number of incorrectly answered questions, and a list showing the question numbers of the incorrectly answered questions.
"""

# main function to start the program
def main():

	# do your work in try suites and except clauses
	try:
		# initialize variables to hold numbers of correct and wrong answers
		NUMBER_OF_CORRECT_ANSWERS = 0
		NUMBER_OF_WRONG_ANSWERS = 0

		# initialize a list variable to hold the incorrectly answered questions
		incorrectly_answered_questions = []

		# NOTE: first creat a text file with students scores and we do that by getting the input from the user
		file_out = open('students_scores.txt', 'w')

		# get user input for the multiple choice in a loop that runs 20 times
		print("Please enter you answers as 'A', 'B', 'C', or 'D'.")
		for num in range(1, 21):
			print("Enter your naswer for question #", num, end='')
			answer = input(": ")
			file_out.write(answer + '\n')

		# close the file
		file_out.close()

		# store the correct answers in a list called correct_answers_list
		correct_answers_list = ['B', 'D', 'A', 'A', 'C', 'A', 'B', 'A', 'C', 'D', 'B', 'C', 'D', 'A', 'D', 'C', 'C', 'B', 'D', 'A']

		# initialize student answer list variable
		students_answers_list = []

		# read the students answer from the file and store them in a list
		# open the file for read
		file_in = open('students_scores.txt', 'r')
		for line in file_in:
			answer = line
			# strip and remove the new line character from the end of the line
			answer = answer.rstrip('\n')
			# append the lines read from the file into the list of students answers
			students_answers_list.append(answer)

		# match the student's answer with the correct answer and count the correct, wrong answers
		for num in range(20):
			# check if the items of the two list match or not
			if (correct_answers_list[num] == students_answers_list[num]):
				# if the items match increment the NUMBER_OF_CORRECT_ANSWERS
				NUMBER_OF_CORRECT_ANSWERS += 1
			else:
				# if the items don't match increment the NUMBER_OF_WRONG_ANSWERS
				NUMBER_OF_WRONG_ANSWERS += 1
				# append the index of the incorrect answer to the incorectly_answered_questions list
				incorrectly_answered_questions.append(num)



		# check if the student passes the test or not
		if (NUMBER_OF_CORRECT_ANSWERS >= 15):
			print("Yey! you have passed the exam and now you can drive.")
		else:
			print("Sorry! you are still not allowed to drive. please try again")

		# print number of correct answers
		print("You have answered ", NUMBER_OF_CORRECT_ANSWERS, "of the 20 questions correctly.")
		# print the number of incorrect answers
		print("You have answered" , NUMBER_OF_WRONG_ANSWERS, "of the 20 questions incorrectly.")
		# print the question numbers of the incorrect answers
		print("You have answered the following questions incorrectly: ")
		for num in incorrectly_answered_questions:
			# since num is the index number and starts from zero we add 1 to it to match the question number from 1 to 20
			print("question number", num + 1)


	# catch any exception raised in the try suite
	except Exception as err:
		print("An error occured. ", err)

		
# call the main function
main()


