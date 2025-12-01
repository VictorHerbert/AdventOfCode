dial = 50
zeroCount = 0

def countZeros(a, b):
    n,m = min(a,b), max(a,b)
    return m//100  - (n+99)//100 + 1 - (a%100==0)

while True:
    try:
        rot = input()
        rot = rot.replace('L', '-')
        rot = rot.replace('R', '+')
        rot = int(rot)
        
        new_dial = dial + rot
        zeroCount += countZeros(dial, new_dial)
        dial = new_dial
    except EOFError:
        break

print(zeroCount)