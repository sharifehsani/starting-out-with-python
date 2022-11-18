"""
- Author: Sharif Ehsani
- Date: June 2020
- https://github.com/sharifehsani

11. Time Calculator
Write a program that asks the user to enter a number of seconds, and works as follows:
• There are 60 seconds in a minute. If the number of seconds entered by the user is greater
than or equal to 60, the program should display the number of minutes in that many
seconds.
• There are 3,600 seconds in an hour. If the number of seconds entered by the user is
greater than or equal to 3,600, the program should display the number of hours in that
many seconds.
• There are 86,400 seconds in a day. If the number of seconds entered by the user is greater
than or equal to 86,400, the program should display the number of days in that many
seconds.
"""
SECONDS = 0
MINUTES = 60
HOUR = 3600
DAY = 86400
REMAINING_TIME = 0
REMAINING_SECONDS = 0

# function to start the program
def main():
	print()
	print("This programs calculates and converts seconds to minutes, hours and day.")
	get_input()

# function to get user input
def get_input():
	number_of_seconds = int(input("Enter the number of seconds: "))
	calculate_time(number_of_seconds)


# function to calculate times
def calculate_time(number_of_seconds):
	if (number_of_seconds < 60):
		SECONDS = number_of_seconds
		print(number_of_seconds, 'Seconds, equals:', format(SECONDS,'.0f'), 'Seconds.')
		print("seconds = ", SECONDS)
	elif (number_of_seconds >= 60 and number_of_seconds < 3600):
		MINUTES = number_of_seconds // 60
		SECONDS = number_of_seconds % 60
		print(number_of_seconds, 'Seconds, equals:', format(MINUTES,'.0f'), 'Minutes and', format(SECONDS,'.0f'), 'Seconds.')
		print("minutes = ", format(MINUTES,'.0f'))
		print("seconds = ", format(SECONDS, '.0f'))
	elif (number_of_seconds >= 3600 and number_of_seconds < 86400):
		HOUR = number_of_seconds // 3600
		REMAINING_SECONDS = number_of_seconds % 3600
		MINUTES = REMAINING_SECONDS // 60
		SECONDS = REMAINING_SECONDS % 60
		print(number_of_seconds, 'Seconds, equals:', format(HOUR, '.0f'), 'Hour/s,', format(MINUTES,'.0f'), 'Minutes and', format(SECONDS,'.0f'), 'Seconds.')
		print("Hour: ", format(HOUR, '.0f'))
		print("Minutes: ", format(MINUTES, '.0f'))
		print("Seconds: ", format(SECONDS, '.0f'))
	else:
		DAY = number_of_seconds // 86400
		REMAINING_SECONDS = number_of_seconds % 86400
		HOUR = REMAINING_SECONDS // 3600
		REMAINING_TIME = REMAINING_SECONDS % 3600
		MINUTES = REMAINING_TIME / 60
		SECONDS = REMAINING_TIME % 60
		print(number_of_seconds, 'Seconds, equals:', format(DAY, '.0f'), 'Day/s,', format(HOUR, '.0f'), 'Hour/s,', format(MINUTES,'.0f'), 'Minutes and', format(SECONDS,'.0f'), 'Seconds.')
		print("Day: ", format(DAY, '.0f'))
		print("Hour: ", format(HOUR, '.0f'))
		print("Minutes: ", format(MINUTES, '.0f'))
		print("Seconds: ", format(SECONDS, '.0f'))




# call the main function
main()
