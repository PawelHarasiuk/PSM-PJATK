class GameOfLife:
    def __init__(self, width, height, rule):
        self.width = width
        self.height = height
        self.rule = rule
        self.board = [[0 for x in range(width)] for y in range(height)]
        self.create_board()

    def create_board(self):
        for i in range(self.width):
            for j in range(self.height):
                self.board[i][j] = 0

    def update_board(self):
        new_board = [[0 for x in range(self.width)] for y in range(self.height)]
        for i in range(self.width):
            for j in range(self.height):
                neighbors = self.get_neighbors(i, j)
                if self.board[i][j] == 1:
                    if self.rule[0].__contains__(neighbors):
                        new_board[i][j] = 1
                else:
                    if self.rule[1].__contains__(neighbors):
                        new_board[i][j] = 1
        self.board = new_board

    def get_neighbors(self, i, j):
        neighbors = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == 0 and y == 0:
                    continue
                if i + x < 0 or j + y < 0 or i + x >= self.width or j + y >= self.height:
                    continue
                neighbors.append(self.board[i + x][j + y])
        return neighbors

    def start_game(self):
        while True:
            self.update_board()
            self.gui.draw_board()
            self.gui.root.update()
