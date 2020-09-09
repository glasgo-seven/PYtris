import ansi
from copy import deepcopy

tet_dict = {
	-3:	{	'figure': [],
			'y': 0,
			'x': 0,
			'color': "bright_purple"},
	
	-2:	{	'figure': [],
			'y': 0,
			'x': 0,
			'color': "bright_black"},
	
	-1:	{	'figure': [],
			'y': 0,
			'x': 0,
			'color': "black"},
	
	0:	{	'figure': [],
			'y': 0,
			'x': 0,
			'color': "white"},
	
	1:	{	'figure': ["▓▓▓▓"],
			'y': 1,
			'x': 4,
			'color': 'cian'},
	
	2:	{	'figure': ["▓  ", "▓▓▓"],
			'y': 2,
			'x': 3,
			'color': 'blue'},
	
	3:	{	'figure': ["▓▓▓", "▓  "],
			'y': 2,
			'x': 3,
			'color': 'bright_yellow'},
	
	4:	{	'figure': ["▓▓", "▓▓"],
			'y': 2,
			'x': 2,
			'color': 'yellow'},
	
	5:	{	'figure': [" ▓▓", "▓▓ "],
			'y': 2,
			'x': 3,
			'color': 'green'},
	
	6:	{	'figure': ["▓▓▓", " ▓ "],
			'y': 2,
			'x': 3,
			'color': 'purple'},
	
	7:	{	'figure': ["▓▓ ", " ▓▓"],
			'y': 2,
			'x': 3,
			'color': 'red'},
}

class Tetromino():
	'''
		id	:	tetromino
		0	:	NULL
		1	:	|
		2	:	J
		3	:	L
		4	:	O
		5	:	S
		6	:	T
		7	:	Z
	'''
	def __init__(self, id = 0):
		self.id = id
		self.figure_stats = deepcopy(tet_dict[id])
		self.position = (0, 0)

	def c_print(self):
		for y in range(self.figure_stats['y']):
			for x in range(self.figure_stats['x']):
				print(ansi.colored(self.figure_stats['figure'][y][x], self.figure_stats['color']), end = '')
			print()

	def get_new_position(self, delta, size_y, size_x, is_propper_move):
		if	self.position[0] + delta[0] <= 0 or self.position[1] + delta[1] <= 0 or \
			self.position[0] + delta[0] + self.figure_stats['y'] >= size_y or \
			self.position[1] + delta[1] + self.figure_stats['x'] >= size_x or not is_propper_move:
			pass
		else:
			self.position = (self.position[0] + delta[0], self.position[1] + delta[1])

	def rot_e(self):
		'''
			Rotate clockwise
		'''
		fig_rot = list()
		for x in range(self.figure_stats['x']):
			new_row = list()
			for y in range(self.figure_stats['y'] - 1, -1, -1):
				new_row.append(self.figure_stats['figure'][y][x])
			fig_rot.append(new_row)
		return fig_rot

	def rot_q(self):
		'''
			Rotate counterclock-wise
		'''
		fig_rot = list()
		for x in range(self.figure_stats['x'] - 1, -1 , -1):
			new_row = list()
			for y in range(self.figure_stats['y']):
				new_row.append(self.figure_stats['figure'][y][x])
			fig_rot.append(new_row)
		return fig_rot


	def rotate(self, pos):
		# fig_rot = tuple(zip(*fig_rot[::-1]))
		if pos[1] == 1:
			self.figure_stats['figure'] = self.rot_e()
		elif pos[1] == -1:
			self.figure_stats['figure'] = self.rot_q()
		self.figure_stats['y'] = len(self.figure_stats['figure'])
		self.figure_stats['x'] = len(self.figure_stats['figure'][0])
