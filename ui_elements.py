import tkinter as tk

def create_ui(window):
    window.configure(bg="#e6f7ff")  # светлый фон

    frame = tk.Frame(window, bg="#e6f7ff", bd=5, relief="ridge")  # обрамление поля
    frame.pack(pady=10)

    info_label = tk.Label(window, text="Выберите, за кого играть", font=("Arial", 14), bg="#f0f0f0", fg="#333")
    info_label.pack(pady=5)

    score_label = tk.Label(window, text="Счёт - X: 0 | O: 0", font=("Arial", 12), bg="#f0f0f0", fg="#333")
    score_label.pack(pady=5)

    reset_button = tk.Button(window, text="Сбросить игру", font=("Arial", 10), bg="#dddddd", relief="groove", cursor="hand2")
    reset_button.pack(pady=5)

    symbol_frame = tk.Frame(window, bg="#f0f0f0")
    symbol_frame.pack(pady=10)

    return {
        "frame": frame,
        "info_label": info_label,
        "score_label": score_label,
        "reset_button": reset_button,
        "symbol_frame": symbol_frame
    }

