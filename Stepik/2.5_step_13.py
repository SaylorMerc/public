# Напишите программу, в которой рассчитывается сумма и произведение цифр положительного трёхзначного числа.

num = int(input())
last_digit = num % 10
prelast_digit = (num % 100) // 10
first_digit = num // 100
total = last_digit + prelast_digit + first_digit
composition = last_digit * prelast_digit * first_digit
print('Сумма цифр =', total)
print('Произведение цифр =', composition)
