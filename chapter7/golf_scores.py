"""
- Author: Sharif Ehsani
- Date: August 2020
- www.gitbuh.com/ehsanis

Programming Exercises
10. Golf Scores
The Springfork Amateur Golf Club has a tournament every weekend. The club president has asked you to write two programs:
1. A program that will read each player’s name and golf score as keyboard input, and then save these as records in a file named golf.txt. 
(Each record will have a field for the player’s name and a field for the player’s score.)
2. A program that reads the records from the golf.txt file and displays them.
"""

# function to start the program
def main():

	# ______________First part of the program_______________
	# open/create the file named golf.txt in a try suite
	try:
		file_out = open('golf.txt', 'w')

		# in a loop ask the user to enter the name and score of the player
		# creat a conditional variable for the loop
		more = 'y'
		while (more == 'y'):
			name = input("Player name: ")				# get player's name from the user
			score = float(input("Player score: "))		# get player's score from the user

			# write the fields to the file
			file_out.write(name + '\n')					# add the new line char at the end of each field
			file_out.write(str(score) + '\n')			# conver the floating point value to str and add new line to the end of the line

			# ask the user if s/he wants to continue
			more = input("Do you have more players to add? 'y' for yes and anything for no: ")

		# close the file
		file_out.close()
	except IOError:
		#print("An error occured trying to creat the file.")

	# value error
	except ValueError:
		print("None-floating point value entered.")

	# print the error type
	except Exception as err:
		print(err)

	# ______________Second part of the program_______________

	# open the file for read in a try suite
	print("Lets now read the file. ")
	try:
		file_in = open("golf.txt", 'r')

		# read the first line
		name_field = file_in.readline()

		# in a loop read all the contents of the file
		while (name_field != ''):
			# read the second line
			score_field = float(file_in.readline())

			# remove the new line char from the end of the name field
			name_field = name_field.rstrip('\n')

			# convert the scor from string to floating point value
			# score_field = float(score_field)

			# display the result
			print("Player's name: ", name_field)
			print("Player's score: ", score_field)

			# read the next line
			name_field = file_in.readline()

		# close the file
		file_in.close()


	# catch all the exceptions raised by the try suites
	# input or outut error
	except IOError:
		print("An error occured trying to read the file.")

	# value error
	except ValueError:
		print("None-computable value exist in the file")

	# print the error type
	except Exception as err:
		print(err)



# call the main function
main()






