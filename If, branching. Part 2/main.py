hour = int(input('Введите время в часах (от 0 до 23): '))
if (hour >= 8 and hour < 10) or (hour >= 12 and hour < 14) or (hour >= 15 and hour < 18) or (hour >= 20 and hour < 22):
  print('Можно получить посылку')
else:
  print('Посылку получить нельзя')
  
if not (hour >= 8 and hour < 10) and not (hour >= 12 and hour < 14) and not (hour >= 15 and hour < 18) and not (hour >= 20 and hour < 22):
  print('Посылку получить нельзя')
else:
  print('Можно получить посылку')
