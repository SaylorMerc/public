# Напишите программу, которая считывает с клавиатуры одно число и выводит обратное ему.
# Если при этом введённое с клавиатуры число – ноль, то вывести «Обратного числа не существует» (без кавычек).
x = float(input())
if x == 0:
    print('Обратного числа не существует')
else:
    y = x ** -1
    print(y)