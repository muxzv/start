# https://sochisirius.ru/uploads/2023/05/vos_invite_2023_inf_sol_4_5_kl.pdf
# Задача 5. Связь на уровне

import json

json_s = '{"0": 0, "1": 1, "2": 2, "3": 3, "4": 2, "5": 3, "6": 2, "7": 1, "8": 2, "9": 3, "10": 4, "11": 3, "12": 2, "13": 3, "14": 4, "15": 3, "16": 2, "17": 3, "18": 2, "19": 2, "20": 1, "21": 0, "22": 1, "23": 2, "24": 1, "25": 2, "26": 3, "27": 2, "28": 1, "29": 0}'
steps = ">< >< >< << << >< << << >< >< =< >< >> << >> => >> >< =< >< << >< >< >< ><"

def get_height(d, x):
    return d[x]
    
def to_delta(c):
    if c == '<':
        return -1
    elif c == '>':
        return 1
    else:
        return 0

def go():
    d2 = json.loads(json_s)
    
    d = {}
    
    for i in d2:
        d[int(i)] = d2[i]
    
    s3 = steps.split()
    
    x1, x2 = 0, 29

    for i, h in enumerate(s3):
        print(i+1)
        print('x', x1, x2)
        if x1 >= x2:
            print("OK")
            break
        y1, y2 = get_height(d, x1), get_height(d, x2)
        print('y', y1, y2)
        if y1 != y2:
            print('NOT GOOD: ERROR')
            break
        
        d1, d2 = to_delta(h[0]), to_delta(h[1])
        x1, x2 = x1 + d1, x2 + d2
        
    print('Final:', x1, y1, x2, y2)
    
go()
