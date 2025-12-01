dial = 50
zeroCount = 0

while True:
    try:
        rot = input()
        rot = rot.replace('L', '-')
        rot = rot.replace('R', '+')
        dial += int(rot)
        dial %= 100
        zeroCount += (dial == 0)
    except EOFError:
        break

print(zeroCount)