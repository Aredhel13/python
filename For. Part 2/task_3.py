print('Задача 3. Это будет бомба')

time_to_explosion = int(input('Сколько у нас времени? '))
for second in range(time_to_explosion, 0, -1):
  answer = int(input('Обезвредить бомбу сейчас? '))
  print('До взрыва осталось', second, 'с')
  if answer == 1:
    print('Бомба обезврежена!')
    break
if answer != 1:
  print('Бомба взорвалась!')



# Мы разрабатываем пошаговую игру по мотивам боевика.
# Игрок - главный герой и должен обезвредить бомбу, которая взорвётся через N секунд.
# Программа спрашивает пользователя хочет ли он обезвредить бомбу сейчас.
# 
# Если ответ “0” (то есть “нет”), то счетчик бомбы уменьшается.
# Если он достиг нуля, то программа выдаёт сообщение “Бомба взорвалась”,
# а если не достиг, то программа вновь переспрашивает,
# не хочет ли игрок обезвредить бомбу, и сообщает, сколько времени осталось до взрыва.. 
# 
# Если ответ “да”, то программа выводит на экран сообщение о том,
# что бомба обезврежена и сколько секунд оставалось до взрыва.
# Используйте цикл for.
