input_number = int(open('INPUT.TXT', 'r').read())
integer_dividers = set()
min_divider = 1
max_divider = input_number
while max_divider >= min_divider:
    if input_number % min_divider == 0:
        res = int(input_number / min_divider)
        integer_dividers.add(res)
        integer_dividers.add(min_divider)
        max_divider = res
    min_divider += 1
res = sum(integer_dividers)
open('OUTPUT.TXT', 'w').write(str(res))