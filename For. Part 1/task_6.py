print('Задача 6. Успеваемость в классе')

grade_3, grade_4, grade_5 = 0, 0, 0
pupils = int(input('Введите количество учеников: '))
for i in range(1, pupils + 1):
  grade = int(input('Какую оценку получил {0} ученик? '.format(i)))
  if grade == 3:
    grade_3 += 1
  elif grade == 4:
    grade_4 += 1
  else:
    grade_5 += 1
if (grade_3 > grade_4) & (grade_3 > grade_5):
  print('Троешники лидируют! Их ', grade_3)
elif (grade_4 > grade_3) & (grade_4 > grade_5):
  print('Хорошисты лидируют! Их ', grade_4)
elif (grade_5 > grade_3) & (grade_5 > grade_4):
  print('Отличники лидируют! Их ', grade_5)
elif (grade_4 == grade_3 == grade_5):
  print('Всех поровну:', grade_3)
elif (grade_4 == grade_3):
  print('Хорошистов и троечников поровну: ', grade_3)
elif (grade_4 == grade_5):
  print('Хорошистов и отличников поровну: ', grade_3)
elif (grade_5 == grade_3):
  print('Отличников и троечников поровну: ', grade_3)




# В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было. 
# 
# Напишите программу, 
# которая получает список оценок - N чисел - и выводит на экран сообщение о том, 
# кого сегодня больше: отличников, хорошистов или троечников.