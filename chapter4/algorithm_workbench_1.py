"""
- Author: Sharif Ehsani
- Date: June 2020
- www.gitbuh.com/ehsanis
- Write an if statement that assigns 20 to the variable y and assigns 40 to the variable z if the variable x is greater than 100.
"""
# function to start the program
def main():
	x = int(input("Enter a value for the variable x: "))
	if (x > 100):
		y = 20
		z = 40
		print("x = ", x,", " "y = ", y,", ", "z = ", z)
	else:
		print("You entered a value less than 100")


main()