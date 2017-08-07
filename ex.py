class ix(object) :
	def __init__(self) :
		self.tx = "AAAAAAAAAAAAAAAAAAAA"
		print("create ix")
	def show(self) :
		print(self.tx + " says")

IX = ix()
print(IX.tx)
IX.show()
