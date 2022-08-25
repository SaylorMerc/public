L = ['THIS', 'IS', 'LOWER', 'STRING']

print(list(map(str.lower, L)))


# Из заданного списка вывести только положительные элементы
def positive(x):
    return x > 0  # функция возвращает только True или False


result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])

# Возвращается итератор, т.е. перечисляйте или приводите к списку
print(list(result))  # [1, 2]


# Отфильтруйте из заданного списка только четные элементы.
def even(y):
    return y % 2 == 0


result_one = filter(even, [-2, -1, 0, 1, -3, 2, -3])
print(list(result_one))

# map + filter
some_list = [i - 10 for i in range(20)]


def pow2(x): return x ** 2


def positive(x): return x > 0


print(some_list)
print(list(map(pow2, filter(positive, some_list))))


# То же самое через list comprehension:
# [i ** 2 for i in some_list if i > 0]

# map(func, list1)  # итератор, но никаких вычислений не будет произведено
# list(map(...))  # только здесь появляется объект

# [func(i) for i in list1]  # сразу готовый объект


# [func(i) for i in list1] == list(map(func, list1))  # результат один и тот же

# эти две функции выполняют одно и тоже — складывают два числа
def my_function(x1, x2):  # Обычная функция
    return x2 + x1


lambda x1, x2: x2 + x1  # Анонимная функция

# Возвести первые 10 натуральных чисел в квадрат
list(map(lambda x: x ** 2, range(1, 11)))  # правильно
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# list(map(lambda x: x ** 2; x + 1, range(1, 11)))  #  неправильно, так как lambda содержит две конструкции

d = {2: "c", 1: "d", 4: "a", 3: "b"}

# Чтобы отсортировать его по ключам, нужно сделать так:
print(dict(sorted(d.items())))
# {1: 'd', 2: 'c', 3: 'b', 4: 'a'}

sorted(d.items(), key=lambda x: x[1])  # сортировка по значению словаря

# (вес, рост)
data = [
    (82, 191),
    (68, 174),
    (90, 189),
    (73, 179),
    (76, 184)
]
print(list(sorted(data, key=lambda x: x[0] / x[1] ** 2)))

print(min(sorted(data, key=lambda x: x[0] / x[1] ** 2)))


