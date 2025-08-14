import pytest
from chess.rook import Rook
from chess.pawn import Pawn

def test_valid_move_horizontal(rook_board):
    b, r = rook_board
    assert r.move(0,5,b) is True
    assert b.board[0][5] is r


def test_blocked_path(rook_board):
    b, r = rook_board
    b.board[0][3] = Pawn(0,3,1)
    assert r.move(0,5,b) is False
    assert b.board[0][0] is r


def test_capture_enemy(rook_board):
    b, r = rook_board
    b.board[0][5] = Pawn(0,5,2)
    assert r.move(0,5,b) is True
    assert b.board[0][5] is r


def test_cannot_capture_ally(rook_board):
    b, r = rook_board
    b.board[0][5] = Pawn(0,5,1)
    assert r.move(0,5,b) is False
    assert b.board[0][0] is r


def test_invalid_diagonal(rook_board):
    b, r = rook_board
    assert r.move(3,3,b) is False
