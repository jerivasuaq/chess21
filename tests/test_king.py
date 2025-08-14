from chess.king import King
from chess.pawn import Pawn


def test_valid_single_step(empty_board):
    b = empty_board
    k = King(4, 4, 1)
    b.board[4][4] = k
    assert k.move(5, 5, b) is True


def test_invalid_far_move(empty_board):
    b = empty_board
    k = King(4, 4, 1)
    b.board[4][4] = k
    assert k.move(6, 6, b) is False


def test_capture_enemy(empty_board):
    b = empty_board
    k = King(4, 4, 1)
    b.board[4][4] = k
    b.board[5][5] = Pawn(5, 5, 2)
    assert k.move(5, 5, b) is True


def test_cannot_capture_ally(empty_board):
    b = empty_board
    k = King(4, 4, 1)
    b.board[4][4] = k
    b.board[5][5] = Pawn(5, 5, 1)
    assert k.move(5, 5, b) is False
