def ok(c1, c2, a, b):
    if a == 0 or b == 0:
        return False
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
        d[di] -= max_c2 * 2

        max_c1 = d[di]
        if c1_ost < max_c1:
            max_c1 = c1_ost
        d[di] -= max_c1

    return sum(d) == 0

#print(ok())

# 1,1,1,1 квадрат
# 1,4,2,2 квадрат с хвостиком
# 2,2,1,2 прямоугольник
# 1,3,

def test():
    print(ok(1,1,1,1) == False)
    print(ok(1,4,2,2) == True)
    print(ok(2,2,1,2) == True)
    print(ok(3,0,1,1) == False)
    print(ok(5,0,2,0) == False)

#test()

def Task(n, m):
    p = n + m * 2
    s = 0
    a = (p + 3) // 4
    for ai in range(a,0,-1):
        b = (p - 2 * ai) // 2
        #print(n,m,ai,b, p, ok(n,m,ai,b))
        if ok(n,m,ai,b):
            s = ai * b
            break
    return s

def test2():
    print(Task(5, 0) == 1)
    print(Task(4, 3) == 6)
    print(Task(3, 0) == 0)
    
test2()