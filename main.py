field = [[0 for i in range(3)] for i in range(3)]

def print_field(field):
    print('---')
    print('  1 2 3')
    for i in range(3):
        print(f'{i+1} ', end = '')
        for j in range(3):
            if field[i][j] == 0:
                print(f'- ', end = '')
            elif field[i][j] > 0:
                print(f'x ', end = '')
            elif field[i][j] < 0:
                print(f'o ', end = '')
        print()
    print('---')

def def_player(player):
    return 'x' if player > 0 else 'o'

def enter_cell(player):
    while True:
        try:
            i, j = map(int, input(f'Player "{def_player(player)}", enter your cell (col and row):').split())
            if 1 <= i <= 3 and 1 <= j <= 3:
                break
        except:
            continue
    return i - 1, j - 1

def check_field(field):
    result = False
    diag_1_sum, diag_2_sum = 0, 0
    for i in range(3):
        row_sum, col_sum = 0, 0
        for j in range(3):
            row_sum += field[i][j]
            col_sum += field[j][i]
            if i == j:
                diag_1_sum += field[i][j]
            if i + j == 2:
                diag_2_sum += field[i][j]
        result = abs(row_sum) == 3 or abs(col_sum) == 3
        if result:
            return result
    result = abs(diag_1_sum) == 3 or abs(diag_2_sum) == 3
    return result

def playing_field(field):
    player = 1
    for _ in range(9):
        while True:
            cell = enter_cell(player)
            if field[cell[1]][cell[0]] == 0:
                field[cell[1]][cell[0]] = player
                break
        print_field(field)
        if check_field(field):
            return player
        player = -player
    return 0

print_field(field)

result = playing_field(field)

if result:
    print(f'Player "{def_player(result)}" is winner!')
else:
    print('Dead heat!')