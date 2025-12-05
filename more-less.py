A, B = map(int, open('INPUT.TXT', 'r').read().split())
if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('=')