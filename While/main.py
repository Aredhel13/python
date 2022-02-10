number = int(input('Введите число: '))
res = 0
if number % 2 == 0:
  res += 1
while number != 0:
  number = int(input('Введите число: '))
  if number == 0:
    break
  elif number % 2 == 0:
    res += 1
print('Количество четных чисел: ', res)
