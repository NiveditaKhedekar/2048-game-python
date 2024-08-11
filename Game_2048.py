import tkinter as tk
import random

class Game2048(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title('2048')
        self.main_grid = tk.Frame(
            self, bg='black', bd=3, width=400, height=400
        )
        self.main_grid.grid(pady=(100, 0))
        self.make_GUI()
        self.start_game()

        self.master.bind("<Left>", self.move_left)
        self.master.bind("<Right>", self.move_right)
        self.master.bind("<Up>", self.move_up)
        self.master.bind("<Down>", self.move_down)
        self.mainloop()

    def make_GUI(self):
        self.cells = []
        for i in range(4):
            row = []
            for j in range(4):
                cell_frame = tk.Frame(
                    self.main_grid,
                    bg='azure4',
                    width=100,
                    height=100
                )
                cell_frame.grid(row=i, column=j, padx=5, pady=5)
                cell_number = tk.Label(
                    self.main_grid,
                    bg='azure4'
                )
                cell_number.grid(row=i, column=j)
                row.append(cell_number)
            self.cells.append(row)

    def start_game(self):
        self.matrix = [[0] * 4 for _ in range(4)]

        row = random.randint(0, 3)
        col = random.randint(0, 3)
        self.matrix[row][col] = 2
        self.cells[row][col].configure(
            text="2", bg='azure4', fg='black'
        )

        while self.matrix[row][col] != 0:
            row = random.randint(0, 3)
            col = random.randint(0, 3)
        self.matrix[row][col] = 2
        self.cells[row][col].configure(
            text="2", bg='azure4', fg='black'
        )

        self.score = 0

    def stack(self):
        new_matrix = [[0] * 4 for _ in range(4)]
        for i in range(4):
            fill_position = 0
            for j in range(4):
                if self.matrix[i][j] != 0:
                    new_matrix[i][fill_position] = self.matrix[i][j]
                    fill_position += 1
        self.matrix = new_matrix

    def combine(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] != 0 and self.matrix[i][j] == self.matrix[i][j + 1]:
                    self.matrix[i][j] *= 2
                    self.matrix[i][j + 1] = 0
                    self.score += self.matrix[i][j]

    def reverse(self):
        new_matrix = []
        for i in range(4):
            new_matrix.append([])
            for j in range(4):
                new_matrix[i].append(self.matrix[i][3 - j])
        self.matrix = new_matrix

    def transpose(self):
        self.matrix = [list(t) for t in zip(*self.matrix)]

    def add_new_tile(self):
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        while self.matrix[row][col] != 0:
            row = random.randint(0, 3)
            col = random.randint(0, 3)
        self.matrix[row][col] = random.choice([2, 4])

    def update_GUI(self):
        for i in range(4):
            for j in range(4):
                if self.matrix[i][j] == 0:
                    self.cells[i][j].configure(
                        text="", bg='azure4'
                    )
                else:
                    self.cells[i][j].configure(
                        text=str(self.matrix[i][j]),
                        bg='orange',
                        fg='white'
                    )
        self.update_idletasks()

    def move_left(self, event):
        self.stack()
        self.combine()
        self.stack()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    def move_right(self, event):
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    def move_up(self, event):
        self.transpose()
        self.stack()
        self.combine()
        self.stack()
        self.transpose()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    def move_down(self, event):
        self.transpose()
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.transpose()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    def game_over(self):
        if any(2048 in row for row in self.matrix):
            self.game_over_frame = tk.Frame(
                self.main_grid, borderwidth=2
            )
            self.game_over_frame.place(
                relx=0.5, rely=0.5, anchor="center"
            )
            tk.Label(
                self.game_over_frame,
                text="You win!",
                bg="orange",
                fg="white",
                font=("Helvetica", 48)
            ).pack()

        elif not any(0 in row for row in self.matrix):
            self.game_over_frame = tk.Frame(
                self.main_grid, borderwidth=2
            )
            self.game_over_frame.place(
                relx=0.5, rely=0.5, anchor="center"
            )
            tk.Label(
                self.game_over_frame,
                text="Game Over!",
                bg="orange",
                fg="white",
                font=("Helvetica", 48)
            ).pack()

if __name__ == "__main__":
    Game2048()
