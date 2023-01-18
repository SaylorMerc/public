answer = input('Какой язык программирования мы изучаем?')
if answer == 'Python':
    print('Верно! Мы ботаем Python =)')
    print('Python - отличный язык!')

answer = input('Какой язык программирования мы изучаем?')
    if answer == 'Python':
        print('Верно! Мы ботаем Python =)')
        print('Python - отличный язык!')
    else:
        print('Не совсем так!')


# Рассмотрим пример:
num1 = int(input())
num2 = int(input())

if num1 < num2:
    print(num1, 'меньше чем', num2)
if num1 > num2:
    print(num1, 'больше чем', num2)
if num1 == num2:                      # используем двойное равенство
    print(num1, 'равно', num2)
if num1 != num2:
    print(num1, 'не равно', num2)

# Следующий код проверяет, находится ли значение переменной age в диапазоне от 3 до 6:
age = int(input())
if 3 <= age <= 6:
    print('Вы ребёнок')
# Код, проверяющий равенство трех переменных, может выглядеть так:
if a == b == c:
    print('числа равны')
else:
    print('числа не равны')

# следующий код вовсе не проверяет тот факт, что все три переменные различны:

if a != b != c:
    print('числа не равны')
else:
    print('числа равны')
