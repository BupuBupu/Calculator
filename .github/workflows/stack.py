class Stack:
	def __init__(self):
		# Initialise the stack's data attributes
		self.stk = []
		
	
	def push(self, item):
		#Add item to stack
		self.stk.insert(0,item)
		

	def peek(self):
		# Return the element at the top of the stack
		# Return a string "Error" if stack is empty
		if self.stk!=[]:
			a = self.stk[0]
			return a
		else:
			return "error"
	
	def is_empty(self):
		# Return True if stack is empty, False otherwise
		if self.stk==[]:
			return True
		else:
			return False

	def pop(self):
		# Pop an item from the stack if non-empty
		if self.stk!=[]:
			return self.stk.pop(0)
		else:
			return "error"





	def __str__(self):
		# Return a string containing elements of current stack in top-to-bottom order, separated by spaces
		# Example, if we push "2" and then "3" to the stack (and don't pop any elements), 
		# then the string returned should be "3 2"
		a = self.stk[::-1]
		b = ""
		for i in a:
			b+=str(i)+" "
		b = b.rstrip()
		return b[::-1]
		

	def __len__(self):
		if self.stk!=[]:
			return len(self.stk)
		else:
			return 0
	

