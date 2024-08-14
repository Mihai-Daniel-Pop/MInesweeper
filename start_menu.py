from tkinter import *

# Function to switch to difficulty selection screen
def show_difficulty_selection():
    # Clear the existing widgets on the root window
    for widget in root.winfo_children():
        widget.destroy()

    # Create a new label for the difficulty selection screen
    difficulty_label = Label(root, text="Select Difficulty", font=("Helvetica", 30, "bold"), bg="#000000", fg="#FFFFFF")
    difficulty_label.pack(pady=20)

    # Create buttons for difficulty selection
    easy_button = Button(root, text="Easy", font=("Helvetica", 20), command=lambda: start_game('Easy'))
    medium_button = Button(root, text="Medium", font=("Helvetica", 20), command=lambda: start_game('Medium'))
    hard_button = Button(root, text="Hard", font=("Helvetica", 20), command=lambda: start_game('Hard'))

    easy_button.pack(pady=10)
    medium_button.pack(pady=10)
    hard_button.pack(pady=10)

def start_game(difficulty):
    # This is where you'd start the game with the selected difficulty
    print(f"Starting game with {difficulty} difficulty")

# Main Window Setup
root = Tk()
root.configure(bg="#000000")
root.title("Minesweeper")
root.iconbitmap('D:/G/Minesweeper/minesweeper.ico')
root.geometry('1200x800')

# Create a label to serve as the banner
banner = Label(root, text="Minesweeper", font=("Helvetica", 40, "bold"), bg="#000000", fg="#FFFFFF")
banner.pack(pady=10)

# Create the "Start" button and center it in the window
start_button = Button(root, text="Start", font=("Helvetica", 20), command=show_difficulty_selection)
start_button.pack(pady=200)  # Adjust padding to position the button in the middle

# Center the label horizontally
banner.pack_configure(side=TOP, padx=10, pady=10)

root.mainloop()
