"""
На вход программе подается натуральное число nn, а затем nn различных натуральных чисел, каждое на отдельной строке.
Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.
"""

n = int(input())
largest = 0
prelargest = 0
for i in range(1, n + 1):
    num = int(input())
    if num > largest:
        prelargest, largest = largest, num
    elif num > prelargest:
        prelargest = num
print(largest, prelargest, sep='\n')



