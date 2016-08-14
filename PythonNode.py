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
				return self.leftChild.insert(data)
			else:
				self.leftChild = Node(data)
				return True
		else:
			if self.rightChild:
				return self.rightChild.insert(data)
			else:
				self.rightChild = Node(data)
				return True
	
	def find(self, data):
		if self.value == data:
			return True
		elif data < self.value:
			if self.leftChild:
				return self.leftChild.find(data)
			else:
				return False
		else:
			if self.rightChild:
				return self.rightChild.find(data)
			else:
				return False
	
	def preorder(self):
		if self:
			print (str(self.value))
			if self.leftChild:
				self.leftChild.preorder()
			if self.rightChild:
				self.rightChild.preorder()
	
	def postorder(self):
		if self:
			if self.leftChild:
				self.leftChild.postorder()
			if self.rightChild:
				self.rightChild.postorder()
			print str(self.value)
			
	def inorder(self):
		if self:
			if self.leftChild:
				self.leftChild.inorder()
			print str(self.value)
			if self.rightChild:
				self.rightChild.inorder()
				
class Tree:	
	def __init__(self):
		self.root = None
		
	def insert(self,data):
		if not self.root == None:
			return self.root.insert(data)
		else:
			self.root = Node(data)
			'''The node was added hence return True'''
			return True
			
	def find(self, data):
		# A root node was found to be existing
		if self.root:
			return self.root.find(data)
		else:
			#Quit as not root node was found
			return False
			
	def preorder(self):
		self.root.preorder()
		
	def postorder(self):
		self.root.postorder()
		
	def inorder(self):
		self.root.inorder()