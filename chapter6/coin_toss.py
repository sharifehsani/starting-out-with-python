
import random 			# import random madule from python standard library
"""
- Author: Sharif Ehsani
- Date: July 2020
- https://github.com/sharifehsani

In the Spotlight:
Using Random Numbers to Represent Other Values
Dr. Kimura was so happy with the dice rolling simulator that you wrote for him, he has
asked you to write one more program. He would like a program that he can use to simulate
ten coin tosses, one after the other. Each time the program simulates a coin toss, it
should randomly display either “Heads” or “Tails”.
You decide that you can simulate the tossing of a coin by randomly generating a number
in the range of 1 through 2. You will write an if statement that displays “Heads” if the
random number is 1, or “Tails” otherwise. Here is the pseudocode:
Repeat 10 times:
If a random number in the range of 1 through 2 equals 1 then:
Display ‘Heads’
Else:
Display ‘Tails’
"""

# main function to start the program
def main():
	print()
	print("This program simulates coin tosses for 10 times repeated.")

	# repeat the coin toss 10 times
	for num in range(10):
		rand_number = random.randint(1,2)
		if (rand_number == 1):
			print("Heads")
		else:
			print("Tails")



# call the main function
main()
