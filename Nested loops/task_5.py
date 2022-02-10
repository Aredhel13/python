print('Задача 5. Простые числа')

print('Для окончания ввода введите 0')

number = int(input('Введите элемент последовательности: '))
count, flag = 0, True

while number != 0:
  for i in range(2, int(number ** 1/2) + 1):
    if number % i == 0:
      print(number % i)
      flag = False
  if flag:
    count += 1
  flag = True  
  number = int(input('Введите элемент последовательности: '))

print('Количество простых чисел: ', count)




#Напишите программу,
#которая считает количество простых чисел в заданной последовательности 
#и выводит ответ на экран.