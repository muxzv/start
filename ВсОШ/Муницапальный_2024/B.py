n = 5 #int(input())
k = 2 #int(input())

a = [2,2]

for e in a:
    n -= (e % n)

print(n - 1)
