# Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя и выводит фразу:
#
# «Hello [введенное имя] [введенная фамилия]! You just delved into Python».

name = input()
forname = input()
str_1 = 'Hello '
space = ' '
vos = '! '
str_2 = 'You just delved into Python'
frasa = str_1 + name + space + forname + vos + str_2
print(frasa)