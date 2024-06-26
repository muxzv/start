import random
HANGMAN_PICS = ['''
  + - - - +
          |
          |
          |
         ===''', '''
  + - - - +
      0   |
          |
          |
         ===''', '''
  + - - - +
      0   |
      |   |
          |
         ===''','''
  + - - - +
      0   |
     /|   |
          |
         ===''', '''
  + - - - +
      0   |
     /|\  |
          |
         ===''', '''
  + - - - +
      0   |
     /|\  |
     / \  |
         ===''']
words = '''аист акула бобр лось пчела собака тритон питон обезьяна коза осёл хорёк попугай'''.split()
def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print("Ошибочные буквы:", end=' ')
    for letter in missedLetters:
        print(letter, end = ' ')

        print()
        blanks = '_' * len(secretWord)
        for i in range(len(secretWord)):
            if secretWord[i] in correctLetters:
                  blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

        for letter in blanks:
            print(letter, end = ' ')
        print()
    
def getGuess(alreadyGuessed):
    while True:
        print("Введите букву.")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Пожалуйста, введите одну букву')
        elif guess in alreadyGuessed:
            print("Вы уже называли эту букву. Назовите другую.")
        elif guess not in "йцукенгшщзхъфывапролджэячсмитьбю":
            print("ВВЕДИТЕ БУКВУ.")
        else:
            return

def PlayAgain():
    print("Хотите сыграть ещё раз? (да/нет)")
    return input().lower().startswith('д')
print("В И С Е Л И Ц А")
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters += guess
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print("Да! Секретное слово:", secretWord, '. Вы выиграли!')
            gameIsDone = True
    else:
        missedLetters += guess
        if len(missedLetters) >= len(HANGMAN_PICS) -1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('Вы исчерпали все попытки! \nНе угадано букв', str(len(missedLetters)), 'и угадано букв', str(len(correctLetters), '. Было загадано слово', secretWord, '.')  )
            gameIsDone = True
    
        if gameIsDone:
            if playAgain:
               missedLetters = ''
               correctLetters = ''
               secretWord = getRandomWord(words)
               gameIsDone = False
            else:
                break




              
