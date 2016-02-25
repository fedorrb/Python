# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self, name, conf):
        self.conf = {}
        self.name = name
        self.conf = conf
        self.exam_max = conf.get('exam_max')
        self.lab_max = conf.get('lab_max')
        self.lab_num = conf.get('lab_num')
        self.k = conf.get('k')
        self.exam_val = float(0)
        self.total_max = float(self.lab_max * self.lab_num + self.exam_max)
        self.total = float(0)
        self.labs = []
        for i in range(self.lab_num):
            self.labs.append(float(0))

    def find_n(self):
        n = 0
        found = False
        len_lab = len(self.labs)
        while n < len_lab:
            if self.labs[n] == 0:
                found = True
                break;
            n += 1
        if found:
            return n
        else:
            return len_lab + 10

    def make_lab(self, m, n = None):
        if n == None:
            n = self.find_n()
        if n > (len(self.labs) - 1):
            return self
        self.labs[n] = float(min(m, self.lab_max))
        return self

    def make_exam(self, m):
        self.exam_val = float(min(m, self.exam_max))
        return self

    def calc_total(self):
        self.total = float(0)
        for i in self.labs:
            self.total += i
        self.total += self.exam_val

    def is_certified(self):
        self.calc_total()
        if (self.total_max * self.k) <= self.total:
            return (self.total, True)
        else:
            return (self.total, False)
#************************************************
class Student1(object):
    name = ''
    marks = {}
    config = {}

    def __init__(self, name, config):
        self.name = name
        self.config = config
        self.marks = {}
        self.marks['exam'] = 0
        self.marks['labs'] = []
        for i in range(self.config['lab_num']):
            self.marks['labs'].append(0)

    def make_lab(self, mark, number=None):
        # оцінка не може бути більшою за оголошену в налаштуваннях курсу
        mark = min(mark, self.config['lab_max'])
        # якщо номер завдання не вказано, знайти перше завдання з нульовим рейтингом і оновити його рейтинг
        if number is None:
            if 0 in self.marks['labs']:
                self.marks['labs'][self.marks['labs'].index(0)] = mark
        # інакше, якщо існує завдання із таким номером, оновити його рейтинг
        elif number >= 0 and number < len(self.marks['labs']):
            self.marks['labs'][number] = mark
        return self

    def make_exam(self, mark):
        # оцінка не може бути більшою за оголошену в налаштуваннях курсу
        self.marks['exam'] = min(mark, self.config['exam_max'])
        return self

    def is_certified(self):
        # розрахувати можливий максимум
        total_max = self.config['exam_max'] + self.config['lab_max'] * self.config['lab_num']
        # взяти оцінку за екзамен
        sum = 1.0 * self.marks['exam']
        # і просумувати оцінки за практичні
        for i in range(len(self.marks['labs'])):
            sum = sum + min(self.config['lab_max'], self.marks['labs'][i])
        # повернути суму та порівняти з необхідним для сертифікату значення
        return (sum, sum >= total_max * self.config['k'])
#************************************************************
conf1 = {'exam_max': 20,'lab_max': 40,'lab_num': 2,'k': 0.75}
o2 = Student1('Oleg', conf1)
o2.make_lab(60).make_lab(35.2)

conf1 = {'exam_max': 20,'lab_max': 40,'lab_num': 2,'k': 0.75}
o3 = Student('Oleg', conf1)
o3.make_lab(10).make_lab(10).make_exam(15)
print o3.is_certified()
o3.make_lab(20,1).make_lab(20,0)
print o3.is_certified()
o3.make_lab(50,2)
