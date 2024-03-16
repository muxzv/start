def nod(n1, n2):
    for i in range(min(n1, n2), 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            return i

def nok(n1, n2):
    for i in range(1, 100):
        if i % n1 == 0 and i % n2 == 0:
            return i

def sokr(d):
    n = nod(d[0], d[1]) 
    return d[0] // n, d[1] // n

def add(d1, d2):
    return d1
    
print(add((3,12),(1,3)))
