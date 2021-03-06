print('Задача 10. Метод бутерброда')

secret_word = input('Введите зашифрованное сообщение: ')
result_world = ''

for i in range(0, len(secret_word), 2):
  print(i, secret_word[i])
  result_world += secret_word[i]

if len(secret_word) % 2 == 0:
  for j in range(len(secret_word) - 1, 0, -2):
    print(j, secret_word[j])
    result_world += secret_word[j]
else:
  for j in range(len(secret_word) - 2, 0, -2):
    print(j, secret_word[j])
    result_world += secret_word[j]

print('Расшифровано слово: ', result_world)


# Секретное агентство «Super-Secret-no» решило
# для шифрования переписки своих сотрудников использовать «метод бутерброда».
# Сначала буквы слова нумеруются в таком порядке:
# первая буква получает номер 1,
# последняя буква - номер 2,
# вторая – номер 3,
# предпоследняя – номер 4, потом третья … и так для всех букв (см. рисунок).
# Затем все буквы записываются в шифр в порядке своих номеров.
# 
# Например, слово «sandwich» зашифруется в «shacnidw».
# 
# К сожалению, программист «Super-Secret-no», написал только программу шифрования и уволился.
# И теперь агенты не могут понять, что же они написали друг другу. Помогите им.
# 
# Пример:
# Введите зашифрованное сообщение: shacnidw
# Расшифрованное сообщение: sandwich
#          1   3   5   7   8   6   4   2
# Слово: | s | a | n | d | w | i | c | h |
#
# Шифр:  | s | h | a | c | n | i | d | w |