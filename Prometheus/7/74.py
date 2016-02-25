# -*- coding: utf-8 -*-
def create_calendar_page(month = 3,year = 2015):
    import calendar

    c = calendar.Calendar(0)
    dates = c.monthdayscalendar(year, month)

    titul = '-' * 20 + '\n'
    titul = titul + 'MO TU WE TH FR SA SU\n'
    titul = titul + '-' * 20 + '\n'

    row = 0
    col = 0
    str_dates = ''
    t = ''
    size_dates = len(dates)
    while row < size_dates:
        col = 0
        while col < 7:
            i = dates[row][col]
            if i == 0 and row < 4:
                str_dates = str_dates + '  '
            elif i != 0:
                t = '%02d' % i
                str_dates += t
            if col < 6:
                str_dates += ' '
            col += 1
        str_dates += '\n'
        row += 1
    str_dates1 = str_dates.rstrip(' \n')

    return titul + str_dates1

# імпорт необхідних класів з модуля datetime
from datetime import date, timedelta

def create_calendar_page1(month = None, year = None):
    # сьогоднішня дата
    today = date.today()
    # вибір сьогодняшніх місяця та року, якщо значення не передані
    month = month or today.month
    year  = year or today.year
    # формування дати першого дня шуканого місяця
    date_to_check = date(year, month, 1)
    # формування заголовку "сторінки", перенесення рядка за допомогою \n
    calendar = "--------------------\nMO TU WE TH FR SA SU\n--------------------\n"
    # формування кроку в 1 добу для зручного переходу між датами в циклі
    one_day = timedelta(1)
    i = 0
    # додаємо необхідну кількість пробілів перед першим днем місяця
    calendar += '   ' * date_to_check.weekday()
    # далі виводимо дні місяця по одному
    while date_to_check.month == month:
        # якщо перший день тижня, додати перехід на новий рядок
        if date_to_check.weekday() == 0:
            calendar += '\n'
        # форматування дати для відображення з нулем
        calendar += "%02d" % (date_to_check.day)
        # додаємо пробіл після дати, якщо це не останній день тижня
        if date_to_check.weekday() < 6:
            calendar += ' '
        # переходимо до наступного дня
        date_to_check = date_to_check + one_day
    # видаляємо зайвий пробіл в кінці
    if calendar[-1] == ' ':
        calendar = calendar[:-1]
    return calendar
m = 1
while m < 13:
    print str(m) + '\n'
    print create_calendar_page(m, 2015)
    print '\n'
    m += 1
#print create_calendar_page1()
#print create_calendar_page(1)
#print create_calendar_page(3)
#print create_calendar_page(04, 1992)