from piece import Piece

class King(Piece):
    def __init__(self, row, col, player=1):
        super().__init__(row, col, player)
        self.char = '♚' if player == 1 else '♔'

    def move(self, row, col, Board):
        # Validate bounds
        if not (0 <= row < 8 and 0 <= col < 8):
            print("Move out of board bounds")
            return False
        dr = abs(row - self.row)
        dc = abs(col - self.col)
        if dr == 0 and dc == 0:
            print("King is already on that square")
            return False
        if dr > 1 or dc > 1:
            print("Invalid king move")
            return False
        dest = Board.board[row][col]
        if dest and dest.player == self.player:
            print("Friendly piece on destination, move failed")
            return False
        Board.board[self.row][self.col] = None
        super().move(row, col)
        Board.board[row][col] = self
        return True
