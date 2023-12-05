import tkinter as tk
import random

root = tk.Tk()
root.title("Tic-Tac-Toe")

choices_count = 0
your_choices_count = 0
computer_choices_count = 0
your_score = 0
computer_score = 0

# Score Label
score_label = tk.Label(root, text=f"You: {your_score}  Computer: {computer_score}", font=('normal', 14))
score_label.grid(row=0, column=0, columnspan=3)

# Create buttons
buttons = [[None, None, None] for _ in range(3)]
for i in range(3):
    for j in range(3):
        button = tk.Button(root, text="", font=('normal', 20), width=5, height=2)
        button.grid(row=i + 1, column=j)
        buttons[i][j] = button

# Restart Button
def restart_game():
    global your_score, computer_score, choices_count
    your_score = 0
    computer_score = 0
    update_score()
    result_label.config(text="")
    reset_board()

restart_button = tk.Button(root, text="Restart", command=restart_game)
restart_button.grid(row=4, column=1)

# Win, lose, and Tie label
result_label = tk.Label(root, text="", font=('normal', 14))
result_label.grid(row=5, column=0, columnspan=3)

def on_button_click(row, col):
    global choices_count, your_choices_count
    if buttons[row][col]['text'] == "":
        buttons[row][col]['text'] = "X"
        choices_count += 1
        your_choices_count += 1
        check_winner("X")
        if choices_count < 9:
            computer_move()

def computer_move():
    global choices_count, computer_choices_count
    available_moves = [(i, j) for i in range(3) for j in range(3) if buttons[i][j]['text'] == ""]
    if available_moves:
        row, col = random.choice(available_moves)
        buttons[row][col]['text'] = "O"
        choices_count += 1
        computer_choices_count += 1
        check_winner("O")

def check_winner(player):
    global your_score, computer_score
    for i in range(3):
        # Check rows
        if all(buttons[i][j]['text'] == player for j in range(3)):
            show_winner(player)

        # Check columns
        if all(buttons[j][i]['text'] == player for j in range(3)):
            show_winner(player)

    # Check diagonals
    if all(buttons[i][i]['text'] == player for i in range(3)):
        show_winner(player)
    if all(buttons[i][2 - i]['text'] == player for i in range(3)):
        show_winner(player)

    # Check for a tie
    if choices_count == 9:
        show_tie()

def show_winner(player):
    global your_score, computer_score
    if player == "X":
        your_score += 1
        result_label.config(text="X wins!")
    else:
        computer_score += 1
        result_label.config(text="O wins!")

    update_score()
    reset_board()

def show_tie():
    result_label.config(text="It's a tie!")
    reset_board()

def reset_board():
    global choices_count
    for i in range(3):
        for j in range(3):
            buttons[i][j]['text'] = ""
    choices_count = 0
    update_score()

def update_score():
    score_label.config(text=f"You: {your_score}  Computer: {computer_score}")

# Bind button clicks
for i in range(3):
    for j in range(3):
        buttons[i][j].config(command=lambda row=i, col=j: on_button_click(row, col))

root.mainloop()
