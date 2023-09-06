import tkinter as tk
from sudoku_window import open_for_puzzle, open_for_solve
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Main Menu")
root.geometry("600x600")
root.configure(bg='white')

img = Image.open("logo.png")

# Resize the image
desired_size = (150, 150)  # Adjust width and height as needed
img = img.resize(desired_size)

# Convert the image to PhotoImage
logo = ImageTk.PhotoImage(img)

# Place the logo on the window
logo_label = tk.Label(root, image=logo, bg="white")
logo_label.pack(pady=(100, 0))  # Adjust padding as required


# Styling button 1
give_puzzle_button = tk.Button(
    root, text="Give Me a Puzzle", command=lambda: open_for_puzzle(root),
    font=('Mono', 20), bg='lightgray', fg='black', borderwidth=0, relief="flat"
)
give_puzzle_button.pack(pady=(30, 10), ipadx=20, ipady=10)

# Styling button 2
solve_puzzle_button = tk.Button(
    root, text="Solve My Puzzle", command=lambda: open_for_solve(root),
    font=('Mono', 20), bg='lightgray', fg='black', borderwidth=0, relief="flat"
)
solve_puzzle_button.pack(pady=(10, 30), ipadx=20, ipady=10)


root.mainloop()
