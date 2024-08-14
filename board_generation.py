from tkinter import *
import random

# Initialize the main application window
root = Tk()
root.configure(bg="#000000")
root.title("Minesweeper")
root.iconbitmap('D:\G\Minesweeper\minesweeper.ico')

# Define grid dimensions (e.g., 10x10 grid)
rows, cols = 10, 10

# Function to handle button clicks
def button_click(row, col):
    print(f"Button at Row {row+1}, Column {col+1} clicked!")

# Create a grid of buttons
buttons = []
for r in range(rows):
    row_buttons = []
    for c in range(cols):
        # Create each button with a command that includes its position
        button = Button(root, text=" ", width=3, height=1, bg="#FFFFFF", command=lambda r=r, c=c: button_click(r, c))
        button.grid(row=r, column=c)
        row_buttons.append(button)
    buttons.append(row_buttons)

# Run the application
root.mainloop()
