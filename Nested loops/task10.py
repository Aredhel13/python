print('Задача 10. Яма ')

n = int(input('Введите глубину ямы: '))

for row in range(n):
  left, right =  '', ''
  flag = False
  for col in range(n, n - 1 - row, -1):
    left += str(col)
    right = str(col) + right
    if n - row > 9:
      flag = True
  left += '.' * (n - 1 - row)
  right = '.' * (n - 1 - row) + right
  if flag:
    left += '.' * (n - 10 - row)
    right = '.' * (n - 10 - row) + right
  print(left + right)


# В одной компьютерной текстовой игре рисуются всяческие элементы ландшафта.
#
# Напишите программу,
# которая получает на вход число N и выводит на экран числа в виде “ямы”:

# Введите число: 5
# 
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345
