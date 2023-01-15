import random
from telegram_library import MessageToTelegram

def random_bot(in_s):
    if in_s == '/start':
        return 'Привет! Введите что-нибудь.'
    elif in_s == '/test':
        o = MessageToTelegram()
        o.message = 'Выберите для теста'
        o.buttons = ['Первая', 'Вторая', 'Третья']
        return o
    elif in_s == 'Первая':
        return 'Очень хорошо'
    elif in_s == '/1':
        return 'Один'
    elif in_s == '/2':
        return 'Два'
    elif in_s == '/3':
        return 'Три'
    else:
        l = ["Максим", "Алла", "Юля"]
        s = 'Порядок: '
        for i in range(1,len(l) + 1):
            x = random.choice(l)
            l.remove(x)
            s += str(i) + ') ' + x + ' | '
        return s

if __name__ == "__main__":
    print(random_bot(""))
