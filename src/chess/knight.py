from chess.piece import Piece


class Knight(Piece):
    def __init__(self, row, col, player=1):
        super().__init__(row, col, player)
        self.char = '♞' if player == 1 else '♘'

    def move(self, row, col, Board):
        # Validate bounds
        if not (0 <= row < 8 and 0 <= col < 8):
            print("Move out of board bounds")
            return False
        dr = abs(row - self.row)
        dc = abs(col - self.col)
        if dr == 0 and dc == 0:
            print("Knight is already on that square")
            return False
        if not ((dr == 2 and dc == 1) or (dr == 1 and dc == 2)):
            print("Invalid knight move")
            return False
        dest = Board.board[row][col]
        if dest and dest.player == self.player:
            print("Friendly piece on destination, move failed")
            return False
        # Knights can jump over pieces, so no path check
        Board.board[self.row][self.col] = None
        super().move(row, col)
        Board.board[row][col] = self
        return True

    def big_art(self):
        ch = self.char
        art = [
            "  /^ ",
            " (Kn)",
            f" ({ch}) ",
            " ( / ",
            "  \\_/"
        ]
        return art
