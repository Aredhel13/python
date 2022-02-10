print('Задача 6. Защита от дурака')

number = int(input('Введите число: '))
if (number >= 10 and number < 100) or (number <= -10 and number > -100):
  print('Число', number, 'двузначное')
else:
  print('Число', number, 'не двузначное')

# Мы участвуем в разработке приложения для математиков, где можно будет делать всё,
# начиная от простейших вычислений и заканчивая построением сложных графиков.
# В этом приложении реализована установка диапазона чисел,
# и нам необходимо написать этакую «защиту от дурака».
# 
# 
# Напишите программу,
# которая получает на вход число и проверяет, двузначное оно или нет.
# Выведите соответствующее сообщение. Числа −42 и −99 тоже считаются двузначными.
# Сделайте это, используя не более одного оператора if-elsе. Не используйте elif.