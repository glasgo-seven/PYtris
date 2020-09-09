import ansi
import board
import debug
import get_input
from random import randint
import tetromino as tet

exit = False
frame = 0
game_board = board.Board(24, 14)
score = 0

def Start():
	debug.setup_lib()
	game_board.setup()
	# game_board.combine_at_position(tet.Tetromino(1), 2, game_board.size_x // 2 - tet.Tetromino(1).figure_stats['x'] // 2)
	# game_board.c_print()


def Update():
	if game_board.active_tetromino.id == 0:
		if not game_board.can_spawn():
			global exit
			exit = True
		else:
			global score
			score += game_board.is_a_row()
			if game_board.next_tetromino.id == 0:
				game_board.next_tetromino = tet.Tetromino(randint(1, 7))
			game_board.active_tetromino = game_board.next_tetromino
			game_board.next_tetromino = tet.Tetromino(randint(1, 7))
			# game_board.active_tetromino.position = (1, game_board.size_x // 2 - game_board.active_tetromino.figure_stats['x'] // 2)
			game_board.active_tetromino.position = (1, 6)
		game_board.save_board()

	if not exit:
		debug.clear()
		game_board.load_board()
		game_board.combine_at_position(game_board.active_tetromino.position)
		game_board.set_color_board(game_board.active_tetromino.id)
		game_board.c_print()
		print("NEXT:")
		game_board.next_tetromino.c_print()
		print()
		global score
		print("SCORE: " + str(score))
		# print("\nFRAME: " + str(frame) + " DRAWING")
		if game_board.collision_detected():
			game_board.active_tetromino = tet.Tetromino(0)
			score += 10
		else:
			game_board.set_color_board(-1)
			new_position = get_input.input_manager()
			if new_position[0] == 'R':
				if game_board.can_rotate():
					game_board.active_tetromino.rotate(new_position)
			else:
				game_board.active_tetromino.get_new_position(new_position, game_board.size_y, game_board.size_x, game_board.is_propper_move(new_position))
		# print("\nFRAME: " + str(frame) + " CALCULATION")

		global frame
		if frame == 60: frame = 0
		else: frame += 1
	debug.sleep(0.4)

def Finish():
	game_board.close_board()
	print(ansi.colored(" The game is finished.", 'bright_red') + "\n Your score is [" + ansi.colored(str(score), 'yellow') + "] !")
	print(" Press " + ansi.colored("SPACE", 'green') + " to exit.")
	while not get_input.get_exit_input():
		pass
	debug.clear()

Start()
while not exit: Update()
Finish()
