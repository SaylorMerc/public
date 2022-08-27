# Различные методы вывода содержимого файла
# my_file = open('filename.txt')
# print(my_file.read())
# print(my_file.readline())
# for line in my_file:
# print(line)
# print(my_file.readlines())

# my_file = open('namefile.txt', 'w')
# my_file.write('tttttttttt')
# print('zzzzzzz', file=my_file)

# Оператор with
# with open('filename.txt') as my_file:
# for line in my_file:
# print(line)

# пользователь вводит произвольное целое число, а программа читает некий русский текст из файла и зашифровывает его в
# другой файл со сдвигом, соответствующим этому числу.
alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphaUp = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
number = int(input('Введите число на которое необходимо выполнить сдвиг'))

summary = ''


def changeChar(char):
    if char in alpha:
        return alpha[(alpha.index(char) + number) % len(alpha)]
    elif char in alphaUp:
        return alpha[(alphaUp.index(char) + number) % len(alphaUp)]
    else:
        return char


with open('filename.txt', encoding="utf8") as myFile:
    for line in myFile:
        for char in line:
            summary += changeChar(char)

with open('namefile.txt', 'w', encoding="utf8") as myFile:
    myFile.write(summary)

