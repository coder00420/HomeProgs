numbers = [int(i) for i in open("INPUT.TXT", "r").read().split()]
res = []
for i in range(-100, 101):
    if i**3 * numbers[0] + i**2 * numbers[1] + i * numbers[2] + numbers[3] == 0: res.append(str(i))
res = " ".join(res)
open("OUTPUT.TXT", "w").write(res)
