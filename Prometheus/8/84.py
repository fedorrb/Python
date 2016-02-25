# -*- coding: utf-8 -*-
def make_sudoku(size):
    sudoku = []
    size_sud = size ** 2
    arr = range(1,size_sud + 1)

    def moveSize(arr):
        new_arr = arr[size:] + arr[:size]
        return new_arr

    def move1(arr):
        new_arr = arr[1:] + arr[:1]
        return new_arr

    for i in range(size_sud):
        sudoku.append(arr)
        if (i+1) % size == 0:
            arr = move1(arr)
        else:
            arr = moveSize(arr)

    return sudoku
#*********************************************
# після спроби скласти вручну (на папері) судоку розмірностей 2, 3, 4 можна помітити,
# що достатньо побудувати перші size квадратів, а інші можна отримати з них зсувом вліво або вправо
# всередині перших size квадратів перший рядок може бути записаний довільним чином (наприклад, числа послідовно)
# інші рядки.. також можна отримати зсувом, лише на цілий квадрат
# до речі, схожий евристичний алгоритм можна знайти і в інтернеті
def make_sudoku1(size):
    s = []
    # заповнюємо перші квадрати
    # замість обчислення полів по одному, в список-рядок можна генерувати готові шматки за допомогою range()
    for i in range(size):
        s.append(range(i * size + 1, size**2 + 1))
        s[i].extend(range(1, i * size +1))
    # для того, щоб не мучитися далі з додаванням елементів до списку, створимо їх одразу тут, заповнимо нулями
    for i in range(size, size**2):
        s.append([])
        for j in range(size**2):
            s[i].append(0)

    # тепер заповнюємо "нулі", копіюючи числа з попередніх квадратів "по діагоналі"
    # здається, тут можна було обійтися 2 циклами, не розмежовуючи окремі квадрати між собою
    for i in range(1,size):
        for j in range(0,size):
            for ii in range(0, size**2):
                s[i*size + j][ii] = s[(i-1)*size + j][(ii+1)%(size**2)]

    return s
#*********************************************

print make_sudoku(2)
print make_sudoku1(2)
