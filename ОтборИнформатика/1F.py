a = list(map(int,input().split()))
rows = a[0]
cols = a[1]

m = [[0 for _ in range(cols)] for _ in range(rows)]

rows_even = list(map(int,input().split()))
cols_even = list(map(int,input().split()))

for i in rows_even:
    for j in cols_even:
        m[i][j] = 1

for e in m:
    print(e)