from datetime import date
import calendar


birth_day = int(input('Введите ваш день рождения: '))
birth_month = int(input('Введите ваш месяц рождения: '))
birth_year = int(input('Введите ваш год рождения: '))
# input----------------------------------------------------------

# вычилсяет день недели рождения
def get_weekday(day, month, year):
    week_number = date(year, month, day).weekday()
    all_week_days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
    return all_week_days[week_number]


# вычисляет високосный ли год
def is_leap_year(year):
    if calendar.isleap(year):
        print ('Вы родились в високосный год.')
    else:
        print ('Вы родились в невисокосный год.')


# вычисляет возраст
def user_age(birth_day, birth_month, birth_year):
    today = date.today()
    age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))
    return age

# вывод табло
def print_birthday():
    number_patterns = {
        '0': ['***', '* *', '* *', '* *', '***'],
        '1': [' * ', '** ', ' * ', ' * ', '***'],
        '2': ['***', '  *', '***', '*  ', '***'],
        '3': ['***', '  *', '***', '  *', '***'],
        '4': ['* *', '* *', '***', '  *', '  *'],
        '5': ['***', '*  ', '***', '  *', '***'],
        '6': ['***', '*  ', '***', '* *', '***'],
        '7': ['***', '  *', '  *', '  *', '  *'],
        '8': ['***', '* *', '***', '* *', '***'],
        '9': ['***', '* *', '***', '  *', '***']
    }

    # Дата рождения без точек, добавляем ведущий ноль к месяцу
    all_digits = f'{birth_day}{birth_month:02}{birth_year}'

    # Выводим каждую строку звездочек
    for line in range(5):
        for digit in all_digits:
            print(number_patterns[digit][line], end='  ')
        print()  # переводит каждую строку цифр в новую строку


# output----------------------------------------------------------
print('______________________________________________________________')
print(f'Вы родились {birth_year}.{birth_month:02}.{birth_day} г.')

week_day = get_weekday(birth_day, birth_month, birth_year)
print(f'это был/а {week_day}')

is_leap_year(birth_year)

age = user_age(birth_day, birth_month, birth_year)
print(f'Ваш возраст: {age}')

print_birthday()
print('______________________________________________________________')