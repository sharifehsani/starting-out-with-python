
"""
- Author: Sharif Ehsani
- Date: December 2020
- www.gitbuh.com/ehsanis

Algorithm Workbench
3. Assume the variable dct references a dictionary. Write an if statement that determines
whether the key 'James' exists in the dictionary. If so, display the value that is associated
with that key. If the key is not in the dictionary, display a message indicating so.
"""

# main function to start the program
def main():

	# creat a dictionary with some key-values
	dct = {'sharif': '403', "james": '400'}

	# check if james is in dictonary
	if 'james' in dct:
		print(dct["james"])
	else:
		print("does not exits")

# call the main functin
main()