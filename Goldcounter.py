numbers = open("INPUT.TXT", "r").read().split()
numbers = [int(i) for i in numbers]
res = numbers[0]
for i in numbers:
    if res < i:
        res = i
print(res)