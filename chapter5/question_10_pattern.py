"""
- Author: Sharif Ehsani
- Date: July 2020
- www.gitbuh.com/ehsanis

10. Write a program that uses nested loops to draw this pattern:
##
# #
#  #
#	 #
#	  #
#		#
Programming Exercises 201
"""

# main function to start the program
def main():
	print()
	print("This program displays patter using nested loops.")
	hash_tag = '#'
	for row in range(6):
		print(hash_tag, end='')
		for col in range(row + 1):
			print(' ', end='')
		print(hash_tag)	
		print()

# call the main function
main()