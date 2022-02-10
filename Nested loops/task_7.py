print('Задача 7. Наибольшая сумма цифр')

number = int(input('Введите элемент последовательности: '))
maxx, summ = 0, 0

while number != 0:
  while number > 0:
    summ += number % 10
    number = number // 10
    print(number)
  if summ > maxx:
    maxx = summ
  summ = 0
  number = int(input('Введите элемент последовательности: '))

print('Максимальная сумма чисел: ', maxx)

# Вводится N чисел. 
# Среди натуральных чисел, которые были введены, 
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.
