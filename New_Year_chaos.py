q = [1,2,5,3,4,7,8,6]
res = 0
n = len(q)
for i in range(n):
    aux = q[i] - (i + 1)
    if aux > 2:
        print('Too chaotic')
        break
    for j in range(max(0,q[i] - 2), i):
        if q[j] > q[i]:
            res += 1

print(res)
