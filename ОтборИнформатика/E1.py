n = int(input())
a = list(map(int, input().split()))
s1, s2 = 0, 0

for e in a:
  s1 += e
  s2 += e ** 2

print(n * s2 - s1 ** 2)
