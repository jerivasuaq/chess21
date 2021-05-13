
from piece import Piece



class Pawn(Piece):
    def __init__(self, row, col, player=1):
        super().__init__(row, col, player)
        self.char = 'P'  
        self.move_1 = True
        

    def move (self, drow, dcol, board):
    	can_eat = (eat(board, dcol, drow))
	if self.move_1 ==True and drow<3 or (dcol<2 and can_eat==True):
		return True
	if else self.move_1 == False and drow<2 or (dcol<2 and can_eat==True):
		return True
	else 
		return False
	self.move_1 = False
	
    def eat (board, dcol, drow):
    	if (chessBoard.board[dcol+1][drow+1]!=None) or ((chessBoard.board[dcol+1][drow-1]!=None)):
    		if (chessBoard.board[dcol+1][drow+1].player != self.player) or ((chessBoard.board[dcol+1][drow-1]!=self.player)
    			return True
    			
