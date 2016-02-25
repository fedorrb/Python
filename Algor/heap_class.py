# -*- coding: utf-8 -*-
#купа (піраміда)
class Heap1(object):
    arr = []
    growing = 0

    #конструктор
    def __init__(self, g = 0):
        self.arr = []
        if g != 0:
            self.growing = 1 #незростаюча
        else:
            self.growing = 0 #неспадна

    #лівий нащадок
    def Left(self, i):
        return i * 2

    #правий нащадок
    def Right(self, i):
        return i * 2 + 1

    #батько
    def Parent(self, i):
        return i / 2

    #підтримка властивості незростаючої піраміди
    def MaxHeapify(self, i):
        p = self.Left(i)
        q = self.Right(i)
        #номера елементів -> індекси елементів
        p -= 1
        q -= 1
        i -= 1

        heap_size = len(self.arr)
        largest = 0
        if p <= heap_size-1 and int(self.arr[p]) > int(self.arr[i]):
            largest = p
        else:
            largest = i
        if q <= heap_size-1 and int(self.arr[q]) > int(self.arr[largest]):
            largest = q
        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.MaxHeapify(largest + 1)

    #підтримка властивості неспадної піраміди
    def MinHeapify(self, i):
        p = self.Left(i)
        q = self.Right(i)
        #номера елементів -> індекси елементів
        p -= 1
        q -= 1
        i -= 1

        heap_size = len(self.arr)
        lowest = 0
        if p <= heap_size-1 and int(self.arr[p]) < int(self.arr[i]):
            lowest = p
        else:
            lowest = i
        if q <= heap_size-1 and int(self.arr[q]) < int(self.arr[lowest]):
            lowest = q
        if lowest != i:
            self.arr[i], self.arr[lowest] = self.arr[lowest], self.arr[i]
            self.MinHeapify(lowest + 1)

    #побудова незростаючої піраміди
    def BuildMaxHeap(self):
        half = len(self.arr) / 2
        i = half
        while i > 0:
            MaxHeapify(i)
            i -= 1

    #Maximum or Minimum
    def GetFirstElement(self):
        len_arr = len(self.arr)
        if len_arr:
            return self.arr[0]
        else:
            return 0

    #heap_size
    def GetCountElements(self):
        return len(self.arr)

    #ExtractMax or Min
    def PopFirstElement(self):
        i1 = self.arr[0]
        i2 = self.arr.pop()
        self.arr[0] = i2
        if self.growing == 1:
            self.MaxHeapify(1)
        else:
            self.MinHeapify(1)
        return i1

    #знаходження позиції для доданого елементу
    def HeapIncreaseKey(self, x, key):
        self.arr[x-1] = key
        if self.growing == 1:
            while x > 1 and int(self.arr[self.Parent(x)-1]) < int(self.arr[x-1]):
                self.arr[x-1], self.arr[self.Parent(x)-1] = self.arr[self.Parent(x)-1], self.arr[x-1]
                x = self.Parent(x)
        else:
            while x > 1 and int(self.arr[self.Parent(x)-1]) > int(self.arr[x-1]):
                self.arr[x-1], self.arr[self.Parent(x)-1] = self.arr[self.Parent(x)-1], self.arr[x-1]
                x = self.Parent(x)

    #додавання елементу до піраміди
    def HeapInsert(self, key):
        self.arr.append(key)
        self.HeapIncreaseKey(self.GetCountElements(), key)