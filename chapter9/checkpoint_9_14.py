"""
- Author: Sharif Ehsani
- Date: September 2020
- www.gitbuh.com/ehsanis

Checkpoint
9.14 What is the output of the following code?
ch = 'a'
ch2 = ch.upper()
print(ch, ch2)

"""

# main function to start the program
def main():

	# What is the output of the following code? a A
	# ch = 'a'
	# ch2= ch.upper()
	# print(ch, ch2)

	#in line 23 a string variable is that references the string 'a' is initialize
	ch = 'a'

	# in line 27 the string that is referenced by ch string variable is converted to upper case
	# and then assigned to string variable ch2
	ch2 = ch.upper()

	# in line 30 the string before and after conversion is printed
	print(ch, ch2)

# call the main function
main()
