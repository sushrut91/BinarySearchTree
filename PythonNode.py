class Node:
	def __init__(self,val):
		self.value = val
		self.leftChild = None
		self.rightChild = None
		
	def insert(self,data):
		if self.value == data:
			return False
		elif data < self.value:
			#Check if there is a left child already present
			if self.leftChild:
				return self.left.insert(data)
			else:
				self.leftChild = Node(data)
				return True
		else:
			if self.rightChild:
				self.rightChild.insert(data)
			else:
				self.rightChild = Node(data)
class Tree:

	def __init__(self):
		self.root = None
		
	def insert(self,data):
		if self.root == None:
			return self.root.insertNode(data)
		else:
			self.root = Node(data)
			'''The node wass added hence return True'''
			return True