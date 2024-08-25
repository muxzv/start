import sys
sys.setrecursionlimit(10000)

def akk(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return akk(m - 1, 1)
    else:
        return akk(m - 1, akk(m, n - 1))

int_list = list(map(int, input().split()))
m,n = int_list[0], int_list[1]

print(akk(m, n))
