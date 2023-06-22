# self --> Regular Method; Cls --> Classmethod , staticmethod

class Employee():

	raise_amt = 1.05
	num_emps = 0
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = f'{first}.{last}@company.com'
		self.pay = pay

		Employee.num_emps += 1

	def fullname(self):
		return f'{self.first} {self.last}'

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

	@classmethod
	def set_raise_amt(cls, amt):
		cls.raise_amt = amt

	@classmethod
	def from_str(cls, emp_str):
		first, last, pay = emp_1_str.split('-')
		return cls(first, last, pay)

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True




emp_1 = Employee('John', 'K', 50000)
emp_2 = Employee('Jane', 'M', 60000)


import datetime

my_date = datetime.date(2023, 6, 18)

print(Employee.is_workday(my_date))