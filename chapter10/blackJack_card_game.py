"""
- Author: Sharif Ehsani
- Date: November 2020
- https://github.com/sharifehsani

In the Spotlight:
Using a Dictionary to Simulate a Deck of Cards
In some games involving poker cards, the cards are assigned numeric values. For example,
in the game of Blackjack, the cards are given the following numeric values:
• Numeric cards are assigned the value they have printed on them. For example, the
value of the 2 of spades is 2, and the value of the 5 of diamonds is 5.
• Jacks, queens, and kings are valued at 10.
• Aces are valued at either 1 or 11, depending on the player’s choice.
In this section we look at a program that uses a dictionary to simulate a standard deck of
poker cards, where the cards are assigned numeric values similar to those used in Blackjack.
(In the program, we assign the value 1 to all aces.) The key-value pairs use the name of the
card as the key and the card’s numeric value as the value. For example, the key-value pair
for the queen of hearts is
'Queen of Hearts':10
And the key-value pair for the 8 of diamonds is
'8 of Diamonds':8
The program prompts the user for the number of cards to deal, and it randomly deals a
hand of that many cards from the deck. The names of the cards are displayed, as well as
the total numeric value of the hand. Program 10-1 shows the program code. The program
is divided into three functions: main, create_deck, and deal_cards. Rather than presenting
the entire program at once, let’s first examine the main function:
"""

# lets make the game in three functions
# function to creat deck of card
def creat_deck_of_cards():

	# declare a dictionary with all keys and values of the card
	deck = {"Ace of Heart":1, "2 of Heart":2, "3 of Heart":3, "4 of Heart":4, "5 of Heart":5, "6 of Heart":6,
		"7 of Heart":7, "8 of Heart":8, "9 of Heart":9, "10 of Heart":10, "Jack of Heart":10, "Queen of Heart":10,
		"King of Heart":10,

		"Ace of Spades":1, "2 of Spades":2, "3 of Spades":3, "4 of Spades":4, "5 of Spades":5, "6 of Spades":6,
		"7 of Spades":7, "8 of Spades":8, "9 of Spades":9, "10 of Spades":10, "Jack of Spades":10, "Queen of Spades":10,
		"King of Spades":10,

		"Ace of Clubs":1, "2 of Clubs":2, "3 of Clubs":3, "4 of Clubs":4, "5 of Clubs":5, "6 of Clubs":6,
		"7 of Clubs":7, "8 of Clubs":8, "9 of Clubs":9, "10 of Clubs":10, "Jack of Clubs":10, "Queen of Clubs":10,
		"King of Clubs":10,

		"Ace of Diamonds":1, "2 of Diamonds":2, "3 of Diamonds":3, "4 of Diamonds":4, "5 of Diamonds":5, "6 of Diamonds":6,
		"7 of Diamonds":7, "8 of Diamonds":8, "9 of Diamonds":9, "10 of Diamonds":10, "Jack of Diamonds":10, "Queen of Diamonds":10,
		"King of Diamonds":10}

	# return the dictonary
	return deck


# a function to deal the card
def deal_card():
	pass

# main function to start the program
def main():

	# NOTE: _____________________________________
	# 
	deck = creat_deck_of_cards()
	

# call the main function
main()

