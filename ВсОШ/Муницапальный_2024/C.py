n = 4
#for _ in range(n):
#    a = input()
a = [2,1,7,5]
b = [3,5,3,6]

a = sorted(a)
b = sorted(b)

ne = [0] * n

for i in range(n):
    ne[i] = abs(b[i] - a[i])

print(sum(ne))
