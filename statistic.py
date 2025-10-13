days = list(map(int, open("INPUT.TXT", mode="r").read().split("\n")[1].split()))
odds = [str(i) for i in days if i % 2 != 0]
evens = [str(i) for i in days if i % 2 == 0]
res = ""
if len(evens) >= len(odds): res = "YES"
else: res = "NO"
open("OUTPUT.TXT", mode= "w").write(f"{" ".join(odds)}\n{" ".join(evens)}\n{res}")