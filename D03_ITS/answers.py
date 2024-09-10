#1
number_1 = 3
number_2 = number_1 ** 2 + 10 / 5
number_3 = number_1 + number_2 % 2 + 1
number_4 = number_1 // 3 + number_3

print(number_4)
#2 
"""
Пример кода с ошибкой № 2

Не забудь изучить операции со строками - "+" и "*"
"""


string_1 = 'Не знаю заметил ты или нет, но строки можно то записывать с помощью трех видов кавычек'
string_2 = "Прошлая строка записана в одинарных кавычках, а вот эта в двойных"
string_3 = """
А это что за монстр?
Да, многострочная строка... Она записывается с помощью тройных кавычек.
"""

string_4 = "Как говаривал один мой знакомый"

string_5 = ' по поводу кавычек в питоне:"Да какая разница, какие использовать? Что вообще может пойти не так?"'

string_6 = string_4 + string_5

string_7 = " Да и в целом то я с ним согласен. Кажется, что никаких проблем быть не должно."

string_8 = '-' * 50
string_9 = string_8 + string_7

print(string_6)
print(string_9)

#3
"""
Пример кода с ошибкой № 3
"""


string = ' I like administration of hospital   '

exclamation_point ='!'
exclamation_point*=3  # О, кстати популярный метод записи операций - '*=', '+=', '-=' и т.д. Изучи такие записи.

string=string.strip()  # И не стесняйся гуглить неизвестные методы
string= string[:12].upper()

print(f'{string}{exclamation_point} Ох, так неожиданно и прияяятноооо.')

#4
input_int = input("Введите целое число: ")

if input_int.isdigit():
    print(f'Твое число в степени два равно {int(input_int)**2}')
else:
    print('Ну я же просил ввести целое число! Ну камон!')

input_str = input("А теперь напиши еще раз это число и добавь к нему букву: ")
if input_str.isdigit():
    print(f'Вы ввели число {input_str}')
else:
    print(f'{input_str} - это не число')

#5
from random import randint
import math

input_number = int(input('Введите целое число от -10 до 10: '))

random_number = randint(-10, 10)
print(f'Случайное число = {random_number}')

difference_numbers = input_number - random_number
print(f'{input_number} - ({random_number}) = {difference_numbers}')

if difference_numbers >= 0:
    sqlt_number = round(math.sqrt(difference_numbers), 2)
    print(f'Корень из {difference_numbers} = {sqlt_number}')
else:
    print(f'Корень из {difference_numbers} не существует, т.к. число отрицательное')

#6
import sys

print('Программа для визуализации работы индексов\n')
test_string = 'Тестовая строчка'
print(test_string)

is_index_flag = bool(int(input('\nВведи\n - 0, если хочешь прекратить программу;\n - 1, если хочешь задать индекс.\n')))

if is_index_flag:
    index = int(input('Введи индекс: '))
    if 0 <= index < len(test_string):
        print(f'Элемент, стоящий под этим индексом - "{test_string[index]}"')
    else:
        print('Индекс вне диапазона строки')
else:
    sys.exit()

#7
print('Программа для визуализации работы индексов\n')
test_string = 'Тестовая строчка'
print(f'{test_string}\n')

ind_1 = input(
    'Введи первый индекс среза (или нажми Enter - это будет означать, что срез берется с начала строки): '
)
ind_2 = input(
    'Введи второй индекс среза (или нажми Enter - это будет означать, что срез берется до конца строки): '
)
step = input(
    'Введи шаг среза (или нажми Enter - это будет означать, что шаг по-умолчанию равен 1): '
)

# Проверяем, не пустая ли строка в ind_1, ind_2, step. Если нет, то переводим в число эти переменные.
if ind_1:
    ind_1 = int(ind_1)
else:
    ind_1 = 0
if ind_2:
    ind_2 = int(ind_2)
else:
    ind_2 = len(test_string)
if step:
    step = int(step)
else:
    step = 1

# Напиши свой код тут, остальной код не трогай

print('\nТвой срез:')
if ind_1 > ind_2:
    print("Ошибка: индекс начала среза не может быть больше индекса конца среза")
else:
    print(test_string[ind_1:ind_2:step])