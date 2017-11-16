game_board = []

board_size = int(input("What size should the board be?"))
ship_count = int(input("How many ships are we playing with?"))


for x in range(board_size):
    game_board.append(["O"] * board_size )
print(len(game_board))
print (game_board)

def print_board(board):
    for row in board:
        print (" ".join(row))

print_board(game_board)
