"""
- Author: Sharif Ehsani
- Date: July 2020
- www.gitbuh.com/ehsanis

4. Falling Distance
The following formula can be used to determine the distance an object falls due to gravity
in a specific time period, starting from rest:
d = 1⁄2 gt2
The variables in the formula are as follows: d is the distance in meters, g is 9.8, and t is the
amount of time in seconds, that the object has been falling.
Write a function named falling_distance that accepts an object’s falling time in seconds
as an argument. The function should return the distance in meters that the object has fallen
during that time interval. Write a program that calls the function in a loop that passes the
values 1 through 10 as arguments and displays the return value.
"""

# function to start the program
def main():
	print()
	print("This program calculates the distance an object falls due to gravity in seconds.")

	# the loop to call the falling_distance() 10 times and passes 1 to 10 as argument 
	for time in range(1,11):
		distance = falling_distance(time)
		print("in ", time, " seconds ", "the object falls ", format(distance, '.2f'), "meters.")



def falling_distance(time_in_secs):
	# t^2 
	t_squared = float(time_in_secs ** 2)

	# calculate the distance an object falls
	d = ((1/2) * (9.8 * t_squared))

	# return the distance to the caller
	return d


# call the main function
main()