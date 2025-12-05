import math
circles = open('INPUT.TXT', 'r').read().split('\n')
while len(circles) > 2:
    circles.remove('')
cir1, cir2 = circles
x1, y1, r1 = map(int, cir1.split())
x2, y2, r2 = map(int, cir2.split())
x_dis = x2 - x1
y_dis = y2 - y1
dis = math.sqrt(math.fabs(x_dis ** 2 + y_dis ** 2))
if dis <= (r1 + r2) and (math.fabs(r2 - r1)) <= dis:
    open('OUTPUT.TXT', 'w').write('YES')
else:
    open('OUTPUT.TXT', 'w').write('NO')