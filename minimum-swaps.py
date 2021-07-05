arr = [2,3,4,1,5]
count = 0
indexs = {k:i+1 for i, k in enumerate(arr)}

for i in range(1, len(arr) + 1):
    if i != arr[i-1]:
        count += 1
        indexs[arr[i - 1]] = indexs[i]
        arr[indexs[i]-1] = arr[i - 1]

print(count)
