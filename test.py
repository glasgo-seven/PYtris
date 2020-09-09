def c_print(lst):
	for y in range(len(lst)):
		for x in range(len(lst[y])):
			print(lst[y][x], end = '')
		print()
	print()

original = ['▓▓▓', '▓  ']
c_print(original)
original = tuple(zip(*original[::-1]))
c_print(original)
original = tuple(zip(*original[::-1]))
c_print(original)
original = tuple(zip(*original[::-1]))
c_print(original)
original = tuple(zip(*original[::-1]))
c_print(original)