class Numstring:
	def __init__(self, init_str=""):
		self.num = 0
		self.length = 0

		for char in init_str:
			self.append(char)

	def toString(self, curr=None):
		if curr is None:
			curr = self.num

		retlst = []

		while curr:
			char = chr(curr % 10000)
			retlst.append(char)
			curr = curr // 10000

		return "".join(retlst)

	def appendleft(self, char):
		assert len(char) == 1
		self.num *= 10000
		self.num += ord(char)
		self.length += 1

	def append(self, char):
		self.num += ord(char)*(10000**self.length)
		self.length += 1	

	def pop(self):
		# self.num = self.num % (10000**self.length-1)
		self.num = self.num % 10000**(self.length-1)
		self.length -= 1

	def popleft(self):
		self.num = self.num // 10000
		self.length -= 1

	def compare(self, numstring2):
		return self.num == numstring2.num

	def size(self):
		return self.length

	def get(self, start, end=None):
		if start >= self.length:
			raise IndexError("index out of bounds")
		if end and end > self.length + 1:
			raise IndexError("index out of bounds")

		if end is not None:
			if start == end:
				return ""

			curr = self.num

			curr = curr // (10000 ** start)

			curr = curr % 10000**(end)

			return self.toString(curr)
		else:
			curr = self.num

			curr = curr // (10000 ** start)

			char = chr(curr % 10000)
			return char

