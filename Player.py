class Player:
	__num = 0
	__usedRemove = False

	def __init__(self, num: int) -> None:
		self.__num = num

	@property
	def player(self) -> int:
		return self.__num

	@player.getter
	def usedRemove(self) -> bool:
		return self.__usedRemove

	@player.setter
	def setRemove(self, state: bool) -> None:
		self.__usedRemove = state