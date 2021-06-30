q = [1,2,5,3,7,8,6,4]
dic = {}
res = 0
n = len(q)
for i in range(n):
    for j in range(n-1):
        if q[j] > q[j + 1]:
            if q[j] in dic:
                dic[q[j]] += 1
                if dic[q[j]] > 2:
                    print('Too chaotic')
                    break
            else:
                dic[q[j]] = 1
            aux = q[j]
            q[j] = q[j + 1]
            q[j + 1] = aux
            res += 1
print(res)
