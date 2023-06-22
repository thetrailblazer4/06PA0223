# decorators <-- closures <--- first class function

'''
A programming language is said to have First-class functions 
when functions in that language are treated like any other variable.

Inner func that behaves like an object, 
which remembers and has access to variables in the local scope in which it was created 
even after the outer func has finished executing

'''

# def square(x):
# 	return x * x


# result = square
# print(result(5))

# def outer_func(message):
# 	def inner_func():
# 		print(message)

# 	return inner_func

# hello_func = outer_func('Hello')
# hello_func()

# hi_func = outer_func('Hi')
# hi_func()


# def square(print(my_func(my_lst, square))


# [1,2,3,4] --> [1,4,9,16]



# my_lst = [1,2,3,4]

# def my_func(arg_lst, func):
# 	result = []
# 	for i in arg_lst:
# 		result.append(func(i))
# 	return result

# print(my_func(my_lst, square))
# print(my_func(my_lst, cube))

def dec_func(orig_func):
	def wrapper_func():
		print('Hello world!')
		return orig_func()
	return wrapper_func


@dec_func
def disp_func():
	print('This is disp_func!')



# dec_disp = dec_func(disp_func)
disp_func()

# def hi_func():
# 	print('This is hi_func!')
# 	print('Hello universe!')


# def bye_func():
# 	print('This is bye_func!')
# 	print('Hello universe!')


# def hey_func():
# 	print('This is hey_func!')
# 	print('Hello universe!')

# disp_func()
# hi_func()
# bye_func()
# hey_func()