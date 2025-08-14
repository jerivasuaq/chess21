import pytest
from chess.bishop import Bishop
from chess.pawn import Pawn

def test_valid_move_diagonal(bishop_board):
    b, bish = bishop_board
    assert bish.move(0,0,b) is True
    assert b.board[0][0] is bish


def test_blocked_path(bishop_board):
    b, bish = bishop_board
    b.board[2][2] = Pawn(2,2,1)
    assert bish.move(0,0,b) is False
    assert b.board[3][3] is bish


def test_capture_enemy(bishop_board):
    b, bish = bishop_board
    b.board[1][1] = Pawn(1,1,2)
    assert bish.move(1,1,b) is True
    assert b.board[1][1] is bish


def test_cannot_capture_ally(bishop_board):
    b, bish = bishop_board
    b.board[1][1] = Pawn(1,1,1)
    assert bish.move(1,1,b) is False
    assert b.board[3][3] is bish


def test_invalid_non_diagonal(bishop_board):
    b, bish = bishop_board
    assert bish.move(3,5,b) is False
