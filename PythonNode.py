class BinaryTree:
	def __init__(self):
		self.data = None
		self.left = None
		self.right = None
	def printNode(self):
		print self.data
	def insertNode(self,data):
		if self.left == None and self.right == None:
			self.data = data
			self.left = data
			self.right = data
		elif data > self.data:
			self.data = data
			self.right = data
		else:
			self.data = data
			self.left = data				