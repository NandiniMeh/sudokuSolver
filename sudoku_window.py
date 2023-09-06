import tkinter as tk
from tkinter import messagebox
import solver
import utils

# Global variable to hold all the entry widgets
entries = []

# Function to solve the Sudoku given by the user in the GUI


def solve_gui():
    # Initialize an empty 9x9 board
    board = [[0] * 9 for _ in range(9)]

    # Read the values entered by the user into the board
    for i in range(9):
        for j in range(9):
            value = entries[i][j].get()
            if value:
                board[i][j] = int(value)

    # Solve the board
    if solver.solve(board):
        # If solved, update the empty cells with the solution in green color
        for i in range(9):
            for j in range(9):
                if entries[i][j].get() == "":
                    entries[i][j].delete(0, tk.END)
                    entries[i][j].insert(tk.END, board[i][j])
                    entries[i][j].config(fg="green")
    else:
        # If no solution, show an error message
        messagebox.showerror("Error", "No solution exists for this Sudoku!")

# Function to solve the puzzle if the player gets it wrong


def solve_puzzle_player_lost():
    # Deep copy the original puzzle
    board = [row.copy() for row in original_puzzle]

    # Solve the board
    if solver.solve(board):
        # If solved, update the incorrect or empty cells with the solution in green color
        for i in range(9):
            for j in range(9):
                if entries[i][j].get() != str(original_puzzle[i][j]) or original_puzzle[i][j] == 0:
                    entries[i][j].delete(0, tk.END)
                    entries[i][j].insert(tk.END, board[i][j])
                    entries[i][j].config(fg="green")
    else:
        # If no solution, show an error message
        messagebox.showerror("Error", "No solution exists for this Sudoku!")

# Function to clear the board of any values and set color to black


def clear_board():
    for i in range(9):
        for j in range(9):
            entries[i][j].config(state="normal")
            entries[i][j].delete(0, tk.END)
            entries[i][j].config(fg="black")

# Function to provide a new puzzle to the user


def give_puzzle():
    clear_board()  # Clear the board
    board = solver.generate_puzzle()
    global original_puzzle
    original_puzzle = [[0] * 9 for _ in range(9)]

    # Display the new puzzle on the board
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                entries[i][j].insert(tk.END, board[i][j])
                entries[i][j].config(fg="red", state="readonly")
                original_puzzle[i][j] = board[i][j]
            else:
                entries[i][j].config(state="normal")

# Function to check the user's solution


def check_solution():
    board = [[0] * 9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            value = entries[i][j].get()
            if value:
                board[i][j] = int(value)

    # Check if the solution is correct
    if utils.is_solved(board):
        messagebox.showinfo("Info", "Congratulations! Correct solution.")
    else:
        messagebox.showerror("Error", "Incorrect solution! Try again.")

# Main function to open the Sudoku GUI window


def open_sudoku(root, mode):
    root.withdraw()
    sudoku_window = tk.Toplevel(root)
    sudoku_window.title("Sudoku Solver")
    sudoku_window.geometry("600x600")

    frame = tk.Frame(sudoku_window)
    frame.pack(pady=10, padx=10)

    global entries
    # Create the Sudoku grid using Entry widgets
    entries = [[tk.Entry(frame, width=2, font=('Mono', 24), justify='center', fg="black")
                for j in range(9)] for i in range(9)]
    for i in range(9):
        for j in range(9):
            entries[i][j].grid(row=i, column=j, padx=1, pady=1, sticky="nsew")
            if i % 3 == 2:
                entries[i][j].grid_configure(pady=(1, 4))
            if j % 3 == 2:
                entries[i][j].grid_configure(padx=(1, 4))

    # Depending on the mode, display relevant buttons
    if mode == "puzzle":
        puzzle_button = tk.Button(
            sudoku_window, text="Give Me a Puzzle", command=give_puzzle)
        puzzle_button.pack(pady=10)
        check_button = tk.Button(
            sudoku_window, text="Check Solution", command=check_solution)
        check_button.pack(pady=10)
        solution_button = tk.Button(
            sudoku_window, text="Give Solution", command=solve_puzzle_player_lost)
        solution_button.pack(pady=10)
    else:
        solve_button = tk.Button(
            sudoku_window, text="Solve My Sudoku", command=solve_gui)
        solve_button.pack(pady=10)

    # Define the action on window close
    def on_closing():
        sudoku_window.destroy()
        root.deiconify()

    sudoku_window.protocol("WM_DELETE_WINDOW", on_closing)

    sudoku_window.mainloop()

# Entry functions for different modes


def open_for_puzzle(root):
    open_sudoku(root, "puzzle")


def open_for_solve(root):
    open_sudoku(root, "solve")
