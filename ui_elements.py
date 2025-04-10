# ui_elements.py
import tkinter as tk

def create_ui(window):
    frame = tk.Frame(window)
    frame.pack(pady=10)

    info_label = tk.Label(window, text="Выберите, за кого играть", font=("Arial", 12))
    info_label.pack(pady=5)

    score_label = tk.Label(window, text="Счёт - X: 0 | O: 0", font=("Arial", 12))
    score_label.pack(pady=5)

    reset_button = tk.Button(window, text="Сбросить игру", font=("Arial", 10))
    reset_button.pack(pady=5)

    symbol_frame = tk.Frame(window)
    symbol_frame.pack(pady=10)

    return {
        "frame": frame,
        "info_label": info_label,
        "score_label": score_label,
        "reset_button": reset_button,
        "symbol_frame": symbol_frame
    }
