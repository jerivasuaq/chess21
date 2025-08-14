from bishop import Bishop
from king import King
from knight import Knight
from pawn import Pawn
from queen import Queen
from rook import Rook

class ChessBoard():
    def __init__(self, name):
        self.name = name
        # Initialize empty board
        self.board = [[None for _ in range(8)] for _ in range(8)]

        # Place main pieces for a team
        def setup_back_row(row, team):
            piece_order = [Rook, Knight, Bishop, Queen if row == 0 else King, 
                          King if row == 0 else Queen, Bishop, Knight, Rook]
            for col, piece_class in enumerate(piece_order):
                self.board[row][col] = piece_class(row, col, team)

        # Place pawns
        def setup_pawns(row, team):
            for col in range(8):
                self.board[row][col] = Pawn(row, col, team)

        # Setup the board with all pieces
        setup_back_row(0, 1)  # Team 1 back row
        setup_pawns(1, 1)     # Team 1 pawns
        setup_pawns(6, 2)     # Team 2 pawns
        setup_back_row(7, 2)  # Team 2 back row

    def draw(self):
        """Draw board with larger squares and alternating tile pattern."""
        sq_h = 3   # lines per square
        sq_w = 5   # chars per square
        dark_fill = '▓'
        light_fill = ' '
        # top file letters
        files = '  ' + ''.join(f.center(sq_w) for f in 'abcdefgh')
        print('Chessboard:', self.name)
        print(files)
        for r in range(8):
            # build sq_h lines for this rank
            rank_lines = ['' for _ in range(sq_h)]
            for c in range(8):
                dark = (r + c) % 2 == 1
                fill = dark_fill if dark else light_fill
                p = self.board[r][c]
                # inside content lines
                for lh in range(sq_h):
                    if lh == sq_h // 2:  # center line, place piece
                        if p:
                            content = p.char.center(sq_w, fill)
                        else:
                            content = fill * sq_w
                    else:
                        content = fill * sq_w
                    rank_lines[lh] += content
            # print each line with rank label
            for lh, line in enumerate(rank_lines):
                prefix = str(8 - r) if lh == sq_h // 2 else ' '
                print(prefix + ' ' + line)
        print(files)

if __name__=='__main__':
    chessBoard = ChessBoard('chessboard1')
    chessBoard.draw()
