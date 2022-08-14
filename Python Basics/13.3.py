print(bool(0))  # False
print(bool(1))  # True

print(bool(""))   # False
print(bool("1"))  # True

print(bool([]))   # False
print(bool([1]))  # True
# Рассмотрим парочку примеров. Если ваша задача проверить, можно ли делить, и является ли делитель нулём, то проверку в явном виде zero != 0 делать излишне.
#Плохо
if zero != 0:
   print(10 / zero)
else:
   print("Делить на ноль нельзя")

# Хорошо
if zero:
   print(10 / zero)
else:
   print("Делить на ноль нельзя")
#Если вам нужно проверить, пустая строка или нет, то сравнивать её способом password == "", а уж тем более способом len(password) == 0 ни к чему.

# Плохо
if password == "":
   print("Вы забыли ввести пароль")
else:
   ...

# Очень плохо
if len(password) == 0:
   print("Вы забыли ввести пароль")
else:
   ...

# Хорошо
if not password:
   print("Вы забыли ввести пароль")
else:
   ...