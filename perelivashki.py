v1 = 0
v2 = 0
#current1 - кол-во воды в сосуде 1
#current2 - кол-во воды в сосуде 2

#max1 - максимальное кол-во воды в сосуде 1
#max2 - максимальное кол-во воды в сосуде 2

#action - действие:
#0 - перелить из 1 во 2
#1 - перелить из 2 в 1
#2 - вылить из 1
#3 - вылить из 2
#4 - налить в 1
#5 - налить во 2

v1 = 0
v2 = 0
def perelit(current1,current2,max1,max2,action):
    if action == 0:
        dolit = max2 - current2
        if dolit == 0:
            pass
        else:
            if current1 < dolit:
                current2 += current1
                current1 = 0
            else:
                current1 -= dolit
                current2 += dolit
    elif action == 1:
        dolit = max2 - current1
        if dolit == 0:
                pass
        else:
            if current2 < dolit:
                current1 += current2
                current2 = 0
            else:
                current2 -= dolit
                current1 += dolit
    if action == 2:
        current1 = 0
    elif action == 3:
        current2 = 0
    elif action == 4:
        current1 = max1
    elif action == 5:
        current2 = max2
    return current1, current2

def algoritm(amount1, amount2, max1, max2):
    a1,a2 = amount1, amount2
    num = 0
    print(num,a1,a2)
    for _ in range(6):
        if amount1 == 0:
            a1 = max1
            num += 1
            print(num,a1,a2)
        a1,a2 = perelit(a1,a2,max1,max2,0)
        num += 1
        print(num,a1,a2)
        if a2 == max2:
            a2 = 0
            num += 1
            print(num,a1,a2)



amount1, amount2 = 0, 0
max1, max2 = 7, 5
algoritm(amount1, amount2, max1, max2)
