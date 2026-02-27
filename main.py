# --- TEST LOOP ---
from core.emergo import EmergoGame

if __name__ == "__main__":
    game = EmergoGame(size=5) # Smaller board for quick testing
    
    while True:
        game.display()
        moves = game.get_legal_moves()
        
        print("\nLegal Moves:")
        for i, m in enumerate(moves):
            print(f"{i}: {m[0]} -> {m[1]}")
            
        choice = input("\nSelect move index (or 'q' to quit): ")
        if choice.lower() == 'q':
            break
            
        try:
            idx = int(choice)
            game.apply_move(moves[idx])
        except:
            print("Invalid input!")