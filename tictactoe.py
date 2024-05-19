top = ['_', '_', '_']
mid = ['_', '_', '_']
bot = ['_', '_', '_']


game_is_on = False

def print_board():
    print("_________________")
    print(top)
    print(mid)
    print(bot)

def top_left(player):
    if top[0] != '_':
        print('Spot occupied, pick another spot')
        return False
    top[0] = 'X' if player == '1' else 'O'
    return True

def top_mid(player):
    if top[1] != '_':
        print('Spot occupied, pick another spot')
        return False
    top[1] = 'X' if player == '1' else 'O'
    return True

def top_right(player):
    if top[2] != '_':
        print('Spot occupied, pick another spot')
        return False
    top[2] = 'X' if player == '1' else 'O'
    return True

def mid_left(player):
    if mid[0] != '_':
        print('Spot occupied, pick another spot')
        return False
    mid[0] = 'X' if player == '1' else 'O'
    return True

def mid_mid(player):
    if mid[1] != '_':
        print('Spot occupied, pick another spot')
        return False
    mid[1] = 'X' if player == '1' else 'O'
    return True

def mid_right(player):
    if mid[2] != '_':
        print('Spot occupied, pick another spot')
        return False
    mid[2] = 'X' if player == '1' else 'O'
    return True

def bot_left(player):
    if bot[0] != '_':
        print('Spot occupied, pick another spot')
        return False
    bot[0] = 'X' if player == '1' else 'O'
    return True

def bot_mid(player):
    if bot[1] != '_':
        print('Spot occupied, pick another spot')
        return False
    bot[1] = 'X' if player == '1' else 'O'
    return True

def bot_right(player):
    if bot[2] != '_':
        print('Spot occupied, pick another spot')
        return False
    bot[2] = 'X' if player == '1' else 'O'
    return True

def player_turn(player):
    player_input = input(f'Player {player}, which spot do you pick?: ').lower()
    return player_input

def check_winner():
    lines = [
        top, mid, bot,  # rows
        [top[0], mid[0], bot[0]],  # columns
        [top[1], mid[1], bot[1]],
        [top[2], mid[2], bot[2]],
        [top[0], mid[1], bot[2]],  # diagonals
        [top[2], mid[1], bot[0]]
    ]
    for line in lines:
        if line == ['X', 'X', 'X']:
            return '1'
        if line == ['O', 'O', 'O']:
            return '2'
    return None

commands = {
    'top left': top_left,
    'top mid': top_mid,
    'top right': top_right,
    'mid left': mid_left,
    'mid mid': mid_mid,
    'mid right': mid_right,
    'bot left': bot_left,
    'bot mid': bot_mid,
    'bot right': bot_right
}

print_board()
print("Welcome to tic tac toe, This game is for 2 players")
game_on = input("Start game? Yes or No : ").lower()
if game_on == 'yes':
    game_is_on = True

current_player = '1'
while game_is_on:
    player_input = player_turn(current_player)
    if player_input in commands:
        if commands[player_input](current_player):
            print_board()
            winner = check_winner()
            if winner:
                print(f'Player {winner} wins!')
                break
            if all(spot != '_' for row in [top, mid, bot] for spot in row):
                print('The game is a draw!')
                break
            current_player = '2' if current_player == '1' else '1'
    else:
        print('Invalid input, try again.')
