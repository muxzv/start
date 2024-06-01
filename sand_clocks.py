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
            a, b = a-b, 0
            time_before += b
            path += ' t(' + str(b) + ')'
        else:
            a, b = 0, b-a
            time_before += a
            path += ' t(' + str(a) + ')'
    elif a > 0:
        time_before += a
        path += ' t(' + str(a) + ')'
        a = 0
    elif b > 0:
        time_before += b
        path += ' t(' + str(b) + ')'
        b = 0
    #else:
        #a, b = max_a, max_b
    print(time_before, a, b, path)
    if time_before > max_time:
        continue
    for action in 'w','a','b','ab':
        if action == 'w' and (a>0 or b>0):
            l.append([time_before, a, b, path + ' ' + action])
        if 'a' in action:
            l.append([time_before, max_a - a, b, path + ' ' + action])
        if 'b' in action:
            l.append([time_before, a, max_b - b, path + ' ' + action])
    i += 1
    if i > 100:
        break

print(i)
