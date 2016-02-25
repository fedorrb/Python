# -*- coding: utf-8 -*-
def find_most_frequent(text):
    text = str(text)
    text = text.lower()
    text2 = ''
    slovnik = {}
    max_repeat = 0
    split_char = [',','.',':',';','!','?','-',' ']
    for c in text:
        if (c in split_char) == False:
            text2 = text2 + c
        else:
            text2 = text2 + ' '
    text = str(text2)
    text = text.split(' ')
    text.sort()
    for slovo in text:
        if len(slovo) == 0:
            continue;
        else:
            if slovnik.has_key(slovo):
                slovnik[slovo] = slovnik[slovo] + 1
                if max_repeat < slovnik[slovo]:
                    max_repeat = slovnik[slovo]
            else:
                slovnik[slovo] = 1
                if max_repeat < 1:
                    max_repeat = 1
    text = []
    for slovo in slovnik:
        if slovnik[slovo] == max_repeat:
            text.append(slovo)
    text.sort()
    return text
def find_most_frequent1(text):
    # якщо текст порожній - нема чого шукати
    if text == '':
        return []
    # видаляємо розділові знаки, змінюємо регістр та перетворюємо рядок у список слів
    text_list = text.replace(',', ' ').replace('.', ' ').replace(':', ' ').replace(';', ' ').replace('!', ' ').replace('?', ' ').replace('-', ' ').lower().split()
    # створюємо словник, де для кожного унікального слова зберігатимемо кількість його входжень.
    counts = dict()
    word = ''
    # для кожного слова в списку
    for word in text_list:
        # якщо воно вже присутнє у словнику
        if word in counts:
            # збільшуємо його лічильник на 1
            counts[word] = counts[word] + 1
        else:
            # інакше додаємо у словник
            counts[word] = 1

    # беремо останнє оброблене слово і вважаємо його найчастіше вживаним
    max_word = [word]
    # перевіряємо слова условнику, шукаючи слово із найбільшим лічильником
    for word in counts:
        # якщо знаходиме частіше вживане слово, зберігаємо його як єдиний елемент списка "лідерів"
        if counts[word] > counts[max_word[0]]:
            max_word = [word]
        # якщо знаходимо слово з аналогічною вживаністю, додаємо у список
        elif counts[word] == counts[max_word[0]] and word != max_word[0]:
            max_word.append(word)
    # повертаємо список слів-"лідерів"
    return max_word
#text1 = 'Hello,Hello, my dear!'
#text1 = 'to understand recursion you need first to understand recursion...'
#text1 = 'Mom! Mom! Are you sleeping?!!!'
text1 = 'zz! xx! aa bb ck dk ek fk gk hk ik jk kk ll'
#print find_most_frequent(text1)
print find_most_frequent1(text1)
