# Лаб работа №4
# Герасименко Екатерина, 100502-УБТа-о23, Вариант 6

str = input("Введите строку -> ")
n = len(str)
n2 = n//2
for i in str:
    if i == 'п':
        str1 = str[:n2].replace(i, '*')
str = str1 + str[n2:]
print('Полученная строка: ', str)
