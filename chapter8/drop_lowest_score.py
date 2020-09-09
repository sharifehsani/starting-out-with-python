"""
- Author: Sharif Ehsani
- Date: September 2020
- www.gitbuh.com/ehsanis

In the Spotlight:
Processing a List
Dr. LaClaire gives a series of exams during the semester in her chemistry class. At the end of the semester
she drops each student’s lowest test score before averaging the scores. She has asked you to design a program 
that will read a student’s test scores as input, and cal- culate the average with the lowest score dropped. 
Here is the algorithm that you developed:
Get the student’s test scores.
Calculate the total of the scores.
Find the lowest score.
Subtract the lowest score from the total. This gives the adjusted total.
Divide the adjusted total by 1 less than the number of test scores. This is the average. Display the average.
"""

# main function to start the program
def main():

	# ask the user how many test scores to add
	score_count = int(input("How many scores do you want to add?: "))

	# creat a list with the size of score_count
	score_list = [0] * score_count

	# in a loop get the list elments and populate the list
	for num in range(score_count):
		# get test scores from the user and populate the list
		print("Enter the score for test number ", num + 1, ": ", end='')
		score_list[num] = test_score = int(input())

	# call the total() function to calcualte total of the scores and pass the list as argument and assign
	# the result to total_of_scores variable
	total_of_scores = total(score_list)
	print("Total of scores ", total_of_scores)

	# call the lowest_score() function to get the adjusted score and pass the total_of_scores as argument
	# assign the result to lowest_score variable
	lowest_score = lowest_score_fun(score_list)
	print("The lowest score ", lowest_score)

	# calculate the adjuested total
	adjusted_total = total_of_scores - lowest_score
	print("Adjuest total ", adjusted_total)

	# calculate the average
	average = float(adjusted_total / (score_count - 1))

	# print the average
	print("The average score with the lowest score droped =", format(average, '.1f'))


# function to calculate the total and return the total
def total(list):
	# sum variable to accumulate the total
	sum = 0

	# in a loop add up all the elements and assign it to sum variable
	for num in range(len(list)):
		# add up the elements of the list
		sum += list[num]

	# return the sum of all the scores
	return sum

# function to find the lowest score and return the result
def lowest_score_fun(list):
	# find the lowest score using the min method
	min_score = min(list)

	# return the result
	return min_score

# call the main function
main()
