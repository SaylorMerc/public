"""Дано натуральное число. Напишите программу, которая вычисляет:

количество цифр 3 в нем;
сколько раз в нем встречается последняя цифра;
количество четных цифр;
сумму его цифр, больших пяти;
произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести ее);
сколько раз в нем встречается цифры 0 и 5 (всего суммарно)."""

num = int(input())
counter_dig_3 = 0
counter_last_digit = 1
counter_even_digit = 0
total_digit_more_5 = 0
comp_more_7 = 1
counter_0_5_meet = 0
while num != 0:  # пока в числе есть цифры
    last_digit = num % 10  # получить последнюю цифру
    if last_digit == 3:  # если цифра равно 3, то увеличиваем счетчик
        counter_dig_3 += 1
    if counter_last_digit == last_digit:  # если цифра равна последней, то увеличиваем счетчик
        counter_last_digit += 1
    if last_digit % 2 == 0:  # если цифра чётная, то увеличиваем счётчик
        counter_even_digit += 1
    if last_digit > 5:  # если цифра больше 5, то прибавляем её к сумме
        total_digit_more_5 += last_digit
    if last_digit > 7:  # если цифра больше 7, то умножаем её на произведение
        comp_more_7 *= last_digit
    if last_digit in (0, 5):  # если цифра равна 0 или 5, то увеличиваем счётчик
        counter_0_5_meet += 1
    num = num // 10  # удалить последнюю цифру из числа
print(counter_dig_3, counter_last_digit, counter_even_digit, total_digit_more_5, comp_more_7, counter_0_5_meet, sep='\n')

