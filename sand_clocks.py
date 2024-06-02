# песочные часы

max_a = 7
max_b = 10
max_time = 20

time_before = 0
a, b = 0, 0
path = ""

l = []
l.append([time_before, a, b, path])

i = 0

while len(l) > 0:
    state = l.pop(0)
    #print(state)
    time_before, a, b, path = state[0], state[1], state[2], state[3]
    if a > 0 and b > 0:
        if a > b:
            path += ' t(' + str(b) + ')'
            time_before += b
            a, b = a-b, 0
        else:
            path += ' t(' + str(a) + ')'
            time_before += a
            a, b = 0, b-a
    elif a > 0:
        path += ' t(' + str(a) + ')'
        time_before += a
        a = 0
    elif b > 0:
        path += ' t(' + str(b) + ')'
        time_before += b
        b = 0
    if time_before > max_time:
        continue
    print(time_before, a, b, path)
    l.append([time_before, max_a - a, b, path + ' a'])
    l.append([time_before, a, max_b - b, path + ' b'])
    l.append([time_before, max_a - a, max_b - b, path + ' ab'])
    i += 1
    if i > 100:
        break

print(i)
