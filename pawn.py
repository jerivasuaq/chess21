
class Pawn():
    def __init__(self, row, col, player=1):
        self.player = player
        self.row = row
        self.col = col

    def draw(self):
        print('P')

    def info(self):
        print('row', self.row, 'col', self.col)

    def move(self, row, col):
        self.row = row
        self.col = col
