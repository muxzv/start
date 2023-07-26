"""  Quest v. 2.0 by MaxiGames  """


class Question:
    def __init__(self, qwst, list_of_answers, ok_num):
            """класс для вопросов"""
            self.qwst=qwst
            self.list_of_answers=list_of_answers
            self.ok_num=ok_num

    def ok(self, userAnswer):
        """ проверка ответа: верно или нет? """
        return int(userAnswer) == self.ok_num+1


class Quest:
    def __init__(self):
        """Класс для игры"""
        self.qs=[]

    def AddQuestion(self, q):
        '''Добавление вопроса'''
        self.qs.append(q)

    def Go(self):
        '''цикл для вопросов'''
        for q in self.qs:

            print(q.qwst+"?") 
            i=0
            for a in q.list_of_answers:
                i+=1
                print(str(i) + ". " + a)

            answ=input("Введите нужную цифру: ")
            if q.ok(answ):
                print("Верно!")
            else:
                print("Не верно!")