

class tree:
	def __init__(self, x):
		self.store=[x, []]
	def AddSuccessor(self, x):
		self.store[1] = self.store[1] + [x]
		return True
	def Print_DepthFirst(self):
		return self.Print_DepthFirst2(0)
	def Print_DepthFirst2(self, n):
		if (self == None):
			return False
		for i in range(0, n):
			print '   ',
		print self.store[0]
		for i in range(0, len(self.store[1])):
			(self.store[1][i]).Print_DepthFirst2(n+1)
		return True
	def Get_LevelOrder(self):
		treelist =  []
		treelist = treelist + [self.store]
		accum = []
		while True:
			if (len(treelist) == 0):
				break
			else:
				y = treelist[0]
				treelist = treelist[1:]
				accum = accum + [y[0]]
				for i in y[1]:
					treelist = treelist + [i.store]
		return accum


