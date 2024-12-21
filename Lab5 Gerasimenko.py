# Лаб работа №5
# Герасименко Екатерина, 100502-УБТа-о23, Вариант 6

# Задание 1
numbers = input('Первое задание.'
                '\nВведите целые числа через пробел: ', ).split()
numbers = [int(num) for num in numbers]

max_num = max(numbers)
nums_little = 0
nums_more = 0

for num in numbers:
    if num < max_num:
        nums_little += 1
    if num > max_num:
        nums_more += 1

print('Максимальный элемент в списке: ', max_num,
      '\nКоличество чисел, которые меньше максимального: ', nums_little,
      '\nКоличество чисел, которые больше максимального: ', nums_more)

# Задание 2
numbers = input('\nВторое задание.'
                '\nВведите целые числа через пробел: ', ).split()
numbers = [int(num) for num in numbers]

numbers_more_five = []

for num in numbers:
    if num > 5:
        numbers_more_five.append(num)

sum = sum(numbers_more_five)
print('Сумма чисел, которые больше 5: ', sum)