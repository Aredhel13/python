import math

print('Задача 2. Грубая математика')
print('Признак завершения ввода - это число 0')

n = float(input('Введите число: '))

while n != 0:
  if n > 0:
    print(f'Число положительное, ln({math.ceil(n)}) = ', math.log(math.ceil(n)))
  else:
    print(f'Число отрицательное, exp({math.floor(n)}) = ', math.exp(math.floor(n)))
  print()
  n = float(input('Введите число: '))

print('Программа завершена')

# В одном аналитическом центре,
# где занимаются разного рода математическим анализом,
# работал практикант,
# который написал программу для расчёта некоторых функций.
# Правда, он в тот день очень устал
# и немного не так прочитал техническое задание 
# и функции теперь рассчитываются довольно грубо.
# 
# Вводится последовательность из N вещественных чисел.
# При этом положительные числа округляются вверх, отрицательные округляются вниз.
# 
# Напишите программу,
# которая выводит натуральный логарифм от числа,
# если оно положительное, и экспоненту в степени числа, если оно отрицательное.
# 
# Пример:
# 
# Введите кол-во чисел: 3
# Введите число: 1.3
# x = 2   log(x) = 0.6931471805599453
# 
# Введите число: -2.1
# x = -3   exp(x) = 0.049787068367863944
# 
# Введите число: -5.9
# x = -6   exp(x) = 0.0024787521766663585