print('Задача 8. Сумма ряда')


n = int(input('Введите число: '))

sum_number = 0

for i in range(n + 1):
  sum_number += ((-1) ** i) * (1 / 2 ** i)

print('Сумма ряда равна:', sum_number)



# Дано натуральное число N.
# Напишите программу для вычисления следующей суммы ряда (начиная с единицы)

# S = 1 - 1/2 + 1/4 - 1/8 + … (-1)**N * 1/2**N 
