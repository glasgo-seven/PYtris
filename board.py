import ansi
import debug
from copy import deepcopy
import tetromino as tet

class Board():
	def __init__(self, size_y, size_x):
		self.size_y = size_y
		self.size_x = size_x
		self.board = [[0 for x in range(size_x)] for y in range(size_y)]
		self.past_board = self.get_board_copy(self.board)
		self.color_board = self.get_board_copy(self.board)
		self.active_tetromino = tet.Tetromino(0)
		self.next_tetromino = tet.Tetromino(0)

	def get_board_copy(self, board_type):
		return deepcopy(board_type)

	def save_board(self):
		self.past_board = self.get_board_copy(self.board)

	def load_board(self):
		self.board = self.get_board_copy(self.past_board)

	def c_print(self):
		print()
		for y in range(self.size_y):
			print(" ", end = "")
			for x in range(self.size_x):
				if	y >= self.active_tetromino.position[0] + self.active_tetromino.figure_stats['y'] and \
					x >= self.active_tetromino.position[1] and x < self.active_tetromino.position[1] + self.active_tetromino.figure_stats['x'] and \
					self.board[y][x] == ' ':
							print(ansi.colored('.', 'bright_white'), end = "")
				else:
					print(ansi.colored(self.board[y][x], tet.tet_dict[self.color_board[y][x]]['color']), end = "")
			print()
		print()

	def w_print(self):
		pass

	def setup(self):
		for y in range(self.size_y):
			for x in range(self.size_x):
				if (x, y) == (0, 0): self.board[y][x] = '╔'
				elif (x, y) == (self.size_x - 1, 0): self.board[y][x] = '╗'
				elif (x, y) == (0, self.size_y - 1): self.board[y][x] = '╚'
				elif (x, y) == (self.size_x - 1, self.size_y - 1): self.board[y][x] = '╝'
				elif y == 0 or y == self.size_y - 1: self.board[y][x] = '═'
				elif x == 0 or x == self.size_x - 1: self.board[y][x] = '║'
				else:
					self.board[y][x] = ' '
					self.color_board[y][x] = -1

	def combine_at_position(self, position):
		y = position[0]
		x = position[1]

		self.active_tetromino.position = (y, x)
		for _y in range(y, y + self.active_tetromino.figure_stats['y']):
			for _x in range(x, x + self.active_tetromino.figure_stats['x']):
				f_y = _y - y - self.active_tetromino.figure_stats['y']
				f_x = _x - x - self.active_tetromino.figure_stats['x']
				if self.active_tetromino.figure_stats['figure'][f_y][f_x] != ' ':
					self.board[_y][_x] = self.active_tetromino.figure_stats['figure'][f_y][f_x]
				# self.color_board[_y][_x] = self.active_tetromino.id

	def set_color_board(self, color_id):
		for y in range(self.active_tetromino.position[0], self.active_tetromino.position[0] + self.active_tetromino.figure_stats['y']):
				for x in range(self.active_tetromino.position[1], self.active_tetromino.position[1] + self.active_tetromino.figure_stats['x']):
					if self.active_tetromino.figure_stats['figure'][y - self.active_tetromino.position[0]][x - self.active_tetromino.position[1]] != ' ':
						self.color_board[y][x] = color_id

	def is_propper_move(self, delta):
		if delta[1] == -1:
			for y in range(self.active_tetromino.position[0], self.active_tetromino.position[0] + self.active_tetromino.figure_stats['y']):
				if self.board[y][self.active_tetromino.position[1] - 1] != ' ':
					return 0
		if delta[1] == 1:
			for y in range(self.active_tetromino.position[0], self.active_tetromino.position[0] + self.active_tetromino.figure_stats['y']):
				if self.board[y][self.active_tetromino.position[1] + self.active_tetromino.figure_stats['x']] != ' ':
					return 0
		return 1

	def collision_detected(self):
		# game_board.color_board[game_board.active_tetromino.position[0] + game_board.active_tetromino.figure_stats['y']][game_board.active_tetromino.position[1]] != -1
		collision = 0
		for y in range(self.active_tetromino.position[0], self.active_tetromino.position[0] + self.active_tetromino.figure_stats['y']):
			for x in range(self.active_tetromino.position[1], self.active_tetromino.position[1] + self.active_tetromino.figure_stats['x']):
				if y < self.active_tetromino.position[0] + self.active_tetromino.figure_stats['y'] - 1:
					if self.board[y][x] == '▓' and self.board[y + 1][x] != self.active_tetromino.figure_stats['figure'][y - self.active_tetromino.position[0] + 1][x - self.active_tetromino.position[1]]:
						collision = 1
						break
					else:
						collision = 0
				else:
					if (self.board[y][x] == '▓' and self.board[y + 1][x] == '▓') or self.color_board[y + 1][x] == 0:
						collision = 1
						break
					else:
						collision = 0
		return collision

	def is_a_row(self):
		'''y = self.size_y - 2
		row = True
		while row:
			for x in range(1, self.size_x - 1):
				if self.color_board[y][x] == -1:
					row = False
					break
			if not row:
				break
			y -= 1
		if row or y < self.size_y - 2:
			for _y in range(y + 1, self.size_y - 1):
				for x in range(1, self.size_x - 1):
					self.board[_y][x] = '■'
					self.color_board[_y][x] = -3
			self.c_print()
			debug.sleep(0.25)
			for _y in range(y + 1, self.size_y - 1):
				for x in range(self.size_x - 1):
					self.board[_y][x] = self.board[_y - 1][x]
					self.color_board[_y][x] = self.color_board[_y - 1][x]
			self.c_print()
			debug.sleep(0.25)'''
		is_rows = list()
		score = 0
		for y in range(1, self.size_y - 1):
			row = 0
			for x in range(1, self.size_x - 1):
				if self.board[y][x] == '▓':
					row += 1
			if row == self.size_x - 2:
				is_rows.append(y)
		if len(is_rows) != 0:
			for row in is_rows:
				score += 100
				for x in range(1, self.size_x - 1):
					self.board[row][x] = '■'
					self.color_board[row][x] = -3
			debug.clear()
			self.c_print()
			debug.sleep(0.25)
			for y in range(self.size_y - 1, 1, -1):
				if self.board[y][1] == '■':
					for s_y in range(y, 1, -1):
						for s_x in range(1, self.size_x - 1):
							self.board[s_y][s_x] = self.board[s_y - 1][s_x]
							self.color_board[s_y][s_x] = self.color_board[s_y - 1][s_x]
			debug.clear()
			self.c_print()
			debug.sleep(0.25)
		return score

	def can_rotate(self):
		new_y = self.active_tetromino.figure_stats['y']
		new_x = self.active_tetromino.figure_stats['x']
		y = self.active_tetromino.position[0]
		x = self.active_tetromino.position[1]
		if y + new_y < self.size_y - 1 and x + new_x < self.size_x - 1:
			return 1
		return 0

	def can_spawn(self):
		for y in range(1, 3):
			for x in range(1, self.size_x - 1):
				if self.color_board[y][x] != -1:
					return 0
		return 1

	def close_board(self):
		for z in range(1, self.size_y - 1, 2):
			for y in range(2):
				for x in range(1, self.size_x - 1):
					self.board[z + y][x] = '░'
					self.color_board[z + y][x] = -2
			debug.clear()
			self.c_print()
			debug.sleep(0.1)
