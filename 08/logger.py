from functools import wraps

def logger(orig_func):
	import logging
	logging.basicConfig(filename=f"{orig_func.__name__}.log", level=logging.INFO)

	@wraps(orig_func)
	def wrapper_func(*args, **kwargs):
		logging.info(f"Ran with args: {args} and kwargs: {kwargs}")
		return orig_func(*args, **kwargs)
	return wrapper_func


def my_timer(orig_func):
	import time

	@wraps(orig_func)
	def wrapper_func(*args, **kwargs):
		ct = time.time()
		result = orig_func(*args, **kwargs)
		nt = time.time() - ct
		print(f"{orig_func.__name__} ran in {nt} secs")
		return result
	return wrapper_func


import time


@logger
@my_timer
def disp_info(name, age):
	time.sleep(1)
	print(f"disp_info ran with args: '{name}' '{age}'")


disp_info('Jane', 45)

