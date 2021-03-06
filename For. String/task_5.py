print('Задача 5. Марсоход 2')

x, y = 8, 10
step = ''

print('Для выхода из программы нажмите на клавишу Q')
print(f'Марсоход находится на позиции [{x}, {y}], введите команду:')


while True:
  step = input().lower()
  if step == 'q':
    break
  if step == 'w' and y < 20:
    y += 1
  elif step == 's' and y > 0:
    y -= 1
  elif step == 'd' and x < 20:
    x += 1
  elif step == 'a' and x > 0:
    x -= 1
  else:
    print('Мы не Вас не поняли, попробуйте еще раз!')
  if (step in ['a', 'd'] and x in [0, 20]) or (step in ['w', 's'] and y in [0, 20]):
    print('Перед вами стена! Для дальнейшего движения, Вам нужно выбрать другое направление.')
  print(f'Марсоход находится на позиции [{x}, {y}], введите команду:')
 
print('Игра завершена')

# К роботу Валли отправили ещё одного робота Билли.
# Это его первый поход на Марс,
# поэтому он тестируется в прямоугольном помещении размером 15 на 20 метров.
# Марсоход высаживается в центре комнаты (в точке 8, 10),
# после чего управление им передаётся оператору - пользователю вашей программы.
# 
# Программа спрашивает
# в какую сторону оператор хочет направить робота:
# север (клавиша W),
# юг (клавиша S),
# запад (клавиша A)
# или восток (клавиша D).
# 
# Оператор делает выбор,
# марсоход перемещается на 1 метр в эту сторону и программа сообщает новую позицию марсохода.
# Если марсоход упёрся в стену,
# то он не должен пытаться перемещаться в сторону стены, в этом случае его позиция не меняется.
# 
# Пример:
# 
# [Программа]: Марсоход находится на позиции 6, 19, введите команду:
# [Оператор]: A
# [Программа]: Марсоход находится на позиции 5, 19, введите команду:
# [Оператор]: W
# [Программа]: Марсоход находится на позиции 5, 20, введите команду:
# [Оператор]: W
# [Программа]: Марсоход находится на позиции 5, 20, введите команду:
