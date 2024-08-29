a,b,c,d,e,f = int(input()),int(input()),int(input()),int(input()),int(input()),int(input())

# a,b,c - первая коробка
# d,e,f - вторая коробка

def fit(a,b,c,d,e,f):
    '''
    Первая (a,b,c) помещается во вторую (d,e,f)
    '''
    return a <= d and b <= e and c <= f

def sort(a,b,c):
    if c > b:
        b,c = c,b
    if b > a:
        a,b = b,a
    if c > b:
        c,b = b,c
    return a,b,c
a,b,c = sort(a,b,c)
d,e,f = sort(d,e,f)
f12 = fit(a,b,c,d,e,f)
f21 = fit(d,e,f,a,b,c)

if f12 and f21:
    print("Equal") #равны
elif f12:
    print('First') #abc в def
elif f21:
    print('Second') #def в abc
else:
    print('None') # никакая
