from random import randint

start = 5
limit = 100

l = []

l.append([start, []])

c = 0
while len(l) > 0:
    item = l.pop(0)
    print(item)
    c, route = item[0], item[1]
    if c > limit:
        break
    l.append([c + 1,route+['+1']])
    l.append([c + 2,route+['+2']])
    l.append([c * 3,route+['*3']])
