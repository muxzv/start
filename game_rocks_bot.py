# stateless code for telegram bot

def Go(text, d):
    if d == None:
        d = dict()
        d['state'] = 0
    state = int(d['state'])
    if state == 0:
        d['state'] = 1
        return 'Привет! Правила. Введие кол во камешков:', d
    elif state == 1:
        d['count'] = int(text)
        d['state'] = 2
        return 'Ход первого игрока:', d
    elif state == 2:
        step = int(text)
        count = d['count']
        count -= step
        d['count'] = count
        d['state'] = 3
        return 'Ход второго игрока', d
    elif state == 3:
        step = int(text)
        count = d['count']
        count -= step
        d['count'] = count
        d['state'] = 2
        return 'Ход первого игрока', d
