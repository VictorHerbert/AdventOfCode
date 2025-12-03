count = 0

pairs = input().split(',')
pairs = [pair.split('-') for pair in pairs]

for pair in pairs:
    for i in range(int(pair[0]), int(pair[1])+1):
        s = str(i)
        if len(s)%2 == 0 and s[:len(s)//2] == s[len(s)//2:]:
            count += i            

print(count)