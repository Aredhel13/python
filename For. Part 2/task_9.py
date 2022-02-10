print('Задача 9. Выражение')

x = int(input('Введите число: '))

numerator, denominator = 1, 1

for i in range(1, 7):
  numerator *= (x - (2 ** i - 1))
  denominator *= (x - 2 ** i)

print('Результат равен =', numerator / denominator)

#Дано число x.
#Напишите программу для вычисления следующего выражения 

# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64)) 