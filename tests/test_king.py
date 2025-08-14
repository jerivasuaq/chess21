from chess.king import King
from chess.pawn import Pawn


def test_valid_single_step(king_board):
    b, k = king_board
    assert k.move(5, 5, b) is True


def test_invalid_far_move(king_board):
    b, k = king_board
    assert k.move(6, 6, b) is False


def test_capture_enemy(king_board):
    b, k = king_board
    b.board[5][5] = Pawn(5, 5, 2)
    assert k.move(5, 5, b) is True


def test_cannot_capture_ally(king_board):
    b, k = king_board
    b.board[5][5] = Pawn(5, 5, 1)
    assert k.move(5, 5, b) is False
