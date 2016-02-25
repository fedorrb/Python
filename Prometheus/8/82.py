# -*- coding: utf-8 -*-
def find_fraction(summ):
    def gcd(a, b):
        t = 0
        while b != 0:
            t = b
            b = a % b
            a = t
        return a

    c = summ / 2
    z = summ - c
    if c == z:
        c -= 1
        z += 1
    if c <= 0:
        return False
    while 1:
        d = gcd(c, z)
        if d == 1 or c <= 1:
            break
        else:
            c -= 1
            z += 1

    return (c, z)
#***********************************
def find_fraction1(summ):
    # для зручності створимо ще 1 функцію для перевірки, чи є дріб правильним і нескорочуваним
    def is_ok(t, b):
        if t >= b or (b % t == 0 and t != 1):
            return False
        # тут можна було б застосувати алгоритм пошуку найбільшого спільного дільника
        # але в силу специфіки задачі ця функція буде викличена лише 2-3 рази, тому зробимо простіше
        for i in range(2, int(t**0.5)):
            if t % i == 0 and b % i == 0:
                return False
        return True

    # правильний дріб тим більший, чим менша різниця між його чисельником та знаменником
    # тож прирівняти кожний з них половині заданої суми - оптимальна точка для початку пошуку
    top = summ / 2
    bottom = summ - top
    # далі цю точку "зсувати" в сторони зменшення чисельника, поки отриманий дріб не задовольнятиме всім умовам
    while top > 0 and not is_ok(top, bottom):
        top -= 1
        bottom += 1
    # якщо значення чисельника досягло нуля, дріб не знайдено
    if top > 0:
        return (top, bottom)
    else:
        return False
print find_fraction(0)
print find_fraction(1)
print find_fraction(2)
print find_fraction(3)
print find_fraction(6)
print find_fraction(10)
print find_fraction(62)
print find_fraction(150000001)

