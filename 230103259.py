size = 3
board= list(range(1,10))

def display_board():
    print('_' * size * 4)
    for i in range(size):
        print((' ' * size + '|') * 3)
        print('', board[i*3] , '|', board[1 + i*3] , '|', board[2+i*3], '|')
        print(('_' * size + '|') * 3)
def code(index,var):
    if index < 1 or index>9 or board[index-1] in ('X', 'O'):
        return False
    board[index-1] = var
    return True 
def checkwin():
    win = False
    wincomb = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for i in wincomb: 
        if board[i[0]-1] == board[i[1]-1] and board[i[0]-1]==board[i[2]-1]:
            win = board[i[0]-1]
    return win

def start_game():
    current = 'X'
    step = 1
    display_board()
    while step<=9 and checkwin() == False:
        if ft_player.upper() == 'X':
            if current == 'X': 
                index = input(f'{first_player}, your turn. Choose position from 1 to 9: ')
            else:
                index = input(f'{second_player}, your turn. Choose position from 1 to 9: ')
        else:
            if current == 'X':
                index = input(f'{second_player}, your turn. Choose position from 1 to 9: ')
            else:
                index = input(f'{first_player}, your turn. Choose position from 1 to 9: ')
        if index.isdigit():
            if code(int(index),current):
                print('A good move')
                step+=1
                display_board()
                if step%2 == 0:
                    current = 'O'
                else:
                    current = 'X'
            else:
                print('wrong number! Repeat,please!')
        else:
            print('incorrectly entered')
    if checkwin() == False:
        print('Draw')
        game_cnt[2]+=1
    else:
        if checkwin() == ft_player.upper():
            print(f'{first_player} win')
            game_cnt[0]+=1
        else:
            print(f'{second_player} win')
            game_cnt[1]+=1
print('Welcome to the tic-tac-toe game')
first_player = input('First_player name: ')
second_player = input('Second_player name: ')
while True:
    ft_player = input(f'{first_player}: X or O? ')
    if ft_player.upper() == 'X':
        sc_player = 'O'
        print(f'{second_player} is O')
        break
    elif ft_player.upper() == 'O':
        sc_player = 'X'
        print(f'{second_player} is X')
        break
    else:
        print('please, try again!')
game_cnt = [0,0,0]
start_game()
want = True
while want:
    if input('Do you want to play one more? ').lower() == 'no':
        want = False
    else:
        board= list(range(1,10))
        if ft_player.upper() == 'X':
            ft_player = 'O'
            sc_player = 'X'
        else:
            ft_player = 'X'
            sc_player = 'O'   
        start_game()
print(f"{first_player}'s score: {game_cnt[0]} \n{second_player}'s score: {game_cnt[1]} \nDraw score: {game_cnt[2]}")
