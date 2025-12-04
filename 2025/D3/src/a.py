acum = 0

def argmax(values):
    return max(range(len(values)), key=lambda i: values[i])

while True:
    try:
        s = input()
        a1 = argmax(s[:-1])
        m1 = s[a1]
        m2 = max(s[a1+1:])
        acum += int(m1 + m2)    
    except EOFError:
        break

print(acum)