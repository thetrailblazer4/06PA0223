# TypeError
# SyntaxError
# NameError


# try:
# 	pass
# except Exception:
# 	pass
# else:
# 	pass
# finally:
# 	pass

# f = open('newfile.txt')

try:
	f = open('newfile.txt')
	# new_var = old_var
except FileNotFoundError as e:
	print(e)
except Exception as e:
	print(e)
else:
	print(f.read())
finally:
	print('Executing.....')