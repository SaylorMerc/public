# Заданы две клетки шахматной доски. Напишите программу, которая определяет имеют ли указанные клетки один цвет или нет.
# Если они покрашены в один цвет, то выведите слово «YES», а если в разные цвета — то «NO».

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if (x1 + x2 + y1 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')