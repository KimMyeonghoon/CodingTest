N = int(input())
M = []

for i in range(1, N+1):
    if (i % 2 == 0) :
        continue
    elif (i % 3 == 0) :
        continue
    elif (i % 5 == 0):
        continue
    else :
        M.append(i)
print(len(M))