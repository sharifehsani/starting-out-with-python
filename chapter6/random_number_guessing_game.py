import random 				# import random module from standard library
"""
- Author: Sharif Ehsani
- Date: July 2020
- https://github.com/sharifehsani

11. Random Number Guessing Game
Write a program that generates a random number in the range of 1 through 100 and asks the
user to guess what the number is. If the user’s guess is higher than the random number, the program
should display “Too high, try again.” If the user’s guess is lower than the random number,
the program should display “Too low, try again.” If the user guesses the number, the application
should congratulate the user and then generate a new random number so the game can
start over.
Optional Enhancement: Enhance the game so it keeps count of the number of guesses that the
user makes. When the user correctly guesses the random number, the program should display
the number of guesses.
"""

# function to start the program
def main():
	print()
	print("This random number gessing game program generates random number between 1 and 100, it asks the user to gues the number" +
		"\nif it is too high or too low, the program lets the user know and asks the user to try again")

	# a while loop to start the game over if the user wants
	start_over = 'y'
	while (start_over == 'y'):
		# generate a random number between 1 and 100
		rand = random.randint(1,100)
		print("The number to guess is an integer between 1 and 100")
		print("rand", rand)

		# get the user input
		user_input = int(input("Guess what is the number: "))

		# a while loop to make the program run until the guess is right
		while (user_input != rand):
			if (user_input < rand):
				print('Too low')
			else:
				print('Too high')
			user_input = int(input("try again: "))
			# end of inner loop

		# ask input to start over or not
		print('congratulations! you guessed it right')
		start_over = input("Want to start over? press 'y' for yes: ")

	# end of outter loop




# call the main function
main()
