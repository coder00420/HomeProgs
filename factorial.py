input_ = int(open('INPUT.TXT', 'r').read())
i = 2
res = 1
while i <= input_:
    res *= i
    i += 1
open('OUTPUT.TXT', 'w').write(str(res))