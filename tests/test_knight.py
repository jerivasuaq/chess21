import pytest
from chess.knight import Knight
from chess.pawn import Pawn

def test_valid_moves(knight_board):
    b, k = knight_board
    for (r,c) in [(6,5),(6,3),(2,5),(2,3),(5,6),(5,2),(3,6),(3,2)]:
        from chess.chessboard import ChessBoard
        b2 = ChessBoard('tmp')
        for rr in range(8):
            for cc in range(8):
                b2.board[rr][cc] = None
        k2 = Knight(4,4,1)
        b2.board[4][4] = k2
        assert k2.move(r,c,b2)


def test_invalid_move(knight_board):
    b, k = knight_board
    assert k.move(5,5,b) is False


def test_capture_enemy(knight_board):
    b, k = knight_board
    b.board[6][5] = Pawn(6,5,2)
    assert k.move(6,5,b) is True


def test_blocked_ignores(knight_board):
    b, k = knight_board
    b.board[5][4] = Pawn(5,4,1)
    assert k.move(6,5,b) is True


def test_cannot_capture_ally(knight_board):
    b, k = knight_board
    b.board[6][5] = Pawn(6,5,1)
    assert k.move(6,5,b) is False
