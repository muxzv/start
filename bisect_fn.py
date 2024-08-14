# численное решение уравнений методом деления отрезка пополам
# при помощи рекурсии

def different_sign(f1, f2):
    return f1<0 and f2>0 or f2<0 and f1>0

def solve1(f,lx,rx):
    for x in range(lx, rx+1):
        if f(x)==0:
            return x

def solve2(f,lx,rx,ex):
    print(lx,rx)
    if lx >= rx:
        return None
    if rx-lx <= ex:
        return (rx+lx)/2
    ly = f(lx)
    ry = f(rx)
    if not different_sign(ly,ry):
        return None
    tx = (lx+rx)/2
    ty = f(tx)
    if different_sign(ly,ty):
        return solve2(f,lx,tx,ex)
    elif different_sign(ty,ry):
        return solve2(f,tx,rx,ex)
    
print(solve2(lambda x: 2*x-2,-1000,1000, 0.001))
