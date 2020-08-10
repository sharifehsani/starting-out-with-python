"""
- Author: Sharif Ehsani
- Date: July 2020
- www.gitbuh.com/ehsanis

5. Kinetic Energy
In physics, an object that is in motion is said to have kinetic energy (KE). The following formula
can be used to determine a moving object’s kinetic energy:
KE = 1⁄2 mv^2
The variables in the formula are as follows: KE is the kinetic energy in joules, m is the
object’s mass in kilograms, and v is the object’s velocity in meters per second.
Write a function named kinetic_energy that accepts an object’s mass in kilograms and
velocity in meters per second as arguments. The function should return the amount of
kinetic energy that the object has. Write a program that asks the user to enter values for
mass and velocity, and then calls the kinetic_energy function to get the object’s kinetic
energy.
"""

# function to start the main function
def main():
	print()
	print("This program determines a moving object’s kinetic enerty.")
	print("In physics, an object that is in motion is said to have kinetic energy (KE).")

	# call get_input function
	object_mass, object_velocity = get_input()

	# once you get the user input call the kinetic_energy function and pass object_mass and object_velocity as
	# parameters to calculate the object's KE and assign the result to ke
	ke = kinetic_energy(object_mass, object_velocity)

	# print the result once you recieve it from kinetic_energy function
	print('The object with mass ', format(object_mass,'.2f'), 'kilograms '
		'and velocity of', format(object_velocity,'.2f'), 'meter/second  has kinetic energy of =', format(ke,'.2f'), 'joules.')


# function to get input and return the input to caller
def get_input():
	# get mass and veloicty
	mass = float(input("Enter ojbect's mass kilograms: "))
	velocity = float(input("Enter object’s velocity in meter per seconds: "))
	# return the input to the caller
	return mass, velocity
	# end of function



# function to calculate ke
def kinetic_energy(m, v):
	# use the KE formula to calculate KE
	kinetic_energy = 0.5 * m * (v ** 2)
	return kinetic_energy
	# end of function


# call the main function
main()