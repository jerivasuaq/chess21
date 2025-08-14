from chessboard import ChessBoard

def empty_board():
    b = ChessBoard('test')
    # wipe all pieces for controlled tests
    for r in range(8):
        for c in range(8):
            b.board[r][c] = None
    return b
