'''
В магазине продаются вафли по 4 монеты за штуку и пончики по 7 монет за штуку. Определите, можно ли закупиться ровно на n монет.

Вы можете купить два или более пончиков и две или более вафли, а также можете купить ноль пончиков или ноль вафель.
'''

def mult(n, k):
    '''
    кратно ли число n числу k
    '''
    return n % k == 0

def check(n):
    '''
    достаточно только 4 проверки для кратных семи (т.к. разные сдвиги 0,3,2,1)
    0 + 4x = n
    7 + 4x = n
    14 + 4x = n
    21 + 4x = n
    '''
    return mult(n, 4) or mult(n, 7) or \
        n > 7 and mult(n - 7, 4) or \
        n > 14 and mult(n - 14, 4) or \
        n > 21 and mult(n - 21, 4)

n = int(input())
print('YES' if check(n) else 'NO')