import random		# import random module from the python standard library
"""
- Author: Sharif Ehsani
- Date: July 2020
- www.gitbuh.com/ehsanis

12. Rock, Paper, Scissors Game
Write a program that lets the user play the game of Rock, Paper, Scissors against the computer.
The program should work as follows.
1. When the program begins, a random number in the range of 1 through 3 is generated.
If the number is 1, then the computer has chosen rock. If the number is 2, then the computer
has chosen paper. If the number is 3, then the computer has chosen scissors.
(Don’t display the computer’s choice yet.)
2. The user enters his or her choice of “rock”, “paper”, or “scissors” at the keyboard.
3. The computer’s choice is displayed.
4. A winner is selected according to the following rules:
• If one player chooses rock and the other player chooses scissors, then rock wins.
(The rock smashes the scissors.)
• If one player chooses scissors and the other player chooses paper, then scissors wins.
(Scissors cuts paper.)
• If one player chooses paper and the other player chooses rock, then paper wins.
(Paper wraps rock.)
• If both players make the same choice, the game must be played again to determine
the winner.
"""

# function to start the program
def main():
	print()
	print("rock, paper, scissors game!.")
	# variables
	computer_wins = False
	user_wins = False
	computer_choice = ''


	# generate random number between 1 and 3
	rand = random.randint(1,3)

	# make random number th same as what user enters as in input in this case (rock, paper, scissors)
	if (rand == 1):
		computer_choice = 'rock'
	elif (rand == 2):
		computer_choice = 'paper'
	else:
		computer_choice = 'scissors'

	

	# get user input
	user_choice = input("Enter your choice: 'rock, paper or scissors': ")

	# once we get the user choice, we display computer choice
	print("computer's choice: ", computer_choice)
	
	# determine who wins if user's choice is not as computer's choice
	if (computer_choice != user_choice):

		if (computer_choice == 'rock' and user_choice == 'scissors'):
			computer_wins = True
			
		elif(computer_choice == 'scissors' and user_choice == 'rock'):
			user_wins = True
			
		elif (computer_choice == 'scissors' and user_choice == 'paper'):
			computer_wins = True
			
		elif (computer_choice == 'paper' and user_choice == 'scissors'):
			user_wins = True
			
		elif (computer_choice == 'paper' and user_choice == 'rock'):
			computer_wins = True
			
		elif (computer_choice == 'scissors' and user_choice == 'paper'):
			user_wins = True

	# if user chooses the same as computer get in the a loop and try again untill the choice is different
	else:
		# use the while loop to determine the winner
		while (computer_choice == user_choice):
			print("Same choice.")
			print("Try again. ")

			# generate the random number again
			rand = random.randint(1,3)

			 # make random number the same as what user enters as in input in this case (rock, paper, scissors)
			if (rand == 1):
				computer_choice = 'rock'
			elif (rand == 2):
				computer_choice = 'paper'
			else:
				computer_choice = 'scissors'

			# get the user input again
			user_choice = input("Enter your choice: 'rock, paper or scissors': ")

			# print the computer's choice again
			print("Conputer's choic: ", computer_choice)

			# determine the winner
			if (computer_choice == 'rock' and user_choice == 'scissors'):
				computer_wins = True
				
			elif(computer_choice == 'scissors' and user_choice == 'rock'):
				user_wins = True
				
			elif (computer_choice == 'scissors' and user_choice == 'paper'):
				computer_wins = True
				
			elif (computer_choice == 'paper' and user_choice == 'scissors'):
				user_wins = True
				
			elif (computer_choice == 'paper' and user_choice == 'rock'):
				computer_wins = True
				
			elif (computer_choice == 'scissors' and user_choice == 'paper'):
				user_wins = True
				
		# end of the loop

			

		
	
	# print the result	
	if (computer_wins == True):
		print("sorry you lost!")
	else:
		print("Yey! you won.")
	

# call the main function
main()