class payment:
	def __init__(self, name, amount, due):
		self.name = name
		self.amount = amount
		self.due = due
		self.current = 0

	def add(self, amount):
		if(self.current + amount <= self.amount):
			self.current += amount

	def details(self):
		print(self.name + ":\n" + "\tCurrent: " + str(self.current) + "\n\tAmount: " + str(self.amount) + "\n\tDue: " + self.due)