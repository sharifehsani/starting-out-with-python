"""
- Author: Sharif Ehsani
- Date: July 2020
- www.gitbuh.com/ehsanis

4. Distance Traveled
The distance a vehicle travels can be calculated as follows:
distance = speed x time
For example, if a train travels 40 km per hour for three hours, the distance traveled is 120
km. Write a program that asks the user for the speed of a vehicle (in km per hour) and
the number of hours it has traveled. It should then use a loop to display the distance the
vehicle has traveled for each hour of that time period. Here is an example of the desired
output:
What is the speed of the vehicle in mph? 40
How many hours has it traveled? 3
Hour Distance Traveled
1 40
2 80
3 120
"""

# main function to start the program
def main():
	print()		# blanck line to seperate the program from the command line for readablity
	print('This program calculates the distance a vehicle travells per hour.')
	# call get_input()
	get_input()

# function to get user input
def get_input():

	# ask the user to enter the speed of a vehicle and the number of hours it travelled
	speed = float(input("Enter the speed of the vehicle in kilometers per hour: "))
	number_of_hours = int(input("Enter the number of hours travelled: "))

	# call the calculate_distance() function and pass speed and number_of_hours as parameter
	calculate_distance(speed, number_of_hours)

# function to calculate distance
def calculate_distance(speed, number_of_hours):
	distance = 0.0
	print()
	print("Hours \t \t \t\t\t", "Distance Travelled")
	print("----------------------------------------------------------")
	# creat a for loop to iterate for the number of hours
	for hours in range(1, number_of_hours + 1):
		distance = hours * speed
		
		print('in', hours, 'hour/s the vehicle travelled' + "\t\t",  distance, 'km')


# call the main function
main()