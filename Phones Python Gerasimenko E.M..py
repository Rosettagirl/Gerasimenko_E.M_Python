import re
def normal_number(phone):
    phone = re.sub(r'\D', '', phone)

    if phone.startswith('7'):
        code = phone[1:4]
        number = phone[4:]

    elif phone.startswith('8'):
        code = phone[1:4]
        number = phone[4:]

    else:
        code = '495'
        number = phone

    return str(code) + str(number)

new_phone = normal_number(input('Введите новый номер телефона: ').strip())

print('Теперь введите номера телефонов из телефонной книги: ')
next_numbers = []
for i in range(3):
    number = normal_number(input('').strip())
    next_numbers.append(number)

for number in next_numbers:
    if number == new_phone:
        print('YES')
    else:
        print('NO')