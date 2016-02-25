# -*- coding: utf-8 -*-
class CombStr(object):

    def __init__(self, stroka):
        self.stroka = stroka

    def count_substrings(self, length):
        lenStr = len(self.stroka)
        if length > lenStr or length == 0:
            return 0
        if length == lenStr:
            return 1
        s = set()
        i = 0
        endWhile = lenStr - length
        while i <= endWhile:
            s.add(self.stroka[i:i+length])
            i += 1
        return len(s)
#********************************************
class CombStr1(object):
    # конструктор
    def __init__(self, string):
        self.string = string

    # метод пошуку підрядків
    def count_substrings(self, length):
        length = int(length)
        # виключення
        if length < 1:
            return 0
        # список знайдених підрядків
        found = []
        # проходимо по рядку
        for i in range(len(self.string) - length + 1):
            # виділяючи з нього підрядок довжиною length, починаючи з і-го символу
            sub = self.string[i:i+length]
            # якщо він є унікальним, додаємо в список знайдених
            if sub not in found:
                found.append(sub)
        # кількість підрядків = довжині списку знайдених
        return len(found)

s0 = CombStr('qqqqqqweqqq%')
print s0.count_substrings(0)
print s0.count_substrings(1)
print s0.count_substrings(2)
print s0.count_substrings(5)
print s0.count_substrings(15)