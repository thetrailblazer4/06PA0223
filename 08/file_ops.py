# f = open('disp_info.log')

# print(f.read())

# f.close()


# with open('disp_info.log', 'r') as f:
	
# 	for line in f:
# 		print(line, end='')

# with open('disp.log', 'w') as f:
# 	f.write('Hello world')
# 	f.seek(0)
# 	f.write('Hey')


with open('disp_info.log', 'r') as rf:
	with open('disp_copy.txt', 'w') as wf:
		for line in rf:
			wf.write(line)