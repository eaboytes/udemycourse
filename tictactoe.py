import random

def display_board(board):
    board[0]='#'
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def player_input():
    pl1_marker = ' '
    while not (pl1_marker == 'X' or pl1_marker == 'O'):
        pl1_marker=input("Player 1, Please choose whether you would like to use X or O as your marker").upper()
    if pl1_marker == "X":
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return (
        (board[1] == mark and board[2] == mark and board [3] == mark) or
        (board[4] == mark and board[5] == mark and board [6] == mark) or
        (board[7] == mark and board[8] == mark and board [9] == mark) or
        (board[1] == mark and board[4] == mark and board [7] == mark) or
        (board[2] == mark and board[5] == mark and board [8] == mark) or
        (board[3] == mark and board[6] == mark and board [9] == mark) or
        (board[1] == mark and board[5] == mark and board [9] == mark) or
        (board[3] == mark and board[5] == mark and board [7] == mark)
    )

def choose_first():
    return random.randint(1,2)

def space_check(board, position):
    return board[position] is ' '

def full_board_check(board):
    for i in range(1,10):
        if board[i] == ' ':
            return False
    return True

def player_choice(board):
    position = 0
    while space_check(board, position) is False:
        position = int(input("Where would you like to place your marker. Please choose an unoccupied position 1-9"))
        if not (position in range(1,10)):
            position = 0
        else:
            continue
    return position

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')

while True:
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    pl1marker, pl2marker = player_input()
    turn = choose_first()
    print("First player is " + str(turn))
    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 1:
            # Player 1 Turn
            display_board(board)
            print('Go Player 1! \n')
            position = player_choice(board)
            place_marker(board, pl1marker, position)
            if win_check(board, pl1marker):
                display_board(board)
                print('Congratulations! Player 1, You have won the game!')
                game_on = False
            elif full_board_check(board):
                display_board(board)
                print('Tie Game')
                game_on = False
            else:
                turn = 2
        if turn == 2:
            # Player2's turn.
            display_board(board)
            print('Go Player 2! \n')
            position = player_choice(board)
            place_marker(board, pl2marker, position)
            if win_check(board, pl2marker):
                display_board(board)
                print('Congratulations! Player 2, You have won the game!')
                game_on = False
            elif full_board_check(board):
                display_board(board)
                print('Tie Game')
                game_on = False
            else:
                turn = 1
                # pass

    if not replay():
        break