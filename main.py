from Card import Card
from Stack import Stack
from Queue import Queue

def switch(cardValue: str) -> bool:
	if cardValue == "ace":
		return True
	if cardValue == "king":
		return True
	if cardValue == "queen":
		return True
	if cardValue == "jack":
		return True
	
	if((cardValue.isnumeric()) and (int(cardValue) in range(2, 11))):
		return True

	return False

def getPlayerKey(order) -> int:
	return list(order.peak().keys())[0]

def eliminatePlayer(deck: Stack, order: Queue, playerKey: int) -> None:
	print(f"Player {playerKey} you lose. Next round.")
	order.dequeue()
	order.moveBack()
	deck.clear()
	players = []
	while order.size != 0:
		players.append(order.peak())
		order.dequeue()
	
	for ii in range(len(players)):
		KEY = list(players[ii].keys())[0]
		players[ii][KEY] = 1

	for ii in players:
		order.enqueue(ii)

def cardGame() -> None:
	deck = Stack()
	cards = {
		"hearts": [],
		"spades": [],
		"clubs": [],
		"diamonds": []
	}
	KEYS = list(cards.keys())
	players = 0

	print("Enter a card and ensure that there are no repeat cards in the deck of 52. Each player is allowed to remove only the top card once per round. At the end of the round the player who goes next will now go last. At the end of each round the deck resets, so there are 52 available cards to choose from at the start of each round")

	while((players < 2) or (players > 52)):
		print("The game must have more than 1 player, but less than 52.")
		try:
			players = int(input("Enter number of players: "))
		except:
			print("Only enter numbers that are > 1")

	order = Queue()
	for ii in range(1, players+1):
		order.enqueue({ii: 1})
	
	del players

	while True:
		playerKey = getPlayerKey(order)
		if order.size < 2:
			print(f"Player {playerKey} won")
			break
		cardSuit = input(f"Player {playerKey} enter the card's suit {KEYS} or enter \"remove\": ").lower().strip()

		if cardSuit == "remove":
			if order.peak()[playerKey] == 1:
				deck.pop()
				order.peak()[playerKey] = 0
				order.moveBack()
				continue

			else:
				print(f"Player {playerKey} you lose. Next round")
				order.dequeue()
				order.moveBack()
				continue

		elif (cardSuit in KEYS) == False:
			eliminatePlayer(deck, order, playerKey)
			continue 

		cardValue = input(f"Player {playerKey} enter the card's value (2 - 10 or Ace - King): ").lower().strip()

		if switch(cardValue) == False:
			eliminatePlayer(deck, order, playerKey)
			continue
	
		card = Card((cardSuit, cardValue))

		if deck.contains(card):
			eliminatePlayer(deck, order, playerKey)
			continue

		deck.push(card)

		if deck.size >= 52:
			if order.size > 2:
				order.moveBack()
				playerKey = getPlayerKey(order)
				order.dequeue()

				print(f"Player {playerKey} You lose. Next round")
				deck.clear()
			else:
				print(f"Player {playerKey} won")
				break

		order.moveBack()

if __name__ == "__main__":
	cardGame()
