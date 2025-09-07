n = int(input())
a = list(map(int,input().split()))
p = list(map(int,input().split()))

min_stoim_point = 10000000
min_ind = -1
for i in range(n): #пробегаемся по позициям станций
    stoim = 0
    for i2 in range(n):
        if i != i2:
            c_stoim = (a[i]-a[i2]) * p[i2]
            stoim += abs(c_stoim)
    if stoim < min_stoim_point:
        min_stoim_point = stoim
        min_ind = i
min_ind += 1
print(min_ind)
