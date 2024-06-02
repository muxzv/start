# песочные часы

def task(max_a, max_b, max_time, good_solve):
    res = []
    time_before = 0
    a, b = 0, 0
    path = []
    
    l = []
    l.append([time_before, a, b, path])
    
    i = 0
    
    while len(l) > 0:
        state = l.pop(0)
        #print(state)
        time_before, a, b, path = state[0], state[1], state[2], state[3]
        if a > 0 and b > 0:
            if a > b:
                path.append(b)
                time_before += b
                a, b = a-b, 0
            else:
                path.append(a)
                time_before += a
                a, b = 0, b-a
        elif a > 0:
            path.append(a)
            time_before += a
            a = 0
        elif b > 0:
            path.append(b)
            time_before += b
            b = 0
        if time_before > max_time:
            continue
        if good_solve(path):
            res.append(path)
        l.append([time_before, max_a - a, b, path + ['a']])
        l.append([time_before, a, max_b - b, path + ['b']])
        l.append([time_before, max_a - a, max_b - b, path + ['ab']])
        i += 1
        if i > 200:
            print("err")
            break
    return res

def good_solve(path, need_time):
    s = 0
    for i in reversed(path):
        if type(i)==int:
            s += i
            if s == need_time:
                return True
    return False

def good_solve1(path):
    return good_solve(path, 11)
    
def good_solve2(path):
    if not good_solve(path, 16):
        return False
    s = ''
    for i in path:
        if type(i)==str:
            s += i
    return s.count('a') == 2 and s.count('b') == 2

print(task(7, 10, 20, good_solve1))
print()

print(task(4, 11, 20, good_solve2))
