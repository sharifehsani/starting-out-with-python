"""
- Author: Sharif Ehsani
- Date: December 2020
- https://github.com/sharifehsani


In the Spotlight:
Set Operations
In this section you will look at Program 10-3, which demonstrates various set operations.
The program creates two sets: one that holds the names of students on the baseball team
and another that holds the names of students on the basketball team. The program then
performs the following operations:
• It finds the intersection of the sets to display the names of students who play both
sports.
• It finds the union of the sets to display the names of students who play either sport.
• It finds the difference of the baseball and basketball sets to display the names of students
who play baseball but not basketball.
• It finds the difference of the basketball and baseball (basketball – baseball) sets to display
the names of students who play basketball but not baseball. It also finds the difference
of the baseball and basketball (baseball – basketball) sets to display the names
of students who play baseball but not basketball.
• It finds the symmetric difference of the basketball and baseball sets to display the
names of students who play one sport but not both.
"""

# function to add and create baseball team
def baseball_team_method(baseball_team):

	# declare a counter variable
	print()
	print("First enter the names of students for baseball team.")
	more = 'y'
	while (more == 'y'):
		
		# get the user to input the name
		name = input("Enter the name of student in the baseball team: ")
		# check if the name alaready exist because sets can't have duplicate elements
		# if name already in the set get another name
		if (name in baseball_team):
			print(name, "already exist in the set and sets can't have duplicate elements.")
			name = input("Enter a different name: ")
			baseball_team.add(name)

		# if name does not exist add it to the set
		else:
			baseball_team.add(name)

		# ask the user if s/he wants to add more
		more = input("Do you want to add more? 'y' = yes, 'n' = no: ")

	# return the set
	return baseball_team

# function to populate basketball team
def basketball_team_method(basketball_team):
	# do the same as above and get students names for basketbal team
	print()
	print("Now enter the names of students for basketbal team.")
	add_more = 'y'
	while (add_more == 'y'):
		
		# get the user to input the name
		name = input("Enter the name of student in the baseball_team team: ")
		# check if the name alaready exist because sets can't have duplicate elements
		# if name already in the set get another name
		if (name in basketball_team):
			print(name, "already exist in the set and sets can't have duplicate elements.")
			name = input("Enter a different name: ")
			basketball_team.add(name)

		# if name does not exist add it to the set
		else:
			basketball_team.add(name)

		# ask the user if s/he wants to add more
		add_more = input("Do you want to add more? 'y' = yes, 'n' = no: ")
	# return the set
	return basketball_team

# function to find the intersection of the sets to display the names of students who play both sport
def intersection_method(baseball, basketball):

	# take the intersection of both sets
	intersection_set = baseball.intersection(basketball)
	#print the result
	print()
	print("The follwoing students play in both teams:")
	for name in intersection_set:
		print(name, end=', ')

# function to finds the union of the sets to display the names of students who play either sport
def union_method(baseball, basketball):
	# take the union of both sets
	union = baseball.union(basketball)
	#print the result
	print()
	print("The follwoing students play in either baseball or basketball teams:")
	for name in union:
		print(name, end=', ')


# function to finds the difference of the baseball and basketball sets to display the names of students
# who play baseball but not basketball.
def difference_method(baseball, basketball):
	# take the difference baseball - basketball
	diff_base = baseball.difference(basketball)

	# dsiplay the result
	print()
	print("The follwoing students play in baseball team but not in basketball team:")
	for name in diff_base:
		print(name, end=', ')

	# take the differnce (basketball - baseball)
	diff_basket = basketball.difference(baseball)

	# dsiplay the result
	print()
	print("The follwoing students play in basketball team but not in baseball team:")
	for name in diff_basket:
		print(name, end=', ')

# function to finds the symmetric difference of the basketball and baseball sets to display the
# names of students who play one sport but not both
def sym_dif(baseball, basketball):
	# take the symetric difference of the two sets
	sym = baseball.symmetric_difference(basketball)

	# dsiplay the result
	print()
	print("The follwoing students play only in one team:")
	for name in sym:
		print(name, end=', ')



# main function to start the program
def main():

	# declare two empty sets and get the user to populate the set
	baseball_team = set()
	basketball_team = set()

	# call bothe the function to creat the sets
	baseball = baseball_team_method(baseball_team)
	basketball = basketball_team_method(basketball_team)

	# call the intersection method to take the intersection of the sets
	intersection_method(baseball, basketball)

	# call the union_method to take the union of both sets
	union_method(baseball, basketball)

	# call the difference method to take the difference of both sets
	difference_method(baseball, basketball)

	# call the sym_dif method to take the symetric differnce of both sets
	sym_dif(baseball, basketball)
	

# call the main function
main()
