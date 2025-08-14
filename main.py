from chessboard import ChessBoard

import os


def clear_screen():
    os.system('clear')  # Linux/macOS


print('Chess game')
board = ChessBoard('chessboard1')


def print_board():
    board.draw()
    print("Enter moves in algebraic form: e2 e4 (from to), or 'quit'")


# map algebraic to indices
files = {f: i for i, f in enumerate('abcdefgh')}


def parse_square(sq):
    if len(sq) != 2:
        return None
    file = sq[0].lower()
    rank = sq[1]
    if file not in files or not rank.isdigit():
        return None
    r = 8 - int(rank)
    c = files[file]
    if not (0 <= r < 8 and 0 <= c < 8):
        return None
    return r, c


current_player = 1
while True:
    clear_screen()
    print(f"Player {current_player} to move")
    print_board()
    move_input = input('Move: ').strip()
    if move_input.lower() in ('q', 'quit', 'exit'):
        break
    parts = move_input.split()
    if len(parts) != 2:
        input('Invalid format. Press Enter...')
        continue
    src = parse_square(parts[0])
    dst = parse_square(parts[1])
    if not src or not dst:
        input('Invalid square. Press Enter...')
        continue
    sr, sc = src
    dr, dc = dst
    piece = board.board[sr][sc]
    if not piece:
        input('No piece at source. Press Enter...')
        continue
    if piece.player != current_player:
        input('Not your piece. Press Enter...')
        continue
    ok = piece.move(dr, dc, board)
    if not ok:
        input('Illegal move. Press Enter...')
        continue
    # switch player
    current_player = 2 if current_player == 1 else 1

print('Game over')
