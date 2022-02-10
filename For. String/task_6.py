print('Задача 6. Спецшифр')

string = input('Введите строку: ')
max_len, lenght = 0, 0

for letter in string:
  if letter == 's':
    lenght += 1
  else:
    if lenght > max_len:
      max_len = lenght
    lenght = 0

#Если строка содержит только 's'
if max_len == 0:
  max_len = lenght
 
print('Самая длинная последовательность:', max_len)


# Два сотрудника спецслужб переписываются необычным шифром.
# Каждую букву они шифруют в виде строки,
# внутри которой есть длинная последовательность букв “s”, 
# а длина самой длинной - это и есть номер буквы алфавита, которую хотят отправить.
# 
# Напишите программу,
# которая получает на вход строку,
# подсчитывает в ней самую длинную последовательность подряд идущих букв “s” и выводит ответ на экран.
# 
# Пример:
# Введите строку: ssbbbsssbc
# Самая длинная последовательность: 3