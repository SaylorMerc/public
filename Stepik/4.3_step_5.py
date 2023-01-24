# Даны три различных целых числа. Напишите программу, которая находит среднее по величине число.

a, b, c = int(input()), int(input()), int(input())
if (b < a < c) or (b > a > c):
    print(a)
elif (a < b < c) or (a > b > c):
    print(b)
elif (b < c < a) or (b > c > a):
    print(c)