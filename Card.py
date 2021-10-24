class Card:
	__suit = ""
	__value = None

	def __init__(self, CARD: tuple) -> None:
		'''
		# Params:
		CARD - Index 0 is the suit. Index 1 is the value of the suit 
		'''
		self.__suit = CARD[0]
		self.__value = CARD[1]

	@property
	def card(self) -> dict:
		'''
		# Returns:
		The card's suit and value 
		'''
		return {self.__suit: self.__value}

	@card.setter
	def setCard(self, CARD: tuple) -> None:
		self.__suit = CARD[0]
		self.__value = CARD[1]
