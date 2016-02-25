# -*- coding: utf-8 -*-
def bouquets(narcissus_price, tulip_price, rose_price, summ):
    buket = 0 #кількість букетів
    #початкові значення для циклів
    arr = []
    arr.append(narcissus_price)
    arr.append(tulip_price)
    arr.append(rose_price)
    arr.sort()
    kv1 = arr[2]
    kv2 = arr[1]
    kv3 = arr[0]
    #макс кількість квітів
    max_Kv1 = int(summ / kv1)
    max_Kv2 = 0
    max_Kv3 = 0
    #вартість квітів
    summ_kv1 = 0
    summ_kv2 = 0
    summ_kv12 = 0
    #кількість квітів у букеті
    sum_kv = 0
    k1, k2, k3 = 0, 0, 0
    start = 0 #перший елемент останнього циклу

    for k1 in range(max_Kv1 + 1):
        k2 = 0
        k3 = 0
        summ_kv1 = k1 * kv1
        max_Kv2 = int((summ - summ_kv1) / kv2)

        for k2 in range(max_Kv2+1):
            k3 = 0
            summ_kv2 = k2 * kv2
            summ_kv12 = summ_kv1 + summ_kv2
            max_Kv3 = int((summ - summ_kv12) / kv3)
            sum_kv = k1 + k2
            start = 1 #парна кількість
            if(sum_kv % 2) != 0:
                start = 0 #непарна кількість

            if max_Kv3 > 1 or (max_Kv3 == 1 and start == 1):
                for k3 in range(start, max_Kv3 + 1, 2):
                    buket += 1

            if k3 == 0 and max_Kv2:
                sum_kv = k1 + k2
                if(sum_kv % 2) != 0:
                    buket += 1

        if k2 == 0 and k3 == 0:
            if(k1 % 2) != 0:
                buket += 1

    return buket
#**********************************************
def bouquets1(narcissus_price, tulip_price, rose_price, limit):
    # розв'язок писався, коли умова знаходилася на рівні абстракції "квітка1", "квітка2", "квітка3",
    # це ще й зручніше, так як цифрові індекси в коді сприймаються легше
    fp1 = narcissus_price
    fp2 = tulip_price
    fp3 = rose_price
    # лічильник
    counter = 0

    # перебір
    # кожної квітки в букеті може бути мінімум 0, максимум - стільки, скільки залишилося грошей
    # якщо в букеті вже є якісь квіти, частина грошей вже витрачена на них - це обмежує перебір
    for f1 in range(1+int(1.0 * limit / fp1)):
        for f2 in range(1+int((1.0 * limit - f1*fp1) / fp2)):
            for f3 in range(1+int((1.0 * limit - f1*fp1 - f2*fp2) / fp3)):
                # в процесі відлагодження програми тут було виведення варіантів, що перебираються
                # print f1, f2, f3, '=', (f1+f2+f3) % 2, '|', f1*fp1, f2*fp2, f3*fp3, '=', f1*fp1 + f2*fp2 + f3*fp3
                # якщо кількість квітів непарна, збільшити лічильник
                # суму перевищити неможливо, так як це обмеження закладено вже в циклі
                if (f1+f2+f3) % 2:
                    counter += 1
    return counter
#***********************************************
print bouquets(15.5,4.1,5.99,21.75) # 8
print bouquets(21.25,13.6,10.5,100) # 51
print bouquets(1,1,1,5) # 34
print bouquets(2,3,4,10) # 12
print bouquets(2,3,4,100) # 4019
print bouquets(200,300,400,10000) # 4019
print bouquets(200,300,400,100000) # 3524556