v1 = 0
v2 = 0
#v1 - кол-во воды в сосуде 1
#v2 - кол-во воды в сосуде 2

#c1 - максимальное кол-во воды в сосуде 1
#c2 - максимальное кол-во воды в сосуде 2

#d - действие:
#0 - перелить из 1 во 2
#1 - перелить из 2 во 1
#2 - вылить из 1
#3 - вылить из 2
#4 - налить в 1
#5 - налить во 2

v1 = 0
v2 = 0
def perelit(v1,v2,c1,c2,d):
    #if d == 0:
    #    
    #elif d == 1:
    # 
    if d == 2:
        v1 = 0
    elif d == 3:
        v2 = 0
    elif d == 4:
        v1 = c1
    elif d == 5:
        v2 = c2
    return v1, v2
def algoritm(c1,c2):
    if v1 == 0:
        v1, v2 = perelit(0,0,c1,c2)
    v1,v2 = perelit(v1,v2,c1,c2,0)
    if v2 == c2:
        v1,v2 = perelit(v1,v2,c1,c2,3)


v1, v2 = 0, 0
c1, c2 = 7, 8
print(v1,v2)
v1, v2 = perelit(v1,v2,c1,c2,4)
print(v1,v2)
v1, v2 = perelit(v1,v2,c1,c2,2)
print(v1,v2)
