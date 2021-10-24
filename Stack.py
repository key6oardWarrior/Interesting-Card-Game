from DoublyLinkedList import DoublyLinkedList

class Stack(DoublyLinkedList):
	__first = None
	__stack = None
	__size = 0

	def __init__(self, first=None) -> None:
		if first != None:
			element = DoublyLinkedList(first)
			self.__first = element
			self.__stack = element
			self.__size = 1

	def peak(self):
		'''
		# Returns:
		Top of the Stack.
		'''
		return (self.__stack.llist) if self.__size > 0 else None

	def push(self, element) -> None:
		'''
		Push an element to the back of the Stack.

		# Params:
		element - Can be of any type, but will be placed in a container. The container will be
		placed at the top of the Stack.
		'''
		elem = DoublyLinkedList(element)

		if self.__size == 0:
			self.__first = elem
			self.__stack = elem
		
		else:
			self.__stack.append = elem
			self.__stack = self.__stack.getNext
			
		self.__size += 1

	def pop(self) -> DoublyLinkedList or None:
		'''
		Removes the element at the top of the stack.

		# Returns:
		None - If the stack is empty before or after the pop\n
		or\n
		DoublyLinkedList - The new element that is at the top of the Stack.
		'''
		if self.__size > 0:
			if self.__stack.getPrev == None:
				del self.__stack
				del self.__first
				self.__stack, self.__first = None, None
			else:
				temp = self.__stack.getPrev
				del self.__stack
				self.__stack = temp

			self.__size -= 1
		
		return self.__stack

	def clear(self) -> None:
		while self.__size > 0:
			self.pop()

	def contains(self, element) -> bool:
		'''
		Checks if the Stack has a given element

		# Params:
		element - Check if this element is in the Stack

		# Returns:
		True if element is in the Stack else False
		'''
		if self.__size > 0:
			PRIMITIVES = (int, bool, float, complex, bytes, memoryview)
			current = self.__first

			if isinstance(element, PRIMITIVES):
				while current != None:
					if current.llist == element:
						return True
					current = current.getNext
			else:
				while current != None:
					if current.llist.__dict__ == element.__dict__:
						return True
					current = current.getNext

		return False

	def insertBefore(self, first: DoublyLinkedList) -> None:
		pass

	def isEmpty(self) -> bool:
		return (self.__size > 0)

	@property
	def size(self) -> int:
		'''
		# Returns:
		The number of elements in the Stack.
		'''
		return self.__size
