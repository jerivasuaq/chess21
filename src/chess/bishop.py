from chess.piece import Piece


class Bishop(Piece):
    def __init__(self, row, col, player=1):
        super().__init__(row, col, player)
        self.char = "♝" if player == 1 else "♗"

    def move(self, row, col, Board):
        # Validate bounds
        if not (0 <= row < 8 and 0 <= col < 8):
            print("Move out of board bounds")
            return False
        dr = row - self.row
        dc = col - self.col
        # Same square
        if dr == 0 and dc == 0:
            print("Bishop is already on that square")
            return False
        # Must be diagonal: |dr| == |dc|
        if abs(dr) != abs(dc):
            print("Not a diagonal move")
            return False

        step_r = 1 if dr > 0 else -1
        step_c = 1 if dc > 0 else -1
        r = self.row + step_r
        c = self.col + step_c
        # Check path (exclude destination)
        while r != row:
            p = Board.board[r][c]
            if p:
                print("Piece blocking the path, move failed")
                return False
            r += step_r
            c += step_c
        # Check destination
        dest = Board.board[row][col]
        if dest and dest.player == self.player:
            print("Friendly piece on destination, move failed")
            return False

        # Move (capture if enemy piece present)
        Board.board[self.row][self.col] = None
        super().move(row, col)
        Board.board[row][col] = self
        return True

    def big_art(self):
        ch = self.char
        art = [" /\\ ", "( B)", f" ({ch})", " /_\\", " === "]
        return art
