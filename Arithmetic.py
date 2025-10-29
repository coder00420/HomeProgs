numbers = open("INPUT.TXT", "r").read().split()
a_multiply_b = int(numbers[0]) * int(numbers[1])
if a_multiply_b == int(numbers[2]):
    print("YES")
else: print("NO")