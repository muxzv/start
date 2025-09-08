n = int(input())
x = list(map(int,input().split()))

l = [0] * n

for i in range(1,n + 1):
    for j in range(i):
        l[j] += x[j]

for i in range(n):
    l[i] *= l[i]
print(l)