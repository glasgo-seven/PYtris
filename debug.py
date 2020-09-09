from os import system, name
from time import sleep

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

def setup_lib():
	system('setup.sh')
