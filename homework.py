numbers = [int(i) for i in open("INPUT.TXT", "r").read().split()]
numbers.pop(0)
sum_ = sum([i for i in numbers if i > 0])
min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))
res = 1
if min_index < max_index:
    for i in numbers[min_index + 1: max_index]:
        res *= i
else:
    for i in numbers[max_index + 1: min_index]:
        res *= i
open("OUTPUT.TXT", mode= "w").write(f"{sum_} {res}")