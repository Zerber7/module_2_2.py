first = int(input('Ввести первое число: '))
second = int(input('Ввести второе число: '))
third = int(input('Ввести третье число: '))

if first == second == third:
    print('Вывод: 3')
elif first == second or first == third or second == third:
    print('Вывод: 2')
elif first != second and first != third and second != third:
    print('Вывод: 0')
