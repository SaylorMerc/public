# Дан порядковый номер месяца. Напишите программу, которая выводит на экран количество дней в этом месяце.
# Принять, что год является невисокосным.

a = int(input())
if a == 4 or a == 6 or a == 9 or a == 11:
    print('30')
elif a == 2:
    print('28')
else:
    print('31')