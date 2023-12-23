# Напишите программу, которая упорядочивает три числа от большего к меньшему.

a, b, c, = int(input()), int(input()), int(input())
minim = min(a, b, c)
maxim = max(a, b, c)
mid = (a + b + c) - (minim + maxim)
print(maxim, mid, minim, sep='\n')

