from IPython.display import clear_output
import random

def display_board(board):
    
    '''Write a function that can print out a board. Set up your board as a list, 
    where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 
    board representation.'''
    
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-|-|-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-|-|-')
    print(board[7] + '|' + board[8] + '|' + board[9])


def player_input():
    
    '''Write a function that can take in a player input and assign their marker as 'X' or 'O'. 
    Think about using while loops to continually ask until you get a correct answer.'''
    
    player1 = ''
    player2 = ''
    
    while True:
        player1 = input('Player1, please choose your marker: (X / O)').upper()
        if player1 in set('XO'):
            if player1 == 'X':
                player2 = 'O'
            else:
                player2 = 'X'
            break
    
    print(f'Player 1 marker: {player1} \nPlayer 2 marker: {player2}')
    return player1,player2

        

def place_marker(board, marker, position):
    '''Write a function that takes in the board list object, a marker ('X' or 'O'), 
    and a desired position (number 1-9) and assigns it to the board'''
    board[position] = marker


def win_check(board, mark):
    
    '''Write a function that takes in a board and a mark (X or O) 
    and then checks to see if that mark has won.'''
    
    if mark == board[1] == board[2] == board[3]:
        return True
    elif mark == board[4] == board[5] == board[6]:
        return True
    elif mark == board[7] == board[8] == board[8]:
        return True
    elif mark == board[1] == board[4] == board[7]:
        return True
    elif mark == board[2] == board[5] == board[8]:
        return True
    elif mark == board[3] == board[6] == board[9]:
        return True
    elif mark == board[1] == board[5] == board[9]:
        return True
    elif mark == board[3] == board[5] == board[7]:
        return True
    else:
        return False


def choose_first():
    '''Write a function that uses the random module to randomly decide 
    which player goes first. You may want to lookup random.randint() 
    Return a string of which player went first.'''
    
    return random.choice(['Player 1', 'Player2'])


def space_check(board, position):
    ''' Write a function that returns a boolean indicating whether 
    a space on the board is freely available.'''
    return board[position] == " "


def full_board_check(board):
    '''Write a function that checks if the board is full and 
    returns a boolean value. True if full, False otherwise.'''
    return " " not in set(board)


def player_choice(board):
    '''Write a function that asks for a player's next position 
    (as a number 1-9) and then uses the function from step 6 to check 
    if it's a free position. If it is, then return the position for later use.'''

    nxt_position = 0

    while nxt_position not in [1,2,3,4,5,6,7,8,9] or not space_check(board , nxt_position):
        nxt_position = int(input('What is your next position?: '))

    return nxt_position
    
        


def replay():
    '''Write a function that asks the player if they want to play again 
    and returns a boolean True if they do want to play again.'''
    
    response = input("Do you want to play again? (Y/N) ")
    
    return response.upper() == 'Y'

#------------------------------------------------------------------

print('Welcome to Tic Tac Toe!')


while True:
    
    board = list('#' + ' '*9)
    player1 , player2 = player_input()
    
    turn = choose_first()
    print(f'{turn} will go first')
    
    ready = input('Ready to play?: (Y/N)').upper()
    game_on = False
    
    if ready == 'Y':
        game_on = True
    
    while game_on:
        
        if turn == "Player 1":
        
            display_board(board)
            position = player_choice(board)
            place_marker(board , player1 , position)
            
            if win_check(board , player1):
                display_board(board)
                print("Player 1 won!")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("Draw!")
                    break
                else:
                    turn = 'Player 2'
        else:
            
            display_board(board)
            position = player_choice(board)
            place_marker(board , player2 , position)
            
            if win_check(board , player1):
                display_board(board)
                print("Player 2 won!")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("Draw!")
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        print("Thanks for playing!")
        break
    
    

    
    
    
