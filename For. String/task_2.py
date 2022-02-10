print('Задача 2. Я стал новым пиратом!')

good_word = 0

for i in range(10):
  word = input('Введите слово: ')
  if (word == 'Карамба') or (word == 'карамба'):
    good_word += 1

print(good_word, 'человек попадут на борт!')
