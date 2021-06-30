a = [1,2,3,4,5]
d = 4
n = len(a)
res = a.copy()

for i in range(n):
    res[(i-d) % n] = a[i]

print(res)
