# -*- coding: utf-8 -*-
class SuperStr(str):

    def is_repeatance(self, s):
        if type(s) != str:
            return False
        if len(s) == 0:
            return False
        len_stroka = len(self)
        if len_stroka == 0:
            return False
        s_count = self.count(s)
        if len_stroka == s_count * len(s):
            return True
        return False

    def is_palindrom(self):
        flag = True
        s_cleaned = self.lower()
        s_length = len(s_cleaned)
        for i in range(s_length / 2):
            if s_cleaned[i] != s_cleaned[s_length-1-i]:
                flag = False
        return flag
#**********************************************
# власне, єдина проблема - наслідувати клас від стандартного str
class SuperStr1(str):
    def is_repeatance(self, substring):
        # спробуємо перевернути рядок
        try:
            if len(substring) == 0 or len(self) == 0:
                return False
            multiplier = len(self) / len(substring)
            return self == substring * multiplier
        # якщо помилка - тип аргументу не підходить
        except TypeError:
            return False

    def is_palindrom(self):
        try:
            return self.lower() == self[::-1].lower()
        except TypeError:
            return False
#*****************************************************
s1 = SuperStr('678678678678')
print s1.is_repeatance('6786') #false
print s1.is_repeatance('678') #true
print s1.is_repeatance('678678') #true
print s1.is_repeatance('678678678') #false
print s1.is_repeatance('q') #false
print s1.is_repeatance('') #false
print s1.is_repeatance(678) #false
print s1.is_repeatance([]) #false
print s1.is_repeatance([678]) #false
print s1.is_palindrom() #false
print s1.isdigit() #true
int(s1) #678678678678
print '("' + s1 + '")' #("678678678678")
s2 = SuperStr('')
print s2.is_repeatance('') #false
print s2.is_repeatance('a') #false
print s2.is_palindrom() #true
print bool(s2) #false
s3 = SuperStr('mystring1Gnirtsym')
print s3.is_repeatance('my') #false
print s3.is_repeatance('q,.%;#') #false
print s3.is_palindrom() #true
print s3.lower()
print s3
s4 = SuperStr('q')
print s4.is_repeatance('') #false
print s4.is_repeatance('q') #true
print s4.is_palindrom() #true
print s4.upper() #Q