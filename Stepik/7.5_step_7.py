"""num = int(input())
counter = 0
total = 0
composition = 1
num_1 = num
while num != 0:  # пока в числе есть цифры
    last_digit = num % 10  # получить последнюю цифру
    counter += 1
    total += last_digit
    composition *= last_digit  # код обработки последней цифры
    num = num // 10  # удалить последнюю цифру из числа
first_digit = (num_1 % (10 ** counter)) // 10 ** (counter - 1)
last_digit = num_1 % 10
print(counter, total, composition, total / counter, first_digit, first_digit + last_digit, sep='\n')
"""
"""mx = 0
s = 0
for i in range(10):
    x = int(input())
    if x < 0:
        s += x
    if mx < x < 0:
        mx = x
if s != 0:
    print(s)
    print(mx)
else:
    print('NO')
"""
"""
n = int(input())
for i in range(n):
    for j in range():
        print('*', sep='')
    print()
"""
# 28n+30k+31m=365

n = int(input())
total = 0
for j in range(1, n + 1):
    composition = 1
    for i in range(1, j + 1):
        composition *= i
    total += composition
print(total)

