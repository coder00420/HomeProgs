digit = open("INPUT.TXT", mode="r").read()
if digit == "0":
    open("OUTPUT.TXT", mode= "w").write("0")
else:
    number = [digit, "9", str(9 - int(digit))]
    open("OUTPUT.TXT", mode= "w").write("".join(number))