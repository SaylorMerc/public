L = ['a', 'b', 'c']
print(id(L))
# равные идентичности
L.append('d')
print(id(L))
print()

a = 5
b = 3 + 2
print(id(a))
print(id(b))
print("разность =", id(a) - id(b))
print()

list_1 = ['a', 'b', 'c']
list_2 = list_1
list_3 = list(list_1)
print(list_1)
print(list_2)
print(list_3)
print()
print(list_1 == list_2)
print(list_1 == list_3)
print()
print(list_1 is list_2)
print(list_1 is list_3)
print()
print()
# Особенности при работе со списками
L = ['Hello', 'world']
M = L

print(M is L)

M.append('!')

print(L)
# ['Hello', 'world', '!']

M = L.copy()

print(M is L)
print()

# shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])

# shopping_center[-1].append("Uniqlo")

# print(shopping_center)

shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
print(shopping_center)
list_id_before = id(shopping_center[-1])

shopping_center[-1].append("Uniqlo")
print(shopping_center)
list_id_after = id(shopping_center[-1])
print(list_id_before is list_id_after)
print()
