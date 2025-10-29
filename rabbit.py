k, n = map(int, open("INPUT.TXT", "r").read().split())
stairs = []
for i in range(k + 1):
    stairs.append(0)
stairs[0] = 1
for i in range(1, k + 1):
    stairs[i] = sum(stairs[:i])
for i in range(n - k):
    for j in range(k):
        stairs[j] = stairs[j + 1]
    stairs[-1] = sum(stairs[:-1])
open("OUTPUT.TXT", "w").write(str(stairs[-1]))