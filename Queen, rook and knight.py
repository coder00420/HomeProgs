input_ = open('INPUT.TXT', 'r').read().split()
letters = 'ABCDEFGH'

queens_pos = list(input_[0])
queens_pos[0] = letters.index(queens_pos[0])
queens_pos[1] = int(queens_pos[1]) - 1

rooks_pos = list(input_[1])
rooks_pos[0] = letters.index(rooks_pos[0]) 
rooks_pos[1] = int(rooks_pos[1]) - 1

knights_pos = list(input_[2])
knights_pos[0] = letters.index(knights_pos[0])
knights_pos[1] = int(knights_pos[1]) - 1


game_board = [[0 for _ in range(8)] for _ in range(8)]


for row in game_board:
    row[queens_pos[0]] = 1
game_board[queens_pos[1]] = [1 for _ in range(8)]
for row in range(8):
    distance = abs(row - queens_pos[1])
    if queens_pos[0] - distance >= 0 and queens_pos[0] - distance < 8:
        game_board[row][queens_pos[0] - distance] = 1
    if queens_pos[0] + distance >= 0 and queens_pos[0] + distance < 8:
        game_board[row][queens_pos[0] + distance] = 1


for row in game_board:
    row[rooks_pos[0]] = 1
game_board[rooks_pos[1]] = [1 for _ in range(8)]


knights_atks = [1, 2, 0, 2, 1]
i = 0
for row in range(knights_pos[1] - 2, knights_pos[1] + 3):
    if row < 0 or row > 7 or row == knights_pos[1]: 
        i += 1
        continue
    if knights_pos[0] - knights_atks[i] >= 0 and knights_pos[0] - knights_atks[i] < 8:
        game_board[row][knights_pos[0] - knights_atks[i]] = 1
    if knights_pos[0] + knights_atks[i] >= 0 and knights_pos[0] + knights_atks[i] < 8:
        game_board[row][knights_pos[0] + knights_atks[i]] = 1
    i += 1


game_board[queens_pos[1]][queens_pos[0]] = 9
game_board[rooks_pos[1]][rooks_pos[0]] = 7
game_board[knights_pos[1]][knights_pos[0]] = 2


res = 0
for i in game_board:
    for j in i:
        if j == 1: res += 1
open('OUTPUT.TXT', 'w').write(str(res))

i = len(game_board) - 1
while i >= 0:
    print(game_board[i])
    i -= 1