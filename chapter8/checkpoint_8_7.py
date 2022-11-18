"""
- Author: Sharif Ehsani
- Date: August 2020
- https://github.com/sharifehsani

Checkpoint
8.7 What will the following code display?
numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]
numbers3 = numbers1 + numbers2
print(numbers1) 
print(numbers2) 
print(numbers3)
"""


# main function to start the program
def main():

	numbers1 = [1, 2, 3]					# a list called numbers1 is initialized and 3 elements are assigned to it
	numbers2 = [10, 20, 30]					# a list called numbers2 is created and 3 elements are assigned to it
	numbers3 = numbers1 + numbers2			# two lists are concatinated
	print(numbers1) 						# prints the elements of the first list [1, 2, 3]
	print(numbers2) 						# prints the elments of the second list [ 10, 20, 30]
	print(numbers3)							# prints the elments of the two lists concatinated together [1, 2, 3, 10 ,20, 30]


# call the main function
main()
