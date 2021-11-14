import os 

def print_board(locations):
    for i in range(len(locations)):
        for j in range(len(locations[i])):
            if j == 2:
                print(' ' + locations[i][j] + ' ')
                if i != 2:
                    print('- - - - - -')
            else:
                print(' ' + locations[i][j] + ' |', end='')

def input_check(player_input, locations):
    if player_input == None or player_input == '':
        return False, 'Player has not provided an input.'
    if ',' not in player_input:
        return False, 'Player did not input in correct format.'
    
    player_input = player_input.split(',')
    for i in range(len(player_input)):
        if player_input[i] ==None or player_input[i] == '':
            return False, 'Player did not include input for the coordinate with index ' + str(i) +'.'
        if not player_input[i].isdigit():
            return False, 'Player input non-numeric character for the coordinate with index ' + str(i) + '.'
        if int(player_input[i]) > 3 or int(player_input[i]) < 1:
            return False, 'Player put in value outside the accepted numeric range for coordinate with index ' + str(i) + '.'

    if locations[int(player_input[0]) - 1][int(player_input[1]) - 1] != ' ':
        return False, 'That position is already filled.' 
    return True, player_input

def player_1_go(locations):
    count = 0
    player_input = input('Player 1 please enter where you want to place a token (between 1-3): ')
    check = input_check(player_input, locations)
    while not check[0]:
        if check[1] != 'That position is already filled.':
            count += 1

        if count >= 3:
            help()
            count = 0
        player_input = input(check[1] + ' Please try again: ')
        check = input_check(player_input, locations)

    player_input = check[1]
    locations[int(player_input[0]) - 1][int(player_input[1]) - 1] = 'x'

    return locations

def player_2_go(locations):
    count = 0
    player_input = input('Player 2 please enter where you want to place a token (between 1-3): ')
    check = input_check(player_input, locations)
    while not check[0]:
        if check[1] != 'That position is already filled.':
            count += 1

        if count >= 3:
            help()
            count = 0
        player_input = input(check[1] + ' Please try again: ')
        check = input_check(player_input, locations)

    player_input = check[1]
    locations[int(player_input[0]) - 1][int(player_input[1]) - 1] = 'o'

    return locations

def win_check(locations):
    # Row check
    for i in locations:
        if i.count('x') == len(i):
            return True, 'Player 1'
        elif i.count('o') == len(i):
            return True, 'Player 2'
    
    # Diagonal check
    if (locations[0][0] == locations[1][1] and locations[0][0] == locations[2][2] and locations[1][1] == locations[2][2]) or (locations[0][2] == locations[1][1] and locations[0][2] == locations[2][0] and locations[1][1] == locations[2][0]):
        if locations[1][1] == 'x':
            return True, 'Player 1'
        elif locations[1][1] == 'o':
            return True, 'Player 2'
    
    # Column check 
    for j in range(len(locations[0])):
        if locations[0][j] == locations[1][j] and locations[0][j] == locations[2][j]:
            if locations[0][j] == 'x':
                return True, 'Player 1'
            elif locations[0][j] == 'o':
                return True, 'Player 2'
    
    # move_bool = True
    for i in locations:
        if ' ' not in i:
            move_bool = False
            break
        else: 
            move_bool = True

    if move_bool == False:
        return True, 'There are no more moves available.'

    return False, ''

def help():
    print()
    print('INSTRUCTIONS FOR PLAY:')
    print('#1 - Players must input their desired square in the form "a,b" where a is the row and b is the column')
    print('#2 - Players must input their desired square using numerical characters and not letters or special characters i.e. a,e,i,o,u, or !,£,$,%')
    print('#3 - Player 1 goes first and is represented by \'x\' and player 2 goes second and is represented by \'o\'')
    print()

def main():
    board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

    game_over = False

    while not game_over:
        game_over, winner = win_check(board)
        if game_over: 
            break
        print_board(board)
        player_1_go(board)
        os.system('cls')
        game_over, winner = win_check(board)
        if game_over: 
            break
        print_board(board)
        player_2_go(board)
        os.system('cls')
    
    print_board(board)
    if winner == 'There are no more moves available.':
        print('There are no more moves available.')
    else:
        print(winner + ' has won!')

if __name__ == '__main__':
    main()