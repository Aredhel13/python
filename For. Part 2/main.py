n = int(input('Введите число: '))

sum_number = 0

for i in range(n + 1):
  sum_number += ((-1) ** i) * (1 / 2 ** i)

print('Сумма ряда равна:', sum_number)