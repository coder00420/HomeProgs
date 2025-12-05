input_ = open('INPUT.TXT', 'r').read().split('\n')
canvas_size = list(map(int, input_[0].split()))
canvas = [[0 for _ in range(canvas_size[0])] for _ in range(canvas_size[1])]
for i in range(int(input_[1])):
    coords = list(map(int, input_[i + 2].split()))
    squares_row = [1 for i in range(coords[2] - coords[0])]
    for i in canvas[coords[1]:coords[3]]:
        i[coords[0]:coords[2]] = squares_row 
res = 0
for i in canvas:
    res += i.count(0)
open('OUTPUT.TXT', 'w').write(str(res))