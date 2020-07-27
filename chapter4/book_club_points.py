"""
- Author: Sharif Ehsani
- Date: June 2020
- www.gitbuh.com/ehsanis

7. Book Club Points
Serendipity Booksellers has a book club that awards points to its customers based on the
number of books purchased each month. The points are awarded as follows:
• If a customer purchases 0 books, he or she earns 0 points.
• If a customer purchases 1 book, he or she earns 5 points.
• If a customer purchases 2 books, he or she earns 15 points.
• If a customer purchases 3 books, he or she earns 30 points.
• If a customer purchases 4 or more books, he or she earns 60 points.
Write a program that asks the user to enter the number of books that he or she has purchased
this month and displays the number of points awarded.

"""
POINTS = 0
# function to start the program
def main():
	print()
	print("This proram calculates the numbe of points a customer accomulates during book purchses at Serendipity bookstor.")
	get_input()

# function to get user input
def get_input():
	number_of_books = int(input("Enter the number of books purchased: "))
	calculate_points(number_of_books)

# function to calcuate points
def calculate_points(number_of_books):
	if (number_of_books == 0):
		POINTS = 0
	elif (number_of_books == 1):
		POINTS = 5
	elif (number_of_books == 2):
		POINTS = 15
	elif (number_of_books == 3):
		POINTS = 30
	elif (number_of_books >= 4):
		POINTS = 60
	else:
		print("you have earned no points")

	print("You have earned ", POINTS, " points with your ", number_of_books, "book purchases.")

# call the main function
main()
