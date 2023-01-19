# Напишите программу, которая определяет наименьшее из двух чисел.
num1 = int(input())
num2 = int(input())
if num2 - num1 < 0:
    print(num2)
else:
    print(num1)