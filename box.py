sides = []
for i in range(5):
    sides.append(input().split())


sides_sorted = []
for i in sides:
    sides_sorted.append(i.copy())
    sides_sorted[-1].sort()
    sides_sorted[-1] = str(" ".join(sides_sorted[-1]))

unique_sides = []
res = -1
while sides_sorted:
    if sides_sorted.count(sides_sorted[0]) == 1:
        unique_sides.append(sides_sorted[0])
        sides_sorted.pop(0)
    elif sides_sorted.count(sides_sorted[0]) == 2:
        side = sides_sorted[0]
        while side in sides_sorted:
            sides_sorted.remove(side)
    elif sides_sorted.count(sides_sorted[0]) == 3 or sides_sorted.count(sides_sorted[0]) == 4:
        break
    elif sides_sorted.count(sides_sorted[0]) == 5:
        res = " ".join(sides[0])
        break

if len(unique_sides) == 1 and not sides_sorted:
    if unique_sides[0] in sides:
        print(" ".join(unique_sides[0]))
    else:
        print(" ".join(unique_sides[0][::-1]))
else:
    print(res)