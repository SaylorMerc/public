# Напишите программу, которая определяет наименьшее из четырёх чисел.

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
minimum = num1
if minimum > num2:
    minimum = num2
if minimum > num3:
    minimum = num3
if minimum > num4:
    minimum = num4
print(minimum)