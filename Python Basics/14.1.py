# объявили функцию для подсчета количества символов в тексте
def char_frequency():
    text = """
   У лукоморья дуб зелёный;
   Златая цепь на дубе том:
   И днём и ночью кот учёный
   Всё ходит по цепи кругом;
   Идёт направо -- песнь заводит,
   Налево -- сказку говорит.
   Там чудеса: там леший бродит,
   Русалка на ветвях сидит;
   Там на неведомых дорожках
   Следы невиданных зверей;
   Избушка там на курьих ножках
   Стоит без окон, без дверей;
   Там лес и дол видений полны;
   Там о заре прихлынут волны
   На брег песчаный и пустой,
   И тридцать витязей прекрасных
   Чредой из вод выходят ясных,
   И с ними дядька их морской;
   Там королевич мимоходом
   Пленяет грозного царя;
   Там в облаках перед народом
   Через леса, через моря
   Колдун несёт богатыря;
   В темнице там царевна тужит,
   А бурый волк ей верно служит;
   Там ступа с Бабою Ягой
   Идёт, бредёт сама собой,
   Там царь Кащей над златом чахнет;
   Там русский дух... там Русью пахнет!
   И там я был, и мёд я пил;
   У моря видел дуб зелёный;
   Под ним сидел, и кот учёный
   Свои мне сказки говорил.
   """

    text = text.lower()
    text = text.replace(" ", "")
    text = text.replace("\n", "")

    count = {}  # для подсчета символов и их количества
    for char in text:
        if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
            count[char] += 1
        else:
            count[char] = 1

    for char, cnt in count.items():
        print(f"Символ {char} встречается {cnt} раз")


...

# вызвали функцию в любом месте программы
char_frequency()


def print_2_add_2():
    result = 2 + 2
    print(result)


print_2_add_2()


def hello_world():
    print("Hello World")


hello_world()


def char_frequency(text):
    text = text.lower()
    text = text.replace(" ", "")
    text = text.replace("\n", "")

    count = {}  # для подсчета символов и их количества
    for char in text:
        if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
            count[char] += 1
        else:
            count[char] = 1

    for char, cnt in count.items():
        print(f"Символ {char} встречается {cnt} раз")


char_frequency("Меня зовут Иван")


# функция, которая возводит любое число в степень n
def pow_func(base, n=2):
    print(base ** n)


pow_func(3)  # 9
pow_func(5, 3)  # 125


def check_num(a, n):
    if a % n == 0:
        print(f"Число {n} является делителем числа {a}")
    else:
        print(f"Число {n} не является делителем числа {a}")


check_num(4, 2)  # Число 2 является делителем числа 4
check_num(5, 2)  # Число 2 не является делителем числа 5


def reverse_stair(n):
    for i in range(n, 0, -1):
        print("*" * i)


reverse_stair(5)


def pow_func(base, n=2):
    print(base ** n)


print(pow_func(3))


# 9
# None

def pow_func(base, n=2):
    inside_result = base ** n
    return inside_result


print(pow_func(3))
# 9

outside_result = pow_func(3)
print(outside_result)


# 9

def get_multipliers(a):
    count = 0
    for n in range(1, a + 1):
        if a % n == 0:
            count += 1

    return count


get_multipliers(5)  # 2
get_multipliers(4)  # 3


def check_palindrome(str_):
    str_ = str_.lower()
    str_ = str_.replace(" ", "")

    if str_ == str_[::-1]:
        return True
    else:
        return False


check_palindrome("test")  # False
check_palindrome("Кит на море не романтик")  # True
