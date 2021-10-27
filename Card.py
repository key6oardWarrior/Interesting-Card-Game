class Card:
	__suit = ""
	__value = None

	def __init__(self, suit: str, value: int | str) -> None:
		'''
		# Params:
		suit - Card suit
		value - 2 - 10 or ace - king
		'''
		self.__suit = suit
		self.__value = value
