def print_ladder(n):
    for i in range(1, n + 1):
        return "*" * i


print(print_ladder(6))

N = 5

for i in range(1, N + 1):
   print("*" * i)

def get_wind_class(speed):  # объявление функции
    if 1 <= speed <= 4:  # только аргумент
        return "weak [1]"
    elif 5 <= speed <= 10:
        return "moderate [2]"
    elif 11 <= speed <= 18:
        return "strong [3]"
    elif speed >= 19:
        return "hurricane [4]"


print(get_wind_class(6))  # мы просим программу напечатать то, что в скобках
