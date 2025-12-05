number_1, number_2 = map(int, open('INPUT.TXT', 'r').read().split())
a = number_1
b = number_2
while a != b:
    if a > b:
        c = a
        a = b
        b = c
    b -= a
greatest_common_divisor = a
res = int(abs(number_1 * number_2) / greatest_common_divisor)
open('OUTPUT.TXT', 'w').write(str(res))