print('Задача 3. Посчитай чужую зарплату...')

average_sal = 0
for i in range(1, 13):
  print('Введите зарплату за', i, 'месяц')
  salary = int(input())
  average_sal += salary
print('Средняя зарплата составляет ', average_sal / 12)

# Бухгалтер устала постоянно считать вручную среднегодовую зарплату сотрудников компании
# и, чтобы облегчить себе жизнь, обратилась к программисту.
 
# Напишите программу,
# которая принимает от пользователя зарплату сотрудника за каждый из 12 месяцев 
# и выводит на экран среднюю зарплату за год.
