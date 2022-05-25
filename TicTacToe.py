from IPython.display import clear_output

def display_board(board):
    clear_output()
    
    print('    |      |     ')
    print('  ' + board[7]+ ' |   '+ board[8] + '  | ' + board[9])
    print('    |      |     ')
    print('----|------|-----')
    print('    |      |     ')
    print('  ' + board[4]+ ' |   '+ board[5] + '  | ' + board[6])
    print('    |      |     ')
    print('----|------|-----')
    print('    |      |     ')
    print('  ' + board[1]+ ' |   '+ board[2] + '  | ' + board[3])
    print('    |      |     ')

def player_input():
    
    player1_marker = input('Player 1, please pick X or O: ').upper()
    
    if player1_marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board,marker,position):
    board[position] = marker

def win_check(board,mark):
    return ((board[7] == mark and board[8] ==mark and board[9]== mark) or
    (board[4] == mark and board[5] == mark and board[6]== mark) or
    (board[1] == mark and board[2] == mark and board[3]== mark) or
    (board[7] == mark and board[4] == mark and board[1]== mark) or
    (board[8] == mark and board[5] == mark and board[2]== mark) or
    (board[9] == mark and board[6] == mark and board[3]== mark) or
    (board[1] == mark and board[5] == mark and board[9]== mark) or
    (board[7] == mark and board[5] == mark and board[3]== mark))
    
import random

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    
    return board[position] == ' '

def full_board_check(board):
    
    for x in range(1,10):
        if space_check(board,x):
            return False 
    return True

def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose a position: (1-9) '))
        
    return position

def replay():
    
    choice = input('Play again? Enter Yes or No: ').lower().startswith('y')

while True:
    
    print('Welcome to Tic Tac Toe!')
    
    play_game = input('Are you ready to play? ')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
        
    game_board = [' ']*10
        
    player1_marker,player2_marker = player_input()
    
    turn = choose_first()
    
    print(turn + ' will go first.')
    
    while game_on == True:
        
        if turn == 'Player 1':
            
            display_board(game_board)
            
            position = player_choice(game_board)
            
            place_marker(game_board,player1_marker,position)
            
            if win_check(game_board, player1_marker) == True:
                display_board(game_board)
                print('Player 1 wins!')
                game_on = False
                
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print('Tie Game!')
                    break
                else:
                    turn = 'Player 2'
                    
        elif turn == 'Player 2':
            
            display_board(game_board)
            
            position = player_choice(game_board)
            
            place_marker(game_board,player2_marker,position)
            
            if win_check(game_board,player2_marker) == True:
                display_board(game_board)
                print('Player 2 wins!')
                game_on = False
                
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print('Tie Game!')
                    break
                else:
                    turn = 'Player 1'
        else:
            print('Houston, we have a problem!')
            
    if not replay():
        break
                