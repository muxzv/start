n = 5 #int(input())
k = 2 #int(input())
a = [2,2]

cur_n = 1

for e in a:
    cur_n += e

print(n - cur_n % n)
