# Сделаем функцию, которая будет выполнять принимаемую функцию дважды:
def twice_func(inside_func):
    """Функция, выполняющая дважды функцию принятую в качестве аргумента"""
    inside_func()
    inside_func()


def hello():
    print("Hello")


twice_func(hello)


# Hello
# Hello

# Замыкание функций
# Сделаем функцию, которая будет возвращать функцию, всегда прибавляющую одно и тоже число x:
def make_adder(x):
    def adder(n):
        return x + n  # захват переменной "x" из nonlocal области

    return adder  # возвращение функции в качестве результата\


# функция, которая будет к любому числу прибавлять пятёрку
add_5 = make_adder(5)
print(add_5(10))  # 15
print(add_5(100))  # 105


# Декораторы
def my_decorator(a_function_to_decorate):
    # Здесь мы определяем новую функцию - «обертку». Она нам нужна, чтобы выполнять
    # каждый раз при вызове оригинальной функции, а не только один раз
    def wrapper():
        # здесь поместим код, который будет выполняться до вызова, потом вызов
        # оригинальной функции, потом код после вызова
        print("Я буду выполнен до основного вызова!")

        result = a_function_to_decorate()  # не забываем вернуть значение исходной функции

        print("Я буду выполнен после основного вызова!")
        return result

    return wrapper
def my_function():
   print("Я - оборачиваемая функция!")
   return 0

print(my_function())
# Я - оборачиваемая функция!
# 0

decorated_function = my_decorator(my_function)  # декорирование функции
print(decorated_function())
# Я буду выполнен до основного вызова!
# Я - оборачиваемая функция!
# Я буду выполнен после основного вызова!
# 0

# Давайте попробуем замерить время выполнения системной функции для возведения числа в степень 2 и соответствующего
# оператора.
import time


def decorator_time(fn):
   def wrapper():
       print(f"Запустилась функция {fn}")
       t0 = time.time()
       result = fn()
       dt = time.time() - t0
       print(f"Функция выполнилась. Время: {dt:.10f}")
       return dt  # задекорированная функция будет возвращать время работы
   return wrapper


def pow_2():
   return 10000000 ** 2


def in_build_pow():
   return pow(10000000, 2)


pow_2 = decorator_time(pow_2)
in_build_pow = decorator_time(in_build_pow)

pow_2()
# Запустилась функция <function pow_2 at 0x7f938401b158>
# Функция выполнилась. Время: 0.0000011921

in_build_pow()
# Запустилась функция <function in_build_pow at 0x7f938401b620>
# Функция выполнилась. Время: 0.0000021458

# Возьмите из предыдущего примера декорированные функции, которые возвращают время работы основной функции и найдите
# среднее время выполнения для 100 выполнений каждой функции.
import time

N = 100


def decorator_time(fn):
   def wrapper():
       t0 = time.time()
       result = fn()
       dt = time.time() - t0
       return dt
   return wrapper


def pow_2():
   return 10000000 ** 2


def in_build_pow():
   return pow(10000000, 2)


pow_2 = decorator_time(pow_2)
in_build_pow = decorator_time(in_build_pow)

mean_pow_2 = 0
mean_in_build_pow = 0
for _ in range(N):
   mean_pow_2 += pow_2()
   mean_in_build_pow += in_build_pow()

print(f"Функция {pow_2} выполнялась {N} раз. Среднее время: {mean_pow_2 / N:.10f}")
print(f"Функция {in_build_pow} выполнялась {N} раз. Среднее время: {mean_in_build_pow / 100:.10f}")