from chess.pawn import Pawn


def test_single_step(empty_board):
    pawn1 = Pawn(1, 3, 1)
    empty_board.board[1][3] = pawn1
    assert pawn1.move(2, 3, empty_board)


def test_double_step_initial(empty_board):
    pawn1 = Pawn(1, 3, 1)
    empty_board.board[1][3] = pawn1
    assert pawn1.move(3, 3, empty_board)


def test_double_step_blocked(empty_board):
    b = empty_board
    p = Pawn(1, 0, 1)
    b.board[1][0] = p
    blocker = Pawn(2, 0, 1)
    b.board[2][0] = blocker
    assert not p.move(3, 0, b)


def test_capture(empty_board):
    b = empty_board
    pawn1 = Pawn(1, 3, 1)
    b.board[1][3] = pawn1
    enemy = Pawn(2, 4, 2)
    b.board[2][4] = enemy
    assert pawn1.move(2, 4, b)


def test_invalid_capture_forward(empty_board):
    b = empty_board
    pawn1 = Pawn(1, 3, 1)
    b.board[1][3] = pawn1
    assert pawn1.move(2, 3, b)
    enemy = Pawn(3, 3, 2)
    b.board[3][3] = enemy
    assert not pawn1.move(3, 3, b)


def test_player2_direction(empty_board):
    b = empty_board
    pawn2 = Pawn(6, 4, 2)
    b.board[6][4] = pawn2
    assert pawn2.move(5, 4, b)
    assert not pawn2.move(6, 4, b)
