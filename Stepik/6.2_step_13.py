# Напишите программу, которая считывает одну строку, после чего выводит «YES»,
# если в введённой строке есть подстрока «суббота» или «воскресенье», и «NO» в противном случае.

strr = input()
if 'суббота' in strr or 'воскресенье' in strr:
    print('YES')
else:
    print('NO')