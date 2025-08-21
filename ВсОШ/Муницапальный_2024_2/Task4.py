n = int(input())
timeL=[]
typeL = []
for _ in range(n):
    s = input().split()
    time = int(s[0]) * 60 + int(s[1])
    timeL.append(time)
    typeL.append(s[2])

ans = []
start90 = None
isMetro = False
c = 0

for i in range(1,n+1):
    if typeL[i] == "M":
        if not isMetro:
            isMetro = True
        ans.append(57)
        start90 = timeL[i]
        c += 1
    else:
        if start90 != None:
            if timeL[i] <= (start09 + 90):
                if c >= 2:
                    ans.append(0)
                else:
                    ans.append(28)
                    isMetro = False
