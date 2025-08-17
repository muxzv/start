#https://codeforces.com/gym/105521/problem/A

a = int(input())#математика
b = int(input())#информатика

k = int(input())

x = int(input())#математика
y = int(input())#информатика


if x == y:
    print(k * x)
elif x > y:
    for _ in range(k + 1):
        if k > 0:
            res += 1
            if x > 0:
                a -= 1
            else:
                b -= 1
    print(res)
elif y > x:
    for _ in range(k + 1):
        if k > 0:
            res += 1
            if b > 0:
                b -= 1
            else:
                a -= 1
    print(res)
