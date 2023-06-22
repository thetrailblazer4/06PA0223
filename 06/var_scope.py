# LEGB --> Local, Enclosing, Global, Builtins

# x = 'global x'


# def outer_func():
# 	# global x
# 	x = 'local x'
# 	print(x)

# outer_func()
# print(x)

# import builtins

# print(dir(builtins))

# list_1 = [34,1,31,0,100]

# def min():
# 	print('Hello')

# print(min(list_1))

x = 'global x'

def outer_func():
	x = 'local x'

	def inner():
		x = 'inner x'
		print(x)

	inner()
	
	print(x)

outer_func()
