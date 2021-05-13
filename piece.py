class Piece():
    def __init__(self, row, col, player=1):
        self.player = player
        self.row = row
        self.col = col
        self.char = ' '

    def draw(self):
        print(self.char, end ="")

    def info(self):
        print('row:', self.row, 'col:', self.col)

    def move(self, row, col):
        self.row = row
        self.col = col
