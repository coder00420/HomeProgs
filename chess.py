import re
move = open("INPUT.TXT", "r").read()
res = ""
if re.fullmatch(r"[A-H][1-8]-[A-H][1-8]\n?", move):
    letters = "ABCDEFGH"
    res = "YES"
    x_position = letters.index(move[0]) + 1
    x_position_new = letters.index(move[3]) + 1
    y_position = int(move[1])
    y_position_new = int(move[4])
    if not (abs(x_position_new - x_position) != 0 and abs(x_position_new - x_position) <= 2):
        res = "NO"
    elif not (abs(y_position_new - y_position) != 0 and abs(y_position_new - y_position) <= 2):
        res = "NO"
    elif abs(x_position_new - x_position) + abs(y_position_new - y_position) != 3:
        res = "NO"
    open("OUTPUT.TXT", "w").write(res)
else:
    open("OUTPUT.TXT", "w").write("ERROR")