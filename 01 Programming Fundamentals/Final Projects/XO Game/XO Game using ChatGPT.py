import tkinter as tk
from tkinter import messagebox
import random
import glob

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.choices_count = 0
        self.your_choices_count = 0
        self.computer_choices_count = 0
        self.your_score = 0
        self.computer_score = 0

        # Score Label
        self.score_label = tk.Label(root, text=f"You: {self.your_score}  Computer: {self.computer_score}", font=('normal', 14))
        self.score_label.grid(row=0, column=0, columnspan=3)

        # Create buttons
        self.buttons = [[None, None, None] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(root, text="", font=('normal', 20), width=5, height=2,
                    command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i + 1, column=j)

        # Restart Button
        self.restart_button = tk.Button(root, text="Restart", command=self.restart_game)
        self.restart_button.grid(row=4, column=1)

        # Win, lose, and Tie label
        self.result_label = tk.Label(root, text="", font=('normal', 14))
        self.result_label.grid(row=5, column=0, columnspan=3)

    def on_button_click(self, row, col):
        if self.buttons[row][col]['text'] == "":
            self.buttons[row][col]['text'] = "X"
            self.choices_count += 1
            self.your_choices_count += 1
            self.check_winner("X")
            if self.choices_count < 9:
                self.computer_move()

    def computer_move(self):
        available_moves = [(i, j) for i in range(3) for j in range(3) if self.buttons[i][j]['text'] == ""]
        if available_moves:
            row, col = random.choice(available_moves)
            self.buttons[row][col]['text'] = "O"
            self.choices_count += 1
            self.computer_choices_count += 1
            self.check_winner("O")

    def check_winner(self, player):
        for i in range(3):
            # Check rows
            if all(self.buttons[i][j]['text'] == player for j in range(3)):
                self.show_winner(player)

            # Check columns
            if all(self.buttons[j][i]['text'] == player for j in range(3)):
                self.show_winner(player)

        # Check diagonals
        if all(self.buttons[i][i]['text'] == player for i in range(3)):
            self.show_winner(player)
        if all(self.buttons[i][2 - i]['text'] == player for i in range(3)):
            self.show_winner(player)

        # Check for a tie
        if self.choices_count == 9:
            self.show_tie()

    def show_winner(self, player):
        if player == "X":
            self.your_score += 1
            self.result_label.config(text="X wins!")
        else:
            self.computer_score += 1
            self.result_label.config(text="O wins!")

        self.update_score()
        self.reset_board()

    def show_tie(self):
        self.result_label.config(text="It's a tie!")
        self.reset_board()

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ""
        self.choices_count = 0
        self.update_score()

    def update_score(self):
        self.score_label.config(text=f"You: {self.your_score}  Computer: {self.computer_score}")

    def restart_game(self):
        self.your_score = 0
        self.computer_score = 0
        self.update_score()
        self.result_label.config(text="")
        self.reset_board()


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
