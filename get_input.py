''' input example
	import keyboard  # using module keyboard

	def input():
		while True:  # making a loop
			try:  # used try so that if user pressed other than the given key error will not be shown
				if keyboard.is_pressed('q'):  # if key 'q' is pressed 
					print('You Pressed A Key!')
					break  # finishing the loop
			except:
				break  # if user pressed a key other than the given key the loop will break
'''
from keyboard import is_pressed as p

def get_input():
	if p('a'):
		return (0, -1)
	elif p('d'):
		return (0, 1)
	elif p('q'):
		return ('R', -1)
	elif p('e'):
		return ('R', 1)
	'''elif p('s'):
		return (2, 0)'''
	return (1, 0)

def get_exit_input():
	if p(' '):
		return 1
	return 0

def input_manager():
	i = get_input()
	print("\nVECTOR:" + str(i))
	return i
