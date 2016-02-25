﻿# -*- coding: utf-8 -*-
def karatsuba(x,y):
    """ Функция умножения х на у методом Кацубы """
    if len(x)%2!=0 and len(x)!=1:
        x='0'+x
    if len(y)%2!=0 and len(y)!=1:
        y='0'+y
        """ Проверяем значения х и у на четное количество символов, и
при необходимости добавляем 0 перед значением. Значения длинной 1
являются исключениями."""
    while len(x)>len(y):
        y='0'+y
    while len(x)<len(y):
        x='0'+x
        """ Выравниваем количество цифр в х и у, добавлением 0 перед значением
до тех пор пока количество цифр не будет совпадать """
    n=len(x) # количество символов в переменной (они одинаковы по этому параметру)
    if n==1:
        print('x =',x,'y =',y)
        return int(x)*int(y)
        """ Если символов в значениях - 1 мы перемножаем их и выводим значение """
    else:
        a=x[:int(len(x)/2)]
        b=x[int(len(x)/2):]
        c=y[:int(len(y)/2)]
        d=y[int(len(y)/2):]
        print('x =',x,'y =',y,'n =',n,'a =',a,'b =',b,'c =',c,'d =',d)
        """ Получаем значения переменных a b c d по средством срезов чисел,
тоесть а равно все числа числа х(у которого индекс 0) до числа с индексом
равном половине длинны - это как раз разделяет числа на равное количество
символом"""
        ac=int(karatsuba(a,c))
        bd=int(karatsuba(b,d))
        """ Рекрусивно просчитываем значения a*c и b*d """
        a_b=str(int(a)+int(b))
        c_d=str(int(c)+int(d))
        """ Получаем сумму a+b c+d чтобы передать их функции дальше"""
        ad_plus_bc=-int(ac)-int(bd)+int(karatsuba(a_b,c_d))
        print('ac =',ac,'bd =',bd,'ad+bc =',ad_plus_bc)
        """ Рекрусивно просчитываем значение a*d+b*c (сразу считая его целиком)"""
        if ad_plus_bc==105:
            z[0]=int(z[0])+1
        if ad_plus_bc==72:
            z[1]=int(z[1])+1
        if ad_plus_bc==12:
            z[2]=int(z[2])+1
        """ Ищем совпадения значений которые указаны в задании и повышаем соответствующую
позицию списка на 1 при совпадении """
        unswer=(10**n)*ac+(10**int((n/2)))*ad_plus_bc+bd
        """ Собственно само умножение по формуле Кацубы и вывод результата """
        return int(unswer)

X=1685287499328328297814655639278583667919355849391453456921116729
Y=7114192848577754587969744626558571536728983167954552999895348492
""" Наши переменные """
z=[0,0,0]
""" Список который хранит значения ответов на поиск совпадений """
X=str(X)
Y=str(Y)
""" Превращаем переменную из числа в текст """
print('X =',X,'\nY =',Y)
X_Y=karatsuba(X,Y)
""" Задействуем метод Кацубы """
if (int(X_Y)-int(X)*int(Y))==0:
    print('Сошлось')
    print('X*Y =',int(X_Y))
    print('ad+bc=105 -',z[0],'\n'+'ad+bc=72 -',z[1],'\n'+'ad+bc=12 -',z[2])
    """ Выводим в случае успеха "Сошлось", результат умножения и количество совпадений"""
else:
    print("не сошлось на", int(X_Y)-int(X)*int(Y))
    """ В случае неудачи выводим результат на который не сошлось решение"""