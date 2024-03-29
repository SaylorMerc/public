# пусть a и b - переменные, которые мы хотим проверить
# a = int(input("введите переменную а: "))
# b = int(input("введите переменную b: "))
# if a and b:  # проверка истинности обеих переменных
# print("Обе переменные истинные")
# print(a, b)
# elif a or b:
# print("Одна из переменных истинная")
# print(a or b)  # печать одной переменной, той, которая является истинной
# else:
# print("Обе переменные ложные")


a = int(input())
if type(a) == int:
    if 100 <= a <= 999:
        if a % 2 == 0:
            if a % 3 == 0:
                print("Число удовлетворяет условиям")
else:
    print("Число не удовлетворяет условиям")

if type(a) == int and 100 <= a <= 999 and a % 2 == 0 and a % 3 == 0:
    print("Число удовлетворяет условиям")

# И ответ — да, можно. В Python есть функция all([ ]), которая возвращает True, если все условия, переданные в
# аргумент функции в виде списка, являются истинными.

if all([type(a) == int,
        100 <= a <= 999,
        a % 2 == 0,
        a % 3 == 0]):
    print("Число удовлетворяет условиям")
else:
    print("Число не удовлетворяет условиям")

# Функция all([ ]) возвращает True, если все элементы списка являются истинными. А что если нужно, чтобы был хотя бы
# один истинный? Тогда на помощь приходит функция any([ ]). Ее работа аналогична рассмотренному выше примеру.

# Напишите программу, которая на вход принимает последовательность целых чисел, и возвращает True, если все числа ненулевые, и False, если хотя бы одно число равно 0.
L = list(map(int, input().split()))

print(all(L))
