hidden_number, assumption = tuple(open('INPUT.TXT', 'r').read().split())
cows = 0
bulls = 0
for i in range(4):
    if hidden_number[i] == assumption[i]: bulls += 1
    elif assumption[i] in hidden_number: cows += 1
open('OUTPUT.TXT', 'w').write(f'{bulls} {cows}')