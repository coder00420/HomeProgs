import math
equasion = input().replace(' ', '')

i = 0
while i < len(equasion):
    if equasion[i] == '-': 
        equasion = equasion[:i] + '+' + equasion[i:]
        i += 1
    i += 1
equasion_sides = equasion.split('=')

a = 0
b = 0
c = 0

for i in range(2):
    parts = equasion_sides[i].split('+')
    while '' in parts:
        parts.remove('')
    for j in parts:
        if '*' in j: coefficient = int(j[:j.index('*')])
        elif not 'x' in j: coefficient = int(j)
        else: coefficient = 1
        if i == 1: coefficient = -coefficient
        if '^' in j: a += coefficient
        elif 'x' in j: b += coefficient
        else: c += coefficient

D = b**2 - 4*a*c
if D < 0: print('No answer')
elif D == 0: print(-(b / 2*a))
elif D > 0:
    x1 = (-b - math.sqrt(D)) / 2*a
    x2 = (-b + math.sqrt(D)) / 2*a
    print(x1, x2)