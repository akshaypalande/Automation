"""
@Author: Akshay Palande
@Date: 2022-05-16 2:00:00
@Last Modified By: Akshay Palande
@Last Modified Date: 2022-05-16 2:00:00
@Title: TicTacToe

"""

import random

def printBoard(board):
    """
    Description:
        This method is used for printing a game board after each moves.
    Parameter:
        board is here the size of the board used for creating game board.
    """
    print()
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('__|___|__')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('__|___|__')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])


def playerInput():
    """
    Description:
        This function is used for choosing 'X' or 'O' by the user.
        if user choose 'X' then computer is set to be 'O' and vice versa.
    
    Return:
        Mark 'X' or 'O' for player and computer.
    """
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player1: Choose X or O: ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def get_turn():
    """
    Description:
        This function is used for getting turn that who will start game first.
    Return:
        Either player or computer turn.
    """
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player'
    else:
        return 'Computer'


def space_check(board, position):
    """
    Description:
        This function is used for checking the space on the board before marking 
        'x' and 'O' on the board.
    Parameter:
        it takes board as a current board and it also takes the
        position is the index of board were player is trying to put Letter.
        if that position is empty it returns true.
    Return:
        True  if the space on the board is Empty.
    """
    return board[position] == ' '


def full_board_check(board):
    """
    Description:
        This function is used for checking if the gameboard is full or or not.
        All the positions are filled with 'X' and 'O'
    Parameter:
        it takes current board and using for loop it start checking all the position on board.
    Return:
        True if the space on the game board is full.
        otherwise it will return false.
    """

    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

# getting player position for moves

def player_position(board):
    """
    Description:
        This function is used for getting player position where he wants to put letter.
    Parameter:
        it takes current board  and it will check the conditions, space is free or not on that position.
    Return:
        It will return position number if the space on that position is free.
    """
    try:
        position = 0
        while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
            position = int(input("Choose a Position : (1-9) "))
            return position
           
    except ValueError:
        print("Enter a Integer Input only (1-9) ")
    except Exception as e:
        print(e)
        
            

#getting computer moves and position

def winning(mark,board):
    """
    Description:
        This function is used for getting computer winning position
    Parameter:
        it takes 'X' or 'O' mark and temporary gameboard to find the winning place.
    Return:
        It will return  True if it is a winning move else false.
    """
    winning_place = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for win_place in winning_place:
        if board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == mark:
            return True


def win_move(i,board,mark):
    """
    Description:
        This function is used for getting win move for computer.
    Parameter:
        it takes i as as position for computer and 'X' or 'O' mark 
        and current gameboard to find the winning place.
    Return:
        It will return true  if cpu entered position is a winning move.
    """

    temp_board = list(board)
    temp_board[i] = mark
    if winning(mark,temp_board):
        return True
    else:
        return False


def computer_position(computer_marker, player_marker , board):
    """
    Description:
        This function is used for getting computer posing for marking letter 'X' or 'O'.
    Parameter:
        it takes 'X' or 'O' mark and current  gameboard  and player mark to find the position.
    Return:
        It will return position for computer to mark on the board
    """
    for i in range(1,10):
        if board[i] == ' ' and win_move(i,board,computer_marker):
            return i
    for i in range(1,10):
        if board[i] == ' ' and win_move(i,board,player_marker):
            return i
    for i in [5,1,7,3,2,9,8,6,4]:
        if board[i] == ' ':
            return i


def place_marker(board, marker, position):
    """
    Description:
        This function is used for marking Letter 'X' or 'O' in the game board.
    Parameter:
        board is the current game board of the game.
        marker is the player mark or the computer mark.
        position contains position of a player or a computer they want to mark or move. 
    """
    board[position] = marker


def check_win(board, mark):
    """
    Description:
        This function is used for checking if a player or a computer wins.
    Parameter:
        it takes 'X' or 'O' mark and board for checking win or not.
    Return:
        It will return  True if it is a winning player or computer wins.
    """

    return ((board[1] == board[2] == board[3] == mark) or # first row check
            (board[4] == board[5] == board[6] == mark) or # second row check
            (board[7] == board[8] == board[9] == mark) or # third row check
            (board[1] == board[4] == board[7] == mark) or # first column check 
            (board[2] == board[5] == board[8] == mark) or # second column check
            (board[3] == board[6] == board[9] == mark) or # third column check
            (board[1] == board[5] == board[9] == mark) or # diagonal check
            (board[3] == board[5] == board[7] == mark))


def replay():
    """
    Description:
        This function is used giving option to player for a replay match.
    Return:
        It will return  true if choice is yes else false.
    """
    try:
        choice = input("Play Again? Enter Yes or No : ").lower()
        return choice == 'yes'
    
    except Exception as e:
        print(e)
        replay()
    

if __name__ == "__main__":
    try:
        while True:   

            print("Welcome To Tic Tac Toe Game")
            # creating tic tac toe game board and skiping the first index[0] for further use
            game_board = [' '] * 10
            # setting marker for computer and a player by taking input from player
            player_marker, computer_marker = playerInput()
            # getting turn who will go first
            turn = get_turn()
            print(turn + ' will go first')

            # varible that indicate game has started
            game_started = True

            while game_started:
                if turn == 'Player':  # checking if turn is for player
                    printBoard(game_board)
                    position = player_position(game_board)  # getting positions on the board
                    # placing the marker on the user specified position on board
                    place_marker(game_board, player_marker, position)

                    if check_win(game_board, player_marker):
                        printBoard(game_board)
                        print("Player1 has won!!")
                        game_started = False              # game will exit

                    else:
                        if full_board_check(game_board):
                            printBoard(game_board)
                            print(" Game Is Tie!!")
                            game_started = False
                        else:
                            turn = 'Computer'

                # computern turn 
                else:
                    position = computer_position(computer_marker,player_marker,game_board)  # getting positions on the board for computer
                    # placing the marker on the user specified position on board
                    place_marker(game_board, computer_marker, position)

                    if check_win(game_board, computer_marker):
                        printBoard(game_board)
                        print("Computer has won!!")
                        game_started = False              # game will exit

                    else:
                        if full_board_check(game_board):
                            printBoard(game_board)
                            print(" Game Is Tie!!")
                            game_started = False
                        else:
                            turn = 'Player'

            if not replay(): # giving player an option to play another game
                break

    except Exception as e:
        print(e)