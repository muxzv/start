n = int(input())
dr = 0
er = 0
if n >= 100:
    print('C')
else:
    e = n % 10
    d = n % 100 // 10
    # единицы от 1 до 9
    print(d,e)
    if 3 >= e > 0:
        dr = e * 'I'
    elif e == 4:
        dr = 'IV'
    elif e == 5:
        dr == 'V'
    elif e == 6:
        dr == 'VI'
    elif e == 7:
        dr == 'VII'
    elif e == 8:
        dr == 'VIII'
    if e == 9:
        dr == 'IX'
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
    
    if d == 0:
        print(dr)
    elif e == 0:
        print(er)
    else:
        print(str(er)+str(dr))
