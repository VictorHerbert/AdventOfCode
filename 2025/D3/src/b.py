acum = 0

def argmax(values):
    return max(range(len(values)), key=lambda i: values[i])

while True:
    try:
        s = input()
        n = ''        
        minlim = 0
        for i in range(12):
            maxlim = -11+i
            if maxlim == 0:
                maxlim = len(s)            
            sub = s[minlim:maxlim]
            minlim = argmax(sub) + 1 + minlim
            n += max(sub)
        acum += int(n)
    except EOFError:
        break

print(acum)