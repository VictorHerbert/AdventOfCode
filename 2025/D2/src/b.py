count = 0

pairs = input().split(',')
pairs = [pair.split('-') for pair in pairs]

for pair in pairs:
    print(pair)
    for i in range(int(pair[0]), int(pair[1])+1):
        s = str(i)
        for k in range(1, len(s)):
            if len(s)%k == 0:
                if len(set(s[l*k:(l+1)*k] for l in range(len(s)//k))) == 1:
                    count += i                    
                    break

print(count)