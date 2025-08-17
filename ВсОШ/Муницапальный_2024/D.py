l = [5, 1, 2] #list(map(int,input().split()))
n = l[0]
h = l[1]
c = l[2]

hl = [2]#list(map(int,input().split()))
cl = [1,5]#list(map(int,input().split()))
d = [None] + [2,1,1,0,2]#list(map(int,input().split()))

l = [-1] * (n + 1)
l[0] = 'None'

for e in hl:
    l[e] = 1
for e in cl:
    l[e] = 0
res = []
for i in range(1, n + 1):
    cur_range = d[i] + 1
    
    if i - cur_range <= 0:
        start = 1
    else:
        start = i - cur_range
    
    if i + cur_range > n + 1:
        end = n + 1
    else:
        end = i + cur_range
    
    f = True
    for j in range(start,end):
        print("Окно:",i)
        print("Пассажир:",j)
        print("Пассажиру",l[j])
        if l[j] == 0:
            f = False
            break
        elif l[j] == 1:
            l[j] = -1
            res.append(j)
print(res)
