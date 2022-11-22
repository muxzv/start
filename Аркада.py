from random import randint

from random import randint

c = 0
h1 = 0
h2 = 0

b = 0
p = 0

while c < 3:
     c += 1
     print('Раунд', c)
     h1 = randint(1, 6)
     print('Бот ходит', h1)
     h2 = randint(1, 6)
     print('Вы ходите', h2)
     if h2 == h1:
          print('Одинаково')
     elif h1 > h2:
          b += 1
     elif h1 < h2:
          p += 1
     
     print('Ваши очки', p, ', Очки бота' , b)
     print()

print('Ваши очки:', p)
print('Очки бота:', b)

if b < p:
     print('Вы победили!!!')
elif b > p:
     print('Бот победил...')
elif b == p:
     print('Ничья.')
     
     
