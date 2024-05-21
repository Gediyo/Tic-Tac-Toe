# @ author: Gediyon M. Girma
# Tic-Tac-Toe game human vs human

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # creates a list with " " (space) character

    def reset(self):
        self.board = [' ' for _ in range(9)] # resets the board

    def set_position(self, position, player):
        if self.board[position] == ' ':
            self.board[position] = player
            return True
        else:
            return False

    def check_win(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
                          (0, 4, 8), (2, 4, 6)]             # Diagonal

        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ' ':
                return self.board[condition[0]]
        return None

    def check_draw(self):
        return ' ' not in self.board

    def print_board(self):
        for i in range(3):
            print(self.board[i*3], '|', self.board[i*3 + 1], '|', self.board[i*3 + 2])
            if i < 2:
                print("---------")


def main():
    game = TicTacToe()
    current_player = 'X'

    while True:
        game.print_board()
        print(f"Player {current_player}'s turn.")

        position = int(input("Enter position (0-8): "))
        if position < 0 or position > 8:
            print("Invalid position! Position must be between 0 and 8.")
            continue

        if game.set_position(position, current_player):
            winner = game.check_win()
            if winner:
                game.print_board()
                print(f"Player {winner} wins!")
                break
            elif game.check_draw():
                game.print_board()
                print("It's a draw!")
                break
            else:
                current_player = 'O' if current_player == 'X' else 'X'  # switching player
        else:
            print("Position already taken!")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == 'yes':
        main()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    main()