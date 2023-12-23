# На вход программе подается число nn – количество собачьих лет.
# Напишите программу, которая вычисляет возраст собаки в человеческих годах.

dog_age = float(input())
if dog_age == 1:
    human_age = 10.5
elif dog_age == 2:
    human_age = 21
else:
    human_age = 21 + (dog_age - 2) * 4
print(human_age)
