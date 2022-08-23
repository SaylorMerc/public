def local():
    x = 5  # локальная переменная
    print(x)


x = 10
local()
print(x)


# 5
# 10

def local():
    print(x)  # так как x нет в локальной области видимости, мы берем её из глобальной области


x = 10
local()
print(x)

# 10
# 10

x = 3


def function():
    print(x)
    return x


print(function())

x = 3


def func():
    # print(x) - ошибка, так как х еще не определен
    global x
    x = 5
    x += 5
    return x


func()
print(func())


def get_my_func():
    def hello_world():
        print("Hello")

    return hello_world


hello_world_func = get_my_func()  # получить функцию в качестве результата

print(type(hello_world_func))  # <class 'function'>
hello_world_func()  # Hello


def get_mul_func(m):
    nonlocal_m = m

    def local_mul(n):
        return n * nonlocal_m

    return local_mul


two_mul = get_mul_func(2)  # возвращаем функцию, которая будет умножать числа на 2
two_mul(5)  # 5 * 2


def func(a, b, c):
    print('a =', a)
    print('b =', b)
    print('c =', c)


func(1, 2, 3)
# a = 1
# b = 2
# c = 3

func(3, 2, 1)
# a = 3
# b = 2
# c = 1

# Правильно
# func(a, b, c=3)

# Неправильно
# func(a=1, b, c)

print(1)
print(1, 2)
print(1, 2, 3)
...

# 1
# 1 2
# 1 2 3
# ...

a = [1, 2, 3]
b = [a, 4, 5, 6]
print(b)
# [[1, 2, 3], 4, 5, 6]

a = [1, 2, 3]
b = [*a, 4, 5, 6]
print(b)


# [1, 2, 3, 4, 5, 6]


def incorrect_func(name_arg=[]):
    # name_arg является локальной переменной
    print("Аргумент до изменения", name_arg)
    name_arg.append(1)
    print("Аргумент после изменения", name_arg)


# вызовем два раза одну и ту же функцию
incorrect_func()
print('-----')
incorrect_func()


# Аргумент до изменения []
# Аргумент после изменения [1]
# -----
# Аргумент до изменения [1]
# Аргумент после изменения [1, 1]


# установим аргумент name_arg пустым, а внутри функции будем проверять его
def correct_func(name_arg=None):
    if name_arg is None:
        name_arg = []
    print("Аргумент до изменения", name_arg)
    name_arg.append(1)
    print("Аргумент после изменения", name_arg)


# вызовем два раза одну и ту же функцию
correct_func()
print('-----')
correct_func()
print('-----')
correct_func([123])
print('-----')
correct_func(name_arg=[123])


# Аргумент до изменения []
# Аргумент после изменения [1]
# -----
# Аргумент до изменения []
# Аргумент после изменения [1]
# -----
# Аргумент до изменения [123]
# Аргумент после изменения [123, 1]
# -----
# Аргумент до изменения [123]
# Аргумент после изменения [123, 1]

# Рекурсивная функция числа фиббоначи
def rec_fibb(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return rec_fibb(n - 1) + rec_fibb(n - 2)


rec_fibb(10)  # 55


# Сумма чисел от 1 до n
def rec_fibb(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return rec_fibb(n - 1) + rec_fibb(n - 2)


rec_fibb(10)  # 55


# Разворот строки
def reverse_str(string):
    if len(string) == 0:
        return ''
    else:
        return string[-1] + reverse_str(string[:-1])


reverse_str('test')  # tset

# Дано натуральное число N. Вычислите сумму его цифр.
def sum_digit(n):
   if n < 10:
       return n
   else:
       return n % 10 + sum_digit(n // 10)

sum_digit(123)  # 6