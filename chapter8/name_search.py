"""
- Author: Sharif Ehsani
- Date: September 2020
- www.gitbuh.com/ehsanis

Programming Exercises
7. Name Search
If you have downloaded the source code from this book’s companion Web site, you will find the 
following files in the Chapter 08 folder:
• GirlNames.txt—This file contains a list of the 200 most popular names given to girls born in 
  the United States from the year 2000 through 2009.
• BoyNames.txt—This file contains a list of the 200 most popular names given to boys born in the 
  United States from the year 2000 through 2009.
Write a program that reads the contents of the two files into two separate lists. The user should be able to enter a 
boy’s name, a girl’s name, or both, and the application will display messages indicating whether the names were among the most popular.
(You can access the book’s companion Web site at www.pearsonhighered.com/gaddis.)
"""

# main funcion to start the program
def main():

	# NOTE. the source for name of the boys and girls name is: https://www.mother.ly/news/top-baby-names-of-the-decade
	# not gaddis webstie.

	# do your works in try and except handlers
	try:
		# initialize the two lists variables with 200 elements

		boys_names_list = []
		girls_names_list =[]

		# open the files in 'r' access mode
		boy_names_file = open('BoyNames.txt', 'r')
		girl_names_file = open('GirlNames.txt', 'r')

		# read the contents of the file that contains boyes names and store them in the boys names lists
		for line in boy_names_file:
			# strip the new line character from the end of the lines
			name = line.rstrip('\n')
			boys_names_list.append(name)

		# close the file that contains boy names
		boy_names_file.close()

		# read the contents of the file that contains girls names and store them in the girls names lists
		for line in girl_names_file:
			# strip the new line character from the end of the lines
			name = line.rstrip('\n')
			girls_names_list.append(name)

		# clsoe the file that contains girl names
		girl_names_file.close()


		# get the user input to search in the lists of 200 popular boys or girls names
		print("Type a boy or a girl name to search if that name is among the the top 200 popular boys or girls names in America.")
		name = input("Please enter the first letter in capital letters: ")
		# check if the name entered by the user is in boys list or girls list
		if (name in boys_names_list or name in girls_names_list):
			print(name, "is among the top 200 popular names of decade in America.")
		else:
			print(name, "is not among top 200 popular names of decade in America.")

	# catch any exception raised in the try suite
	except Exception as err:
		print(err)

# call the main function
main()


