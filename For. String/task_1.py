print('Задача 1. Календарь')

day_of_week = input('Введите день недели: ')
days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']

print('\nНомер дня недели: ', end = ' ')

for day in days:
  if day == day_of_week.lower():
    print(days.index(day) + 1)
 



"""
### New solution

days = ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье')

day_of_week = input('Введите день недели: ')

if day_of_week.lower() not in days:
  print('Ошибка! Вы ввели не день недели.')
else:
  print('\nНомер дня недели:', days.index(day_of_week.lower())+1)



day_of_week = input('Введите день недели: ')

print('\nНомер дня недели: ', end = ' ')
for day_of_week.lower in ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
  print(day_of_week)
if day_of_week == 'Понедельник' or 'понедельник':
  print(1)
elif day_of_week == 'Вторник' or 'вторник':
  print(2)
elif day_of_week == 'Среда' or 'среда':
  print(3)
elif day_of_week == 'Четверг' or 'четверг':
  print(4)
elif day_of_week == 'Пятница' or 'пятница':
  print(5)
elif day_of_week == 'Суббота' or 'суббота':
  print(6)
elif day_of_week == 'Воскресенье' or 'воскресенье':
  print(7)
"""