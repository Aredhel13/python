print('Задача 3. Кривой мессенджер')

text = input('Введите текст: ')
position = 1

for symbol in text:
  if symbol == '*':
    break
  position += 1

print("Символ '*' стоит на позиции", position)
