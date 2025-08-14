import pytest
from chess.chessboard import ChessBoard
from chess.bishop import Bishop
from chess.rook import Rook
from chess.knight import Knight
from chess.queen import Queen
from chess.king import King
from chess.pawn import Pawn

@pytest.fixture
def empty_board():
    b = ChessBoard('test')
    # wipe all pieces for controlled tests
    for r in range(8):
        for c in range(8):
            b.board[r][c] = None
    return b

# Piece fixtures
@pytest.fixture
def bishop_board(empty_board):
    b = empty_board
    bish = Bishop(3,3,1)
    b.board[3][3] = bish
    return b, bish

@pytest.fixture
def rook_board(empty_board):
    b = empty_board
    r = Rook(0,0,1)
    b.board[0][0] = r
    return b, r

@pytest.fixture
def knight_board(empty_board):
    b = empty_board
    k = Knight(4,4,1)
    b.board[4][4] = k
    return b, k

@pytest.fixture
def queen_board(empty_board):
    b = empty_board
    q = Queen(4,4,1)
    b.board[4][4] = q
    return b, q

@pytest.fixture
def king_board(empty_board):
    b = empty_board
    k = King(4,4,1)
    b.board[4][4] = k
    return b, k

@pytest.fixture
def two_pawns():
    # returns a board and two pawns from opposite teams facing each other scenario
    b = ChessBoard('pawns')
    for r in range(8):
        for c in range(8):
            b.board[r][c] = None
    p1 = Pawn(1,3,1); b.board[1][3] = p1
    p2 = Pawn(6,4,2); b.board[6][4] = p2
    return b, p1, p2
