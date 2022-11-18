
"""
- Author: Sharif Ehsani
- Date: September 2020
- https://github.com/sharifehsani

Checkpoint
9.15 Write a loop that asks the user “Do you want to repeat the program or quit?
(R/Q)”. The loop should repeat until the user has entered an R or Q (either
uppercase or lowercase).
"""

# main function to start the program
def main():


	# initialize a conditional variable to control the loop
	repeat = 't'

	# run the while loop until the user input equals 'r' or 'q'
	# the repat.upper() converts the input to uppercase before it tests the condition
	while ((repeat.upper() != "R") or (repeat.upper() != "Q")):
		repeat = input("Do you want to repeat the program or quit? ")



# call the main function

main()
