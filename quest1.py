from quest_class import Question
from quest_class import Quest

#создание объекта игры
quest=Quest()

#добавление вопросов
quest.AddQuestion(Question("Как тебя зовут",["Юля", "Макс", "Алла"], 1))
quest.AddQuestion(Question("Сколько тебе лет",["8", "1", "9"], 2))

#запуск
quest.Go()

#Я очень рад что сделал это(голосом робота)
