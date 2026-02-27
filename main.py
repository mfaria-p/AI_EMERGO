import tkinter as tk
from tkinter import messagebox

class BoardGameGUI:
    def __init__(self, root, board_size=8):
        self.root = root
        self.root.title("Adversarial Search: Two-Player Board Game")
        self.board_size = board_size
        self.buttons = {}
        
        # Initialize the Game State (Simple 2D List)
        # 0: Empty, 1: Player 1, 2: Player 2
        self.board_state = [[0 for _ in range(board_size)] for _ in range(board_size)]
        
        self.create_widgets()

    def create_widgets(self):
        """Creates the grid of buttons representing the board."""
        self.main_frame = tk.Frame(self.root, padx=20, pady=20)
        self.main_frame.pack()

        for r in range(self.board_size):
            for c in range(self.board_size):
                btn = tk.Button(
                    self.main_frame, 
                    text="", 
                    width=4, 
                    height=2, 
                    command=lambda r=r, c=c: self.handle_click(r, c),
                    bg="white"
                )
                btn.grid(row=r, column=c, sticky="nsew")
                self.buttons[(r, c)] = btn

        # Status Label
        self.status_label = tk.Label(self.root, text="Player 1's Turn", font=("Arial", 12))
        self.status_label.pack(pady=10)

    def handle_click(self, r, c):
        """Handle human moves."""
        if self.board_state[r][c] == 0:
            # Basic visual feedback for testing
            self.board_state[r][c] = 1 
            self.buttons[(r, c)].config(text="X", fg="blue", state="disabled")
            print(f"Move registered at: ({r}, {c})")
            # Here you would trigger the AI move logic
        else:
            messagebox.showwarning("Invalid Move", "This cell is already occupied!")

if __name__ == "__main__":
    root = tk.Tk()
    # You can change board_size here dynamically
    app = BoardGameGUI(root, board_size=6) 
    root.mainloop()