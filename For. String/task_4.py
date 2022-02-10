print('Задача 4. Театр')

rows = int(input('Введите кол-во рядов: '))
places = int(input('Введите кол-во сидений ряду: '))
distance = int(input('Введите кол-во метров между рядами: '))

result = '=' * places + ' ' + '*' * distance + ' ' + '=' * places

print('\nСцена\n')
for row in range(rows):
  print(result)
