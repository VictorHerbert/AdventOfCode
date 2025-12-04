from queue import Queue

acum = 0

mat = []

while True:
    try:
        mat.append(list(input()))
    except EOFError:
        break
    
del_list = []

while True:    
    for i, j in del_list:
        mat[i][j] = '.'
    
    del_list = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == '@':
                adj = 0
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if di == dj == 0:
                            continue

                        ni = i + di
                        nj = j + dj
                        if 0 <= ni < len(mat) and 0 <= nj < len(mat[i]):
                            adj += (mat[ni][nj] == '@')

                if (adj < 4):
                    acum += 1
                    del_list.append((i, j))
                    
    if len(del_list) == 0:
        break

print(acum)