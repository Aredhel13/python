print('Задача 3. Рамка')

width = int(input('Введите ширину: '))
height = int(input('Введите высоту: '))

print(' -' * width)
for i in range(height):
  print('|' + ' ' * (2 * width - 1) + '|')
print(' -' * width) 
  

# Напишите программу,
# которая рисует с помощью символьной графики прямоугольную рамку.
# Для вертикальных линий используйте символ вертикального штриха “|”,
# а для горизонтальных - дефис “-”. Пусть пользователь вводит ширину и высоту рамки.

#  _ _ _ _ _ _ _ _ _
# |                 |
# |                 |
# |                 |
# |                 |
# |                 |
# |                 |
# |_ _ _ _ _ _ _ _ _|
