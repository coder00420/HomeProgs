res = open('INPUT.TXT', 'r').read()[1:].count('1')
res = int(int(res) / 2)
open('OUTPUT.TXT', 'w').write(str(res))