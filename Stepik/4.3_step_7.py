#Известен вес боксера-любителя (целое число). Известно, что вес таков,
# что боксер может быть отнесён к одной из трех весовых категорий:
# Легкий вес – до 60 кг;
# Первый полусредний вес – до 64 кг;
# Полусредний вес – до 69 кг.
# Напишите программу, определяющую, в какой категории будет выступать данный боксер.

a = int(input())
if a < 60:
    print('Легкий вес')
elif 64 > a >= 60:
    print('Первый полусредний вес')
else:
    print('Полусредний вес')
