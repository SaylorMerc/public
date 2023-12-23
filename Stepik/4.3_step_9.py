# Красный, синий и желтый называются основными цветами, потому что их нельзя получить путем смешения других цветов.
# При смешивании двух основных цветов получается вторичный цвет:
#
# если смешать красный и синий, то получится фиолетовый;
# если смешать красный и желтый, то получится оранжевый;
# если смешать синий и желтый, то получится зеленый.
# Напишите программу, которая считывает названия двух основных цветов для смешивания.
# Если пользователь вводит что-нибудь помимо названий «красный», «синий» или «желтый», то программа должна вывести
# сообщение об ошибке.
# В противном случае программа должна вывести название вторичного цвета, который получится в результате.

color1 = input()
color2 = input()
red, blue, yellow, orange, purple, green = 'красный', 'синий', 'желтый', 'оранжевый', 'фиолетовый ', 'зеленый'

if (color1 == red and color2 == blue) or (color1 == blue and color2 == red):
    print(purple)
elif (color1 == blue and color2 == yellow) or (color1 == yellow and color2 == blue):
    print(green)
elif (color1 == yellow and color2 == red) or (color1 == red and color2 == yellow):
    print(orange)
elif color1 == red and color2 == red:
    print(red)
elif color1 == blue and color2 == blue:
    print(blue)
elif color1 == yellow and color2 == yellow:
    print(yellow)
else:
    print('ошибка цвета')
