
import tkinter as tk
from ui_elements import create_ui
from game_board import init_game


def main():
    window = tk.Tk()
    window.title('Крестики-нолики')
    window.geometry('320x400')

    elements = create_ui(window)
    init_game(window, elements)

    window.mainloop()


if __name__ == "__main__":
    main()





