n = int(input())

if n >= 100:
    print('C')
else:
    e = n % 10
    d = n % 100 // 10
    # десятки
    if 1 <= d <= 2:
        er = 'X' * d
    elif d == 3:
        er = 'XXX'
    elif d == 4:
        er = 'XL'
    elif d == 5:
        er = 'L'
    elif d == 6:
        er = 'LX'
    elif d == 7:
        er = 'LXX'
    elif d == 8:
        er = 'LXXX'
    elif d == 9:
        er = 'XC'
    # единицы от 1 до 9
    if e == 1 or e == 2 or e == 3:
        dr = e * 'I'
    elif e == 4:
        dr = 'IV'
    elif e == 5:
        dr = 'V'
    elif e == 6:
        dr = 'VI'
    elif e == 7:
        dr = 'VII'
    elif e == 8:
        dr = 'VIII'
    elif e == 9:
        dr = 'IX'
    
    if d == 0:
        print(dr)
    elif e == 0:
        print(er)
    else:
        print(str(er) + str(dr))
