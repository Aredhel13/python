print('Задача 6. Письмо')

letter_params = int(input('Введите длину стороны письма: '))
quantity = 0
while letter_params > 12:
  quantity += 1
  letter_params /= 2
print('Количество сложений равно =', quantity * 2)


# У нас есть
# квадратный конверт размера 12х12 сантиметров и письмо на квадратном листе бумаги,
# которое не помещается в конверт.
# 
# Напишите программу,
# которая подскажет сколько раз нужно сложить письмо пополам,
# чтобы оно поместилось в конверт.
# Размеры письма вводятся с клавиатуры.