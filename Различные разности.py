def f(num):
    n1, n2, n3, n4 = int(str(num)[0]), int(str(num)[1]), int(str(num)[2]), int(str(num)[3])
    n12 = abs(n1 - n2)
    n13 = abs(n1 - n3)
    n14 = abs(n1 - n4)
    n23 = abs(n2 - n3)
    n24 = abs(n2 - n4)
    n34 = abs(n3 - n4)
    s = {n12, n13, n14, n23, n24, n34}
    return len(s) == 6

for i in range(1000, 9999 + 1):
    if f(i):
        print(i)
        break
