class DoublyLinkedList:
	__data = None
	__next = None
	__prev = None
	__key = object()

	def __init__(self, DATA=None) -> None:
		'''
		# Params:
		DATA - Object or primitave type
		'''
		if DATA != None:
			self.__data = DATA

	def setPrev(self, prev, KEY) -> None:
		'''
		# This method is private
		'''
		assert(KEY == self.__key), \
			"This method is private, call DoublyLinkedList.append(nxt) instead."
		self.__prev = prev

	def insertBefore(self, first) -> None:
		pass

	def contains(self, element) -> bool:
		pass

	@property
	def llist(self):
		return self.__data

	@llist.setter
	def setData(self, DATA) -> None:
		self.__data = DATA

	@llist.setter
	def append(self, nxt) -> None:
		self.__next = nxt
		self.__next.setPrev(self, self.__key)

	@llist.getter
	def getNext(self):
		return self.__next

	@llist.getter
	def getPrev(self):
		return self.__prev
