n = 5
queries = [[1,2,100],[2,5,100],[3,4,100]]
dic_sum = {}
m = queries[0][2]
for query in queries:
    for i in range(query[0], query[1] + 1):
        if i in dic_sum:
            dic_sum[i] += query[2]
        else:
            dic_sum[i] = query[2]
        if dic_sum[i] > m:
            m = dic_sum[i]
print(m)
