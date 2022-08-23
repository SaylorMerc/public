# Функции генераторы
# Бесконечная последовательность чисел Фибоначчи
def fib():
    a, b = 0, 1
    yield a  # F0
    yield b  # F1

    while True:
        a, b = b, a + b
        yield b


for num in fib():
    print(num)


# функция-генератор, возвращающую бесконечную последовательность натуральных чисел
def count(start=1, step=1):
    counter = start
    while True:
        yield counter
        counter += step


# Создайте генератор цикла, то есть в функцию на входе будет передаваться массив, например, [1, 2, 3],
# генератор будет вечно работать возвращая 1 2 3 1 2 3… и так далее.
def repeat_list(list_):
    list_values = list_.copy()
    while True:
        value = list_values.pop(0)
        list_values.append(value)
        yield value


for i in repeat_list([1, 2, 3]):
    print(i)
