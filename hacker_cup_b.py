t = int(input())
add_board = {}  # Note that a player filling an entire diagonal with their symbols does not cause them to win.
board = []
n_n = []

for _ in range(t):
    n = int(input())
    n_n.append(n)
    for i in range(n):
        row = input()
        add_board[i] = row
    board.append(add_board)
    add_board = {}


def find_max_x(num_boards):
    size = n_n[num_boards]
    not_this_board = {}
    for _ in range(t):
        for j in range(size):
            this = '.' * size
            not_this_board[j] = this
    this_board = board[num_boards]
    possible = 0
    b_row = []
    b_column = []
    for j in range(size):
        add_row = []
        add_column = []
        for k in range(size):
            add_row.append(board[num_boards][j][k])
            add_column.append(board[num_boards][k][j])
        b_row.append(add_row)
        b_column.append(add_column)

    num_x_r = [0] * size
    num_x_c = [0] * size
    for j in range(size):  # counting 'X' in row/column
        for k in range(size):
            if 'X' in b_row[j][k]:
                num_x_r[j] += 1
            if 'X' in b_column[j][k]:
                num_x_c[j] += 1

    max_row = max(num_x_r)
    max_col = max(num_x_c)
    position_max_row = [j for j, k in enumerate(num_x_r) if k == max_row]
    position_max_col = [j for j, k in enumerate(num_x_c) if k == max_col]

    if this_board != not_this_board:
        for j in range(size):  # เติมที่เดียวชนะ2ที่
            for k in range(size):
                if '.' == b_row[j][k] and b_row[j].count('X') == max(max_row, max_col) and 'O' not in b_row[j]:
                    new = b_row[j][k].index('.')
                    b_row[j][new] = 'X'
                    if b_row[j] == b_column[k]:
                        possible -= 1
                    b_row[j][k] = '.'
                elif '.' == b_column[k][j] and b_column[k].count('X') == max(max_row, max_col) and 'O' not in b_column[j]:
                    new = b_column[k][j].index('.')
                    b_column[k][new] = 'X'
                    if b_row[j] == b_column[k]:
                        possible -= 1
                    b_column[k][new] = '.'

    if max_row == max_col:
        possible += len(position_max_row) + len(position_max_col)
        times = size - max_row
        for j in range(len(position_max_row)):  # มี 0 ไม่ชนะ
            if 'O' in b_row[position_max_row[j]]:
                possible -= 1
        for j in range(len(position_max_col)):
            if 'O' in b_column[position_max_col[j]]:
                possible -= 1
    elif max_row > max_col:
        possible += len(position_max_row)
        times = size - max_row
        for j in range(len(position_max_row)):
            if 'O' in b_row[position_max_row[j]]:
                possible -= 1
    else:
        possible += len(position_max_col)
        times = size - max_col
        for j in range(len(position_max_col)):
            if 'O' in b_column[position_max_col[j]]:
                possible -= 1

    if possible > 0:
        print(f"Case #{num_boards+1}: {times} {possible}")
    else:
        print(f"Case #{num_boards+1}: Impossible")


for _ in range(t):
    find_max_x(_)
