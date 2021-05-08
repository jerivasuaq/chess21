
class Rook():
    def __init__(self, row, col, player=1):
        self.row = row
        self.col = col
        self.player = player

    def draw(self):
        print('R')
    
    def info(self):
        print('row', self.row, 'col', self.col)

    def move(self, row, col):
        self.row = row
        self.col = col
