def prefixes_list(sequence):
    if len(sequence) <= 1:
        return [0]
    k = 0
    i = 1
    prefixes = [0]
    while i < len(sequence):
        if sequence[i] == sequence[k]:
            k += 1
            prefixes.append(k)
            i += 1
        elif k == 0:
            prefixes.append(k)
            i += 1
        else:
            k -= 1
    return prefixes


n = int(input())
sequence = input().split()[:-1]
