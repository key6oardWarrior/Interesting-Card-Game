from Card import Card
from Stack import Stack
from Queue import Queue
from Player import Player
from os import system
from time import sleep

def isValueLegal(cardValue: str | int) -> bool:
	'''
	Check if card value is legal

	# Returns:
	True if the cardValue is in a standard deck of card else False
	'''
	if cardValue == "ace":
		return True
	if cardValue == "king":
		return True
	if cardValue == "queen":
		return True
	if cardValue == "jack":
		return True
	
	return ((cardValue.isnumeric()) and (int(cardValue) in range(2, 11)))

def isSuitLegal(suit: str) -> bool:
	if suit == "hearts":
		return True

	if suit == "spades":
		return True

	if suit == "clubs":
		return True

	if suit == "diamonds":
		return True

	return False

def getPlayerNum(order) -> int:
	return order.peak().player

def eliminatePlayer(deck: Stack, order: Queue, playerNum: int) -> None:
	print(f"Player {playerNum} you lose. Next round.")
	order.dequeue()
	order.moveBack()
	deck.clear()

	for ii in range(order.size):
		order.peak().setRemove = False
		order.moveBack()

def cardGame() -> None:
	deck = Stack()
	players = 0

	print("Enter a card and ensure that there are no repeat cards in the deck of 52. Each player is allowed to remove only the top card once per round. At the end of the round the player who goes next will now go last. At the end of each round the deck resets, so there are 52 available cards to choose from at the start of each round")

	while((players < 2) or (players > 53)):
		print("The game must have more than 1 player, but less than 53.")
		try:
			players = int(input("Enter number of players: "))
		except:
			print("Only enter numbers that are > 1, but < 54")

	order = Queue()
	for ii in range(1, players+1):
		order.enqueue(Player(ii))
	
	del players
	playerNum = getPlayerNum(order)

	while order.size > 1:
		playerNum = getPlayerNum(order)
		cardSuit = input(f"Player {playerNum} enter the card's suit (i.e hearts, spades, clubs, or diamonds) or enter \"remove\": ").lower().strip()

		if cardSuit == "remove":
			if order.peak().usedRemove == False:
				deck.pop()
				order.peak().setRemove = True
				order.moveBack()
				continue

			else:
				eliminatePlayer(deck, order, playerNum)
				continue

		elif isSuitLegal(cardSuit) == False:
			eliminatePlayer(deck, order, playerNum)
			continue 

		cardValue = input(f"Player {playerNum} enter the card's value (2 - 10 or Ace - King): ").lower().strip()

		if isValueLegal(cardValue) == False:
			eliminatePlayer(deck, order, playerNum)
			continue
	
		card = Card(cardSuit, cardValue)

		if deck.contains(card):
			eliminatePlayer(deck, order, playerNum)
			continue

		deck.push(card)

		if deck.size >= 52:
			if order.size > 2:
				order.moveBack()
				playerNum = getPlayerNum(order)
				order.dequeue()

				print(f"Player {playerNum} You lose. Next round")
				deck.clear()
			else:
				print(f"Player {playerNum} won")
				break

		order.moveBack()
		sleep(.5)
		system("clear")
	print(f"Player {getPlayerNum(order)} won")

if __name__ == "__main__":
	cardGame()
