input_ = open('INPUT.TXT', 'r').read().split('\n')
n, k = map(int, input_[0].split())
letters = []
for i in range(2, len(input_), 2):
    letter = list(map(int, input_[i].split()))
    modified_letter = [0]
    first_number = letter.pop(0)
    for n in letter:
        next_number = n - first_number
        if next_number < 0: next_number += k
        modified_letter.append(next_number)
    letters.append(modified_letter)
counter = 0
for i in range(len(letters)):
    letter1 = letters.pop(0)
    for letter2 in letters:
        if letter1 == letter2: counter += 1
print(counter)