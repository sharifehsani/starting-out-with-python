"""
- Author: Sharif Ehsani
- Date: December 2020
- https://github.com/sharifehsani

Programming Exercises
7. World Series Winners
In this chapter’s source code folder (available on the book’s companion Web site at www.
pearsonhighered.com/gaddis), you will find a text file named WorldSeriesWinners.txt.
This file contains a chronological list of the World Series’ winning teams from 1903
through 2009. The first line in the file is the name of the team that won in 1903, and the
last line is the name of the team that won in 2009. (Note that the World Series was not
played in 1904 or 1994. There are entries in the file indicating this.)
Write a program that reads this file and creates a dictionary in which the keys are the names
of the teams and each key’s associated value is the number of times the team has won the
World Series. The program should also create a dictionary in which the keys are the years
and each key’s associated value is the name of the team that won that year.
The program should prompt the user for a year in the range of 1903 through 2009. It
should then display the name of the team that won the World Series that year and the number
of times that team has won the World Series.
"""

# function to creat dictionary year as key and team as value
def year_team(my_list, list_two, year_team_dic):
	
	# iterate throu the list and and get each element and assign every other element to
	# the dictinary as key and value pair
	# run the loop lenght of list times
	# use counter to assign as the list index through the loop
	count = 0
	
	for i in range(len(my_list)-1):
		# to eleminate the index out of range error, set a condiont to run no more that the length of the list
		while count <= len(my_list) - 1:		
			val = my_list[count]
			key = my_list[count + 1]
			list_two.append(val)
			# looking at the list team comes first so in the first dictionary we use year as key and team as value
			year_team_dic[key] = val
	
			# incremenet counter by 2 to go to the 3rd element every time
			count += 2
	# display the dictoinary
	print()
	print("World Series Winners:")
	print("Year ---> Team")
	print("__________________________________")
	for key in year_team_dic:
		if (year_team_dic[key] == ''):
			print(key, "--->", 'WORLD SERIES WAS NOT PLAYED')
		else:
			print(key,"--->", year_team_dic[key])
	print("---End of the list.---")
	# return to caller for other calculations
	return list_two
	return year_team_dic


# function to creat dictionary with the name of the team as a key and number of time it won as value
def multiple(list_two, multiple_dic):
	
	# declare a ditionary variable
	
	
	# iterate through the loop and count the number of time a team appeared in the list
	# and count the number of wins and assign to multipl_dic dictionary.
	count = 0
	for elem in list_two:
		count = list_two.count(elem)
		multiple_dic[elem] = count

	# display the result
	print()
	print("Number of times a team has won:")
	print("Team ---> Number of wins")
	print("_________________________________")
	for key in multiple_dic:
		if (key != ''):				# check for the year 1904 and 1994 that there was no game.
			print(key,"--->", multiple_dic[key])
	print("---End of the list.---")
	# return the dictonary to the caller for other calculations
	return multiple_dic

# functoin to get user input for the year and give the winner team as a result and the number of time the team won
def find_the_winner(year_team_dic, multiple_dic):
	# get user input
	print()
	print("Enter a year between 1903 and 2011 to find out who wone that year")
	keep_searching = 'y'
	while (keep_searching == 'y'):
		year = input("Enter a year: ")
		# get the value for year and check if the year exist
		team = year_team_dic.get(year)
		if team == '':
			print("Game was not played in", year)
		else:
			print(team, 'won in', year)

			# match the team with the team in multipl_dic if found get the value for it and display
			for key in multiple_dic:
				if (team == key):				# check for the year 1904 and 1994 that there was no game.
					print(team, 'has won', multiple_dic[key], 'times')
		# ask the user if s/he wants to continue	
		keep_searching = input("Want to search more? 'y/n': ")

# main function to start the program
def main():

	# declare dictonary variables
	year_team_dic = {}
	multiple_dic = {}
	# declare a list variable
	my_list = []
	list_two = []
	# open the file
	file_in = open("world_series_winners.txt", 'r')

	# iterate through the file and put each word and pupulate the list with the words
	for line in file_in:
		line = line.strip()
		my_list.append(line)

	#close the file
	file_in.close()
	
	# call the year_team() function and pass  my_list as argument
	year_team(my_list, list_two, year_team_dic)
	

	# call the team_year() function and pass my_list as argument
	multiple(list_two, multiple_dic)

	# call the find_the_winner function
	find_the_winner(year_team_dic, multiple_dic)

	
	
# call the main function
main()
