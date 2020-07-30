"""
- Author: Sharif Ehsani
- Date: July 2020
- www.gitbuh.com/ehsanis

1. Bug Collector
A bug collector collects bugs every day for seven days. Write a program that keeps a running
total of the number of bugs collected during the seven days. The loop should ask for
the number of bugs collected for each day, and when the loop is finished, the program
should display the total number of bugs collected.
"""

# function to start the program
def main():
	print("This program keeps record of the bug collected during the week. ")
	# call the get_input()function
	get_input()

# function to get user input
def get_input():
	days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
	# running tool
	total_bug_collected = 0
	for day in range(7):
		bug = int(input("Please enter the number of bugs collected today: "))
		total_bug_collected = total_bug_collected + bug
		

	# display the total of bugs collected
	print("Total number of bugs collected: ", total_bug_collected)


#call the main function
main()
