# -*- coding: utf-8 -*-
import os, sys, copy

#клас вузла для дерева
class Node():
    def __init__(self, value = None):
        self.left = None
        self.right = None
        self.parent = None
        self.value = None
        if value:
            self.value = value

#клас бінарного дерева пошуку
class BinTreeSearch():
    def __init__(self, value = None):
        self.root = Node(value)
        self.arr = []

    #додавання значення в дерево
    def Tree_Insert(self, value):
        z = Node(value)
        y = None
        x = self.root
        while x.value != None:
            y = x
            if value <= x.value:
                x = x.left
            else:
                x = x.right
            if type(x) == type(None):
                x = Node()
        #z.parent = y
        if y == None:
            self.root.value = value
        else:
            if value < y.value:
                y.left = z
            else:
                y.right = z
    #прохід по дереву в відсортованному порядку
    def InorderTreeWalk(self, node):
        if isinstance(node, Node):
            if node.value != None:
                self.InorderTreeWalk(node.left)
                #print node.value
                if node.left == None and node.right == None:
                    print node.value
                self.arr.append(node.value)
                self.InorderTreeWalk(node.right)

    #прохід по дереву в відсортованному порядку  з підрахунком сум
    def InorderTreeWalkSum(self, node):
        c = 1940
        z = Node()
        if isinstance(node, Node):
            if node.value != None:
                self.InorderTreeWalkSum(node.left)

                if node.left == None and node.right == None:
                    self.arr = []
                    z = node
                    while z.parent:
                        self.arr.append(z.value)
                        if sum(self.arr) == c:
                            print str(c) + ' = ' + str(self.arr)
                        while sum(self.arr) > c:
                            self.arr.pop(0)
                        if sum(self.arr) == c:
                            print str(c) + ' = ' + str(self.arr)
                        z = z.parent

                    self.arr.append(z.value)
                    if sum(self.arr) == c:
                        print str(c) + ' = ' + str(self.arr)
                    while sum(self.arr) > c:
                        self.arr.pop(0)
                    if sum(self.arr) == c:
                        print str(c) + ' = ' + str(self.arr)

                self.InorderTreeWalkSum(node.right)

    #пошук вузла по значенню к
    def TreeSearch(self, node, k):
        result = None
        if isinstance(node, Node):
            if node.value == k:
                result = node
            elif node.value > k:
                result = self.TreeSearch(node.left, k)
            else:
                result = self.TreeSearch(node.right, k)
        return result

    #пошук вузла по значенню к без рекурсії
    def IterativeTreeSearch(self, node, k):
        while isinstance(node, Node) and node.value != k:
            if k < node.value:
                node = node.left
            else:
                node = node.right
        return node

    def TreeMinimum(self, node):
        while node and node.left:
            node = node.left
        return node

    def TreeMaximum(self, node):
        while node and node.right:
            node = node.right
        return node

    #повертає вузол який є наступним за node
    def TreeSuccessor(self, node):
        if node:
            if node.right:
                return self.TreeMinimum(node.right)
            y = self.GetParent(node)
            while y and node == y.right:
                node = y
                y = self.GetParent(y)
            return y
        else:
            return None

    #якщо не реалізовувати self.parent
    #пошук батьківського вузла
    def GetParent(self, node):
        if node:
            root_node = self.root
            if node == root_node:
                return None
            while root_node:
                if node == root_node.left:
                    break
                if node == root_node.right:
                    break
                if node.value <= root_node.value:
                    root_node = root_node.left
                else:
                    root_node = root_node.right
            return root_node
        else:
            return None

    def TreeDelete(self, node):
        pass

    #побудувати бінарне дерево з заданого масиву
    def BuildTree(self, values):
        y = None
        x = self.root
        r = 0
        for i in values:
            if i > 0:
                if x.value == None:
                    x.value = i
                    continue
                else:
                    z = Node(values[0])
                    z.value = i
                    if r > 1:
                        x = x.parent
                        r = r - 2
                        if x == None:
                            return self.root
                        while x.right != None:
                            x = x.parent
                        while r > 1:
                            x = x.parent
                            r = r - 1
                        while x.right != None:
                            x = x.parent
                        if r == 1:
                            x = x.parent
                            while x.right != None:
                                x = x.parent
                        if x == None:
                            return self.root
                        r = 1
                    if r == 1:
                        x.right = z
                        r = 0
                    else:
                        x.left = z
                    z.parent = x
                    x = z
            else:
                r += 1
        return self.root

    #побудувати бінарне дерево пошуку з заданого дерева
    def MakeSearchTree(self, node, i):
        if isinstance(node, Node):
            if node.value != None:
                i = self.MakeSearchTree(node.left, i)
                node.value = self.arr[i]
                i += 1
                i = self.MakeSearchTree(node.right, i)
            return i
        return i

f = open(r"input_1000a.txt","r").read()
A = f.split(' ')
B = []
i = 0
len_A = len(A)
while i < len_A:
    B.append(int(A[i])) #масив цілих чисел
    i += 1
t = BinTreeSearch()
t.BuildTree(B)
t.arr = []
t.InorderTreeWalk(t.root)
t.arr.sort()
t.MakeSearchTree(t.root, 0)
print 'sorted\n'
t.InorderTreeWalk(t.root)
t.InorderTreeWalkSum(t.root)
