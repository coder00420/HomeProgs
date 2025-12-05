import math as m

platforms = open('INPUT.TXT', 'r').read().split('\n')[1].split()
platforms = list(map(int, platforms))
first_platform = 0
second_platform = m.fabs(platforms[0] - platforms[1]) if len(platforms) > 1 else first_platform

i = 2
while i < len(platforms):
    cur_platform = platforms[i]
    short_jump = m.fabs(cur_platform - platforms[i - 1]) + second_platform
    long_jump = m.fabs(cur_platform - platforms[i - 2]) * 3 + first_platform
    third_platform = short_jump if short_jump < long_jump else long_jump
    first_platform = second_platform
    second_platform = third_platform
    i += 1

res = str(int(second_platform))
open('OUTPUT.TXT', 'w').write(res)