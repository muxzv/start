def chet_nechet(n):
    return n % 2 == 0

a = list(map(int,input().split()))
rows = a[0]
cols = a[1]

m = [[0 for _ in range(cols)] for _ in range(rows)]

rows_even = list(map(int,input().split()))
cols_even = list(map(int,input().split()))

ones_rows = []
ones_cols = []

for i in range(len(rows_even)):
    if rows_even[i] == 1:
        ones_rows.append(i)

for i in range(len(cols_even)):
    if cols_even[i] == 1:
        ones_cols.append(i)


#print(ones_cols)
#print(ones_rows)

n_c = chet_nechet(len(ones_rows))
m_c = chet_nechet(len(ones_cols))

if m_c != n_c:
    print("NO")
else:
    print("YES")
    for i in range(max(len(ones_cols),len(ones_rows))):
        if i < len(ones_cols):
            #rint(i,len(ones_cols))
            col = ones_cols[i]
        if i < len(ones_rows):
            row = ones_rows[i]
        m[row][col] = 1

    for e in m:
        print(*e)