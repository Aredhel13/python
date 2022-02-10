import math 

print('Задача 7. Ход конём')
print('Введите местоположение коня: ')

cell_x, cell_y, point_x, point_y = 1, 1, 1, 1

while cell_x < 0 or cell_x > 0.8:
  cell_x = float(input('По x = '))

while cell_y < 0 or cell_y > 0.8:
  cell_y = float(input('По y = '))


print('Введите местоположение точки на доске: ')

while point_x < 0 or point_x > 0.8:
  point_x = float(input('По x = '))

while point_y < 0 or point_y > 0.8:
  point_y = float(input('По y = '))

cell_x = math.floor(10 * cell_x)
cell_y = math.floor(10 * cell_y)
point_x = math.floor(10 * point_x)
point_y = math.floor(10 * point_y)

print(f'Конь в клетке ({cell_x}, {cell_y}). Точка в клетке ({point_x}, {point_y}).')

if math.fabs(cell_x - point_x) + math.fabs(cell_y - point_y) == 3:
  print('Да, конь может ходить в эту точку.')
else:
  print('Нет, конь не может ходить в эту точку.')



# В рамках разработки шахматного ИИ стоит новая задача.
# По заданным вещественным координатам коня
# и второй точки программа должна определить может ли конь ходить в эту точку.
# 
# Используйте как можно меньше конструкций if и логических операторов.
# Обеспечьте контроль ввода.

# Введите местоположение коня:
# 0.071
# 0.118
# Введите местоположение точки на доске:
# 0.213
# 0.068
# Конь в клетке (0, 1). Точка в клетке (2, 0).
# Да, конь может ходить в эту точку.