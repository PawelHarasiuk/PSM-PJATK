import tkinter as tk


class GUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=game.width * 10, height=game.height * 10)
        self.canvas.pack()
        self.draw_board()
        self.rule_entry = tk.Entry(self.root)
        self.rule_entry.pack()
        self.start_button = tk.Button(self.root, text="Start", command=self.start_game)
        self.start_button.pack()
        self.root.mainloop()

    def draw_board(self):
        self.canvas.delete("all")
        for i in range(self.game.width):
            for j in range(self.game.height):
                if self.game.board[i][j] == 1:
                    self.canvas.create_rectangle(i * 10, j * 10, i * 10 + 10, j * 10 + 10, fill="black")

    def start_game(self):
        rule = self.rule_entry.get()
        self.game.rule = rule
        self.game.gui = self
        self.game.start_game()
