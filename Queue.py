from DoublyLinkedList import DoublyLinkedList

class Queue(DoublyLinkedList):
	__queue = None
	__last = None
	__size = 0

	def __init__(self, first=None) -> None:
		if first != None:
			element = DoublyLinkedList(first)
			self.__queue = element
			self.__last = element
			self.__size = 1

	def peak(self):
		'''
		# Returns:
		The top of the Queue
		'''
		return (self.__queue.llist) if self.__size > 0 else None

	def enqueue(self, element) -> None:
		'''
		Place an element to the back of the Queue.

		# Params:
		element - The element to be placed in a container. The container will be placed
		at the back of the Queue.
		'''
		elem = DoublyLinkedList(element)

		if self.__size == 0:
			self.__queue = elem
			self.__last = elem

		else:
			self.__last.append = elem
			self.__last = self.__last.getNext

		self.__size += 1

	def __enqueue(self, element: DoublyLinkedList) -> None:
		'''
		Place an element to the back of the Queue.

		# Params:
		element - The element to be placed in a container. The container will be placed
		at the back of the Queue.
		'''
		self.__last.append = element
		self.__last = self.__last.getNext

	def dequeue(self) -> DoublyLinkedList | None:
		'''
		Remove the first element in the Queue.

		# Returns:
		None - If the Queue is empty or if the size is 1\n
		or\n
		DoublyLinkedList - The new top of the Queue.
		'''
		if self.__size > 0:
			if self.__queue.getNext != None:
				temp = self.__queue.getNext
				del self.__queue
				self.__queue = temp
			else:
				del self.__queue
				del self.__last
				self.__queue, self.__last = None, None
			
			self.__size -= 1
		
		return self.__queue

	def clear(self) -> None:
		'''
		Remove all elements from the Queue
		'''
		while self.__size > 0:
			self.dequeue()

	def insertBefore(self, first) -> None:
		'''
		Insert an element at the first position

		# Params:
		first - the object that will be put in the first position
		'''
		first = DoublyLinkedList(first)

		if self.__size > 0:
			first.append = self.__queue
			self.__queue = first
		else:
			self.__queue = first
			self.__last = first
			self.__size = 1

	def moveBack(self) -> None:
		'''
		Move top of Queue to the back
		'''
		if self.__size > 1:
			self.__enqueue(self.__queue)
			self.__queue = self.__queue.getNext

	def contains(self, element) -> None:
		pass

	def isEmpty(self) -> bool:
		return (self.__size > 0)

	@property
	def size(self) -> int:
		'''
		# Returns:
		How many elements are in the Queue.
		'''
		return self.__size
