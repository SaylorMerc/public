# Напишите программу, которая принимает целое число xx и определяет, принадлежит ли данное число указанному промежутку.

x = int(input())

if x <= -3 or x >= 7:
    print('Принадлежит')
else:
    print('Не принадлежит')