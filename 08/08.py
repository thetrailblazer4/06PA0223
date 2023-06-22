def dec_func(orig_func):
	def wrapper_func(*args, **kwargs):
		print('Hello world!')
		return orig_func(*args, **kwargs)
	return wrapper_func


@dec_func
def disp_func():
	print('This is disp_func!')

@dec_func
def disp_info(name, age):
	print(f"disp_info ran with args: '{name}' '{age}'")


disp_info('John', 25)