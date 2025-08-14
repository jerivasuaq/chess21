from piece import Piece


class Pawn(Piece):
    def __init__(self, row, col, player=1):
        super().__init__(row, col, player)
        self.char = '♟' if player == 1 else '♙'

    def move(self, row, col, Board):
        # Player 1 assumed moves 'down' (+1 row), player 2 moves 'up' (-1 row)
        direction = 1 if self.player == 1 else -1
        start_row = 1 if self.player == 1 else 6
        # Validate bounds
        if not (0 <= row < 8 and 0 <= col < 8):
            print("Move out of board bounds")
            return False
        dr = row - self.row
        dc = col - self.col
        if dr == 0 and dc == 0:
            print("Pawn is already on that square")
            return False
        # Forward move(s)
        if dc == 0:
            # Single step
            if dr == direction:
                if Board.board[row][col] is None:
                    Board.board[self.row][self.col] = None
                    super().move(row, col)
                    Board.board[row][col] = self
                    return True
                else:
                    print("Square occupied, move failed")
                    return False
            # Double step from start
            if dr == 2 * direction and self.row == start_row:
                intermediate_row = self.row + direction
                if Board.board[intermediate_row][col] is None and Board.board[row][col] is None:
                    Board.board[self.row][self.col] = None
                    super().move(row, col)
                    Board.board[row][col] = self
                    return True
                else:
                    print("Path blocked for double step")
                    return False
            print("Invalid pawn forward move")
            return False
        # Capture move
        if abs(dc) == 1 and dr == direction:
            dest = Board.board[row][col]
            if dest and dest.player != self.player:
                Board.board[self.row][self.col] = None
                super().move(row, col)
                Board.board[row][col] = self
                return True
            else:
                print("Invalid pawn capture")
                return False
        print("Invalid pawn move")
        return False

