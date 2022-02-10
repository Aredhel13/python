print('Задача 6. Сумма факториалов')

number = int(input('Введите число: '))
factorial, summ = 1, 0

for i in range(1, number + 1):
  for j in range(1, i + 1):
    factorial *= j
  summ += factorial
  factorial = 1

print(f'Сумма факториалов от 1 до {number} =', summ)



# Напишите программу,
# которая запрашивает у пользователя число N
# и находит сумму факториалов 1! + 2! + 3! +... + N! 
