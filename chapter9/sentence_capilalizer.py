"""
- Author: Sharif Ehsani
- Date: November 2020
- www.gitbuh.com/ehsanis

8. Sentence Capitalizer
Write a program with a function that accepts a string as an argument and returns a copy
of the string with the first character of each sentence capitalized. For instance, if the argument
is “hello. my name is Joe. what is your name?” the function should return the string
“Hello. My name is Joe. What is your name?” The program should let the user enter a
string and then pass it to the function. The modified string should be displayed.
"""




# a function that capitalizes the sentence that recives a string as a parameters, capitalizes the first
# character of the each senctence and returns the value
def sentence_capitalizer(my_string):
	# split the text such that is seperated from period and space (gramatically correct sentenses)
	the_string = my_string.split('. ')
	# initialize variables
	new_string = ''
	my_string = ''
	# in a loop iterate through the indices of the list and get the first charachter of each sentenc
	# capitalize it and concatinate it back with the rest of the sentence
	for word in the_string:
		first_char_of_sentence = word[0]
		first_char_of_sentence = first_char_of_sentence.upper()
		new_string = first_char_of_sentence + word[1:] + '. ' 		# since the perios is removed at split add one
		
		my_string = my_string + new_string


	# remove the last period that is added at the end of each sentence. 
	my_string = my_string[0:-2]
	return my_string
		


# main function to start the program
def main():

	# creat a string by getting it from the user
	print("Please enter a text consisting of few sentences and I return the text back with the")
	print("first character of each sentence capitalized.", end="")
	my_string = input(": ")
	# call the sentence_capitalizer() function and pass the string as an argument and assign the returned value
	# to new_string variable
	new_string = sentence_capitalizer(my_string)

	# print the returned value
	print(new_string)




# call the main function
main()