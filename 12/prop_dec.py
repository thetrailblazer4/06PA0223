class Employee():
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay

	def __repr__(self):
		return f"Employee('{self.first}', '{self.last}', {self.pay})"

	def __str__(self):
		return f"{self.fullname} - {self.pay}"

	@property
	def fullname(self):
		return f'{self.first} {self.last}'

	@property
	def email(self):
		return f'{self.first}.{self.last}@company.com'


	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)



emp_1 = Employee('John', 'K', 50000)


print(emp_1.__repr__())
print(emp_1.__str__())