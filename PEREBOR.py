# рекурсивный перебор вариантов

# :2
# -1

def rek(a,b,s,res):
    if a == b:
        res.append(s)
    elif a > b:
        if a % 2 ==0:
            rek(a//2, b, s + ':2', res)
        rek(a-1, b, s + '-1', res)
    return res
    
a = 20
b = 10

print(rek(a,b,'',[]))
