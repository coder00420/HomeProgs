input_integer = int(open('INPUT.TXT', 'r').read())
bynary_integer = bin(input_integer)
res = bynary_integer.count('1')
open('OUTPUT.TXT', 'w').write(str(res))
