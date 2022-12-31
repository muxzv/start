from random import randint

class Game:
    def __init__(self, pl1, pl2, maxcount):
        self.pl1 = pl1
        self.pl2 = pl2
        self.maxcount = maxcount
        
    def Go(self):
        print('Игра "Камешки"')
        print('Правила игры: игроки по очереди берут камешки, не больше кол-ва оставшися камешков.'+
        'Проигрывает тот, кто возмёт последние камешки(последний камешек)')
        print('Приготовились? Старт!')
        count = self.maxcount
        loser = 0
        while count != 0:
            print('Ход 1 игрока!')
            print('Камешков в кучке:', count)
            take = self.pl1.take(count)
            count -= take
            if count == 0:
                loser = 1
                break
            print('Ход 2 игрока!')
            print('Камешков в кучке:', count)
            take = self.pl2.take(count)
            count -= take
            
        if loser == 0:
            print("Первый игрок победил!")
        else:
            print("Второй игрок победил!")

class Player:
    def __init__(self):
        pass
    def take(self, count):
        pass

class BotPlayer(Player):
    def take(self, count):
        t = randint(1, count)
        print('Бот взял', t, 'камешков')
        return t

class ManPlayer(Player):
    def take(self, count):
        t = int(input('Сколько камешков взять? '))
        print('Было взято', t, 'камешков')
        return t

pl1 = ManPlayer()
pl2 = ManPlayer()

game = Game(pl1, pl2, 15)

game.Go()
