x = [1,2,3,4,5,6,7]
n = len(x)
for index in range(2 ** (n-1)):
    partition = []
    subset = []
    for p in range(n):
        subset.append(x[p])
        if 1 << p & index or p == n-1:
            partition.append(subset)
            subset = []
    print(partition)
