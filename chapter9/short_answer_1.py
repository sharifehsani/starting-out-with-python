"""
- Author: Sharif Ehsani
- Date: June 2020
- www.gitbuh.com/ehsanis

Short Answer
1. What does the following code display?
mystr = 'yes'
mystr += 'no'
mystr += 'yes'
print(mystr
"""
# main function to start the program
def main():

	# the statement in line 17 initializes a string variable that references to string 'yes'
	mystr = 'yes'

	# in line 20 string 'no' is concatinated with string that is referenced mystr
	mystr += 'no'

	# in lie 23 the same thing happens and concatinates string 'yes' to mstr
	mystr += 'yes'

	# the result of the print will be 'yesnoyes'
	print(mystr)
	
# call the main function
main()