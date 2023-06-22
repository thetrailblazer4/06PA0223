# class, methods, class variables, instances


class Employee():

	raise_amt = 1.05
	num_emps = 0
	
	def __init__(t, first, last, pay):
		self.first = first
		self.last = last
		self.email = f'{first}.{last}@company.com'
		self.pay = pay

		Employee.num_emps += 1

	def fullname(self):
		return f'{self.first} {self.last}'


	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)



print(Employee.num_emps)
emp_1 = Employee('John', 'K', 50000)
emp_2 = Employee('Jane', 'M', 60000)

print(Employee.num_emps)

# print(Employee.total_emps())
