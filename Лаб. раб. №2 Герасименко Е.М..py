# Лаб работа №2
# Герасименко Екатерина, 100502-УБТа-о23, Вариант 6

import math as m
import sys

x = float(input('Введите значение х: '))
y = float(input('Введите значение y: '))
if y == 0:
    y = float(input('Выберите другое значение y: '))

f = float(input('\nВыберите функцию (номер): \n1) cos(0.5x) \n2) e^y \n3) ln(x/y) \n'))
b = None

match f:
    case 1:
        f = m.cos(0.5 * x)
    case 2:
        f = m.exp(y)
    case 3:
        f = m.log(x / y)
    case _:
        print('Некорректный выбор функции')
        sys.exit()

if 0.5 < (x * y) < 10:
    b = m.exp(f - abs(y))
elif 0.1 < x * y < 0.5:
    b = (abs(f + y)) ** (1/3)
else:
    b = 2 * (f ** 2)

print('\nРезультат: ', b)
