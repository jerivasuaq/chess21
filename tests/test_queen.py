import pytest

from chess.queen import Queen
from chess.pawn import Pawn


@pytest.fixture
def queen_board(empty_board):
    b = empty_board
    q = Queen(4, 4, 1)
    b.board[4][4] = q
    return b, q


def test_valid_move_diagonal(queen_board):
    b, q = queen_board
    assert q.move(1, 1, b) is True
    assert b.board[1][1] is q


def test_valid_move_straight(queen_board):
    b, q = queen_board
    assert q.move(4, 7, b) is True
    assert b.board[4][7] is q


def test_blocked_path(queen_board):
    b, q = queen_board
    b.board[4][6] = Pawn(4, 6, 1)
    assert q.move(4, 7, b) is False


def test_capture_enemy(queen_board):
    b, q = queen_board
    b.board[1][1] = Pawn(1, 1, 2)
    assert q.move(1, 1, b) is True


def test_cannot_capture_ally(queen_board):
    b, q = queen_board
    b.board[1][1] = Pawn(1, 1, 1)
    assert q.move(1, 1, b) is False


def test_invalid_move(queen_board):
    b, q = queen_board
    assert q.move(6, 5, b) is False
