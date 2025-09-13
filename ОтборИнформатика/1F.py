a = [] # list(map(int,input().split()))
rows = 4 # a[0]
cols = 3 # a[1]

m = [[0 for _ in range(cols)] for _ in range(rows)]

rows_even = list(map(int,input().split()))
cols_even = list(map(int,input().split()))

ones_rows = []
ones_cols = []

for i in range(len(rows)):
    if rows[i] == 1:
        ones_rows.append(i)

for i in range(len(cols)):
    if cols[i] == 1:
        ones_cols.append(i)

if len(ones_cols) != len(ones_rows):
    print("NO")
else:
    m = [[0 for _ in range(cols)] for _ in range(rows)]
    for e in ones_rows:
        for e2 in ones_cols:
            m[e][e2] = 1

for e in m:
    print(e)