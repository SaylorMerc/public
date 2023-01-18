num = int(input())
digit4 = num % 10
digit3 = (num % 100) // 10
digit2 = (num // 100) % 10
digit1 = num // 1000
if digit1 + digit4 == digit2 - digit3:
    print('ДА')
else:
    print('НЕТ')
