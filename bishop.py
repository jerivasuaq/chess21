from piece import Piece

class Bishop(Piece):
    def __init__(self, row, col, player=1):
        super().__init__(row, col, player)
        self.char = 'B'

    def move(self, row, col, Board):
        if (row > 7 or row < 0 or col > 7 or col < 0):
            print("Movimiento fuera de tablero")
            return
        if (self.row == row or self.col == col):
            print("El alfil ya se encuentra en esta posición")
            return
        m = (row - self.row)/(col - self.col)
        if(abs(m) != 1):
            print("No es movimiento diagonal")
            return
        
        iRow = 1 if row < self.row else -1
        iCol = 1 if col < self.col else -1

        conti = 0
        for i in range(row,self.row,iRow):
            conti += 1
            contj = 0
            for j in range(col,self.col,iCol):
                contj += 1
                if conti == contj:
                    p = Board.board[i][j]
                    if p:
                        if p.player == self.player:
                            print("Ficha aliada en el camino, movimiento fallido")
                            return
                        else:
                            if p.col != col:
                               print("Ficha enemiga en el camino, movimiento fallido")
                               return 
    

        Board.board[self.row][self.col] = None
        super().move(row,col)
        Board.board[row][col] = self
        
        

        