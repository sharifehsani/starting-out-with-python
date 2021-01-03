"""
- Author: Sharif Ehsani
- Date: December 2020
- www.gitbuh.com/ehsanis

Programming Exercises
2. Capital Quiz
Write a program that creates a dictionary containing the canadian provinces and territories
as keys and their capitals as values. The program should then randomly quiz the user by displaying 
the name of a state and asking the user to enter that state’s capital. The program should keep 
a count of the number of correct and incorrect responses. 
"""

# import random
import random

# main function to start the progam
def main():

	# creat a dictionary with Canadaian provinces and territories with their capitals
	prov_and_ter = {"Alberta":"Edmonton", "Brithish Columbia":"Victoria", "Manitoba":"Winnipeg",
				"New Brunswick":"Fredericton", "Newfoundland and Labrador": "St.John's",
				"Northwest Territories":"Yelloknife", "Nova Scotia":"Halifax", "Nanavut":"Iqaluit",
				"Ontario":"Toronto", "Prince Edward Island":"Charlottetown", "Quebec":"Quebec",
				"Saskatchewan":"Regina", "Yukon":"Whitehorse"}

	# declare couter variables to hold correct and incoorect answer count
	score = 0
	correct = 0
	incorrect = 0
	
	# get user input and in a loop keep playing until the user wants to stop
	stop_the_game = 'n'
	while (stop_the_game == 'n'):

		# NOTE: Since python 3 does not support popitem() method we use the 
		# following expression to get the key-value randomly
		province, capital = random.choice(list(prov_and_ter.items()))
		# make it lower case to make the comparison easier
		capital = capital.lower()
		print("What is the capital of", province, end='')
		# get user input for capital
		capital_name = input(": ")
		# make the user input lowercase for comparison
		capital_name = capital_name.lower()

		# check if the answer is correct or not and hold the count as well
		if (capital_name == capital):
			correct += 1
		else:
			incorrect += 1

		# ask the user about continuing or stopping the game
		stop_the_game = input("Do you want to stop the game? (y/n): ")
		score += 1
	

	print("Your score is:", (correct / score) * 100)
	print("Number of correct answers:", correct)
	print("Number of incorrect answers:", incorrect)

# call the main function
main()
