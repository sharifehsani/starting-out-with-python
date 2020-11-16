"""
- Author: Sharif Ehsani
- Date: October 2020
- www.gitbuh.com/ehsanis

6. Driver’s License Exam
The local driver’s license office has asked you to create an application that grades the written
portion of the driver’s license exam. The exam has 20 multiple-choice questions. Here
are the correct answers:
1. B 	6. A 	11. B 	16. C
2. D 	7. B 	12. C 	17. C
3. A 	8. A 	13. D 	18. B
4. A 	9. C 	14. A 	19. D
5. C 	10. D 	15. D 	20. A
Your program should store these correct answers in a list. The program should read the
student’s answers for each of the 20 questions from a text file and store the answers in
another list. (Create your own text file to test the application.) After the student’s answers
have been read from the file, the program should display a message indicating whether the
student passed or failed the exam. (A student must correctly answer 15 of the 20 questions
to pass the exam.) It should then display the total number of correctly answered questions,
the total number of incorrectly answered questions, and a list showing the question numbers
of the incorrectly answered questions.

"""

# main function to start the program
def main():

	# lets creat an actual 10 question multiple-choice-questions on driving
	# and do an actual test with the user input and store the result in a file and then 
	# read the results from the file and match the answers

	# initialize a list variable and store the correct answers in it
	correct_answers = ["A", "B", "A", "C", "A", "D", "D", "B", "D", "A",]

	# first write the correct answers in a file
	# open a writeable text file
	file_out = open("correct_answer.txt", 'w')

	# write the correct answers list to the file
	for num in range(len(correct_answers)):
		file_out.write(correct_answers[num] + '\n')


	# close the file
	file_out.close()


	# question 1
	print("There are 10 questions in the test")
	print("Driving test. Please enter your answer as: a, b, c d and press enter\n")
	print("1. When leaving a highway, you should use _________ to slow down.\n")
	print("A) an Acceleration lane") # correct
	print("B) a deceleration lane")
	print("C) a weave zone")
	print("D) an express lane")
	one = input("Your answer: ")
	one = one.upper()
	print()

	# question 2
	print("2. To turn right from a two-way road onto another two-way road, what should you do?\n")
	print("A) Turn into the left lane.")
	print("B) Stay centred in your turning lane.")  # correct
	print("C) Swing wide to the left before turning.")
	print("D) Do all of the above.\n")
	two = input("Your answer: ")
	two = two.upper()
	print()


	# question 3
	print("3. Properly positioned head restraints can greatly reduce\n")
	print("A) the risk of whiplash injuries.") # correct
	print("B) speed while driving.")
	print("C) collisions on railway crossings.")
	print("D) the risk of being thrown from the vehicle.\n")
	three = input("Your answer: ")
	three = three.upper()
	print()

	# question 
	print("4. When leaving a roundabout or traffic circle, you should\n")
	print("A) proceed without signallin.") 
	print("B) sound your horn")
	print("C) signal right.") # correct
	print("D) signal left.\n")
	four = input("Your answer: ")
	four = four.upper()
	print()



	# question 
	print("5 ______ parking is most often used in parking lots. \n")
	print("A) Angle.) ") # correct
	print("B) Parallel) ")
	print("C) Hill.")
	print("D) None of te above\n")
	five = input("Your answer: ")
	five = five.upper()
	print()

	# question 
	print("6. You should not follow cyclists closely because\n")
	print("A) they should be treated like pedestrians.")
	print("B) they always wish to compete with motor vehicles.")
	print("C) they may stop anywhere in the lane.")
	print("D) they lack brake light.\n")  # correct
	six = input("Your answer: ")
	six = six.upper()
	print()

	# question 
	print("7. What is the maximum allowable blood alcohol concentration (BAC) for a GDL driver?\n")
	print("A) 0.01%") 
	print("B) 0.05%")
	print("C) 0.08%")
	print("D) Zero\n")# correct
	seven = input("Your answer: ")
	seven = seven.upper()
	print()

	# question 
	print("8. If someone is passing you on a two-lane highway, you should\n")
	print("A) move slightly to the left side of your lane.")
	print("B) move slightly to the right side of your lane") # correct
	print("C) move quickly to the left side of your lane.")
	print("D) stop immideately\n")
	eight = input("Your answer: ")
	eight = eight.upper()
	print()


	# question 
	print("9. The holder of a Class 6 operator's licence may operate which of the following vehicles?\n")
	print("A) a bus.")
	print("B) a tractor.")
	print("C) an ambulance.")
	print("D) a motorcycle.\n")# correct
	nine = input("Your answer: ") 
	nine = nine.upper()
	print()


	# question 
	print("10. If you get a flat tire while driving, you should\n")
	print("A) hold the steering wheel with a firm grip.") # correct
	print("B) brake to stop.")
	print("C) depresss the gas pedal to speed up.")
	print("D) turn off your hazard lights.\n")
	ten = input("Your answer: ") 
	ten = ten.upper()
	print()

	user_answers_list = [one, two, three, four, five, six, seven, eight, nine, ten]
	

	# open the correct answer file that was previously created
	file_in = open("correct_answer.txt", 'r')

	# read each answer and store them in a list call true_answers
	# initialize a list variable to hold the answers
	true_answers = []

	# in a loop read each line
	for line in file_in:
		a = line
		a = a.rstrip('\n')		# strip the new line character from the end of the line
		# write each line into the true_answers list
		true_answers.append(a)
	# close the file
	file_in.close()


	# in a seperate loop compare the answers
	count_true = 0			# counter to hold the number of corrcet ansers
	count_false = 0			# counter to hold the count of false answers
	incorrect_answers_list = []			# a list to hold the question number of incorrectly answered questions
	for num in range(len(correct_answers)):
		# each answer read from true_answers list is assigned to t_answer variable
		t_answer = true_answers[num]
		# each answer read from user_answers list is assigned to u_answer variable
		u_answer = user_answers_list[num]
		# copare the two answers
		if (u_answer == t_answer):
			# increment the counter if answer matches
			count_true = count_true + 1

		else:
			# increment counter if the answer does not match
			count_false += 1
			# write the incorrect answer's question number to the incorrect_answer_list list
			incorrect_answers_list.append(num)

	# check how many answers are correct
	if (count_true >= 7):
		# if 7 or more answers are correct print you passed
		print("You passed!")

	else:
		# if 4 or morse answers are false print you did not pass
		print("Sorry you did not pass. Try again")
		print("")

	# print the results
	print("Total number of correct answers: ", count_true)
	print("Total number of incorrect answers: ", count_false)
	print("the question numbers of the incorrectly answered questions: ", end='')
	for num in incorrect_answers_list:
		print(num + 1, end=',')



# call the main function
main()