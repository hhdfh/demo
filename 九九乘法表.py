for k in range(1,10):
	for l in range(1, 10):
		formula = '{0:1}x{1:1}={2:<2}'.format(k, l, k*l)
		if k>l:
			print(end='       ')
		if k<=l:
			print(formula, end=' ')
	print()
