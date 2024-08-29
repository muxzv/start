a,b,c,d,e,f = int(input()),int(input()),int(input()),int(input()),int(input()),int(input())

# a,b,c - первая коробка
# d,e,f - вторая коробка

def fit(a,b,c,d,e,f):
    '''
    Первая (a,b,c) помещается во вторую (d,e,f)
    '''
    return a <= d and b <= e and c <= f

f12 = fit(a,b,c,d,e,f) or fit(a,b,c,e,f,d) or fit(a,b,c,f,d,e) or fit(b,c,a,d,e,f) or fit(b,c,a,e,f,d) or fit(b,c,a,f,d,e) or fit(c,a,b,d,e,f) or fit(c,a,b,e,f,d) or fit(c,a,b,f,d,e)

f21 = fit(d,e,f,a,b,c) or fit(d,e,f,b,c,a) or fit(d,e,f,c,a,b) or fit(e,f,d,a,b,c) or fit(e,f,d,b,c,a) or fit(e,f,d,c,a,b) or fit(f,d,e,a,b,c) or fit(f,d,e,b,c,a) or fit(f,d,e,c,a,b)

if f12 and f21:
    print("Equal") #равны
elif f12:
    print('First') #abc в def
elif f21:
    print('Second') #def в abc
else:
    print('None') # никакая
