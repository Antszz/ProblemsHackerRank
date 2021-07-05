n = 4
queries = [[2,3,603],[1,1,286],[4,4,882]]

array = [0] * (n + 1)
m = 0
for query in queries:
    array[query[0]] += query[2]
    if query[1] + 1 <= n:
        array[query[1] + 1] -= query[2]
print(array)
cumulative = 0
for sum in array:
    cumulative += sum
    if cumulative > m:
        m = cumulative

print(m)