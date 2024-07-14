import tkinter as tk
from tkinter import messagebox
import random

def roll_dice():
    number = random.randint(1, 6)
    messagebox.showinfo("Dice Roll", f"You rolled: {number}")

def main():
    root = tk.Tk()
    root.title("Dice Roller")

    window_size = 110
    window_width = window_size
    window_height = window_size
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    roll_button = tk.Button(root, text="Roll the Dice", command=roll_dice)
    roll_button.pack(pady=10)

    exit_button = tk.Button(root, text="Exit", command=root.quit)
    exit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
