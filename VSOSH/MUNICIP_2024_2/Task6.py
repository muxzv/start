n,m = 5,0

def ok(c1, c2, a, b):
    p1 = c1 + c2 * 2 #длина всех палочек
    p2 = a * 2 + b * 2 #периметр прямоугольника
    if p1 < p2:
        return False
    d = [a, a, b, b]
    c1_ost = c1
    c2_ost = c2
    for di in range(len(d)):
        max_c2 = d[di] // 2
        if c2_ost < max_c2:
            max_c2 = c2_ost
        c2_ost -= max_c2
        d[di] -= max_c2    * 2

        max_c1 = d[di]
        if c1_ost < max_c1:
            max_c1 = c1_ost
        d[di] -= max_c1

    return sum(d) == 0

print(ok(1,1,1,1))