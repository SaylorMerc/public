per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('введите сумму, которую хотите положить на вклад:  '))
TKB = int((per_cent['ТКБ'])*(money/100))
SKB = int((per_cent['СКБ'])*(money/100))
VTB = int((per_cent['ВТБ'])*(money/100))
SBER = int((per_cent['СБЕР'])*(money/100))
deposit = [TKB, SKB, VTB, SBER]
print('Накопленные средства за год вклада в каждом банке = ', deposit)
print('Максимальная сумма, которую вы cможете заработать —', max(deposit))