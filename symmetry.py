input_ = open('INPUT.TXT', 'r').read().split('\n')
line_coords = list(map(int, input_[0].split()))
point_A = list(map(int, input_[1].split()))
if line_coords[0] == line_coords[2]:
    B_x_coord = line_coords[0] * 2 - point_A[0]
    B_y_coord = point_A[1]
else:
    B_x_coord = point_A[0]
    B_y_coord = line_coords[1] * 2 - point_A[1]
open('OUTPUT.TXT', 'w').write(f'{B_x_coord} {B_y_coord}')