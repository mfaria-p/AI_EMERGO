class EmergoGame:
    def __init__(self, size=7):
        self.size = size
        # Grid: each cell is a list. Bottom piece at index 0, top at index -1.
        self.board = [[[] for _ in range(size)] for _ in range(size)]
        self.current_player = 'W'
        self.setup_board()

    def setup_board(self):
        """Standard Emergo setup: White on bottom rows, Black on top."""
        # Simple test setup: 2 rows for each
        for x in range(self.size):
            self.board[0][x] = ['W']
            self.board[self.size-1][x] = ['B']

    def display(self):
        """Prints the board to the console."""
        print("\n   " + "  ".join(str(i) for i in range(self.size)))
        for r in range(self.size):
            row_str = f"{r} "
            for c in range(self.size):
                stack = self.board[r][c]
                if not stack:
                    row_str += "[ ]"
                else:
                    # Show top piece and stack height
                    row_str += f"[{stack[-1]}{len(stack)}]"
            print(row_str)
        print(f"\nTurn: {self.current_player}")

    def get_legal_moves(self):
        """Finds all moves for current player. For testing, we'll do simple 1-step moves."""
        moves = []
        for r in range(self.size):
            for c in range(self.size):
                stack = self.board[r][c]
                if stack and stack[-1] == self.current_player:
                    # Check 8 neighbors
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if dr == 0 and dc == 0: continue
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < self.size and 0 <= nc < self.size:
                                # In Emergo, you can move to empty or merge with friendly
                                moves.append(((r, c), (nr, nc)))
        return moves

    def apply_move(self, move):
        start, end = move
        # Move the whole stack
        self.board[end[0]][end[1]] = self.board[start[0]][start[1]]
        self.board[start[0]][start[1]] = []
        self.current_player = 'B' if self.current_player == 'W' else 'W'
