number = int(input('Введите четырёхзначное число: '))
print('Введенное число: ', number)
print('Полученное число: ', number % 10 * 1000 + number // 10 % 10 * 100 + number // 100 % 10 * 10 + number // 1000)