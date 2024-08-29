a,b,c,d,e,f = int(input()),int(input()),int(input()),int(input()),int(input()),int(input())

# a,b,c - первая коробка
# d,e,f - вторая коробка

def fit(a,b,c,d,e,f):
    '''
    Первая (a,b,c) помещается во вторую (d,e,f)
    '''
    return a <= d and b <= e and c <= f

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
