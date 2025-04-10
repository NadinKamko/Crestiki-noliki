
import tkinter as tk
from tkinter import messagebox


def init_game(window, elements):
    current_player = "X"
    scores = {"X": 0, "O": 0}
    buttons = []






    def reset_game():
        nonlocal current_player
        for row in buttons:
            for btn in row:
                btn.config(text="", state="normal")
        current_player = "X"
        elements["info_label"].config(text=f"Ходит игрок {current_player}")

    def update_score(player):
        scores[player] += 1
        elements["score_label"].config(text=f"Счёт - X: {scores['X']} | O: {scores['O']}")
        if scores[player] == 3:
            messagebox.showinfo("Игра окончена!", f"Игрок {player} выиграл серию из 3 побед!")
            scores["X"], scores["O"] = 0, 0
            elements["score_label"].config(text=f"Счёт - X: 0 | O: 0")

    def check_winner():
        for i in range(3):
            if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
                return True
            if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
                return True
        if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
            return True
        if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
            return True
        return False

    def check_draw():
        return all(buttons[i][j]['text'] != "" for i in range(3) for j in range(3))

    def on_click(row, col):
        nonlocal current_player
        if buttons[row][col]['text'] == "":
            buttons[row][col]['text'] = current_player
            if check_winner():
                update_score(current_player)
                messagebox.showinfo("Победа", f"Игрок {current_player} победил!")
                reset_game()
            elif check_draw():
                messagebox.showinfo("Ничья", "Ничья! Все клетки заполнены.")
                reset_game()
            else:
                current_player = "O" if current_player == "X" else "X"
                elements["info_label"].config(text=f"Ходит игрок {current_player}")

    def create_board():
        for i in range(3):
            row = []
            for j in range(3):
                btn = tk.Button(elements["frame"], text='', font=("Arial", 20), width=5, height=2,
                                command=lambda r=i, c=j: on_click(r, c))
                btn.grid(row=i, column=j)
                row.append(btn)
            buttons.append(row)

    def choose_symbol(symbol):
        nonlocal current_player
        current_player = symbol
        elements["info_label"].config(text=f"Ходит игрок {current_player}")
        elements["symbol_frame"].destroy()
        create_board()

    tk.Button(elements["symbol_frame"], text="Играть за X", command=lambda: choose_symbol("X"), width=12).grid(row=0, column=0, padx=5)
    tk.Button(elements["symbol_frame"], text="Играть за O", command=lambda: choose_symbol("O"), width=12).grid(row=0, column=1, padx=5)

    elements["reset_button"].config(command=reset_game)
