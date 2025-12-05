salaries = list(map(int, open('INPUT.TXT', 'r').read().split()))
res = max(salaries) - min(salaries)
open('OUTPUT.TXT', 'w').write(str(res))