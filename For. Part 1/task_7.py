print('Задача 7. Отрезок')

a = int(input('Введите начало интервала: '))
b = int(input('Введите конец интервала: '))
average = count = 0
for i in range(a, b + 1):
  if i % 3 == 0:
    average += i
    count += 1
print('Среднее арифметическое =', average / count)

# Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль 
#среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.