print('Задача 7. Обычный день на работе')

print('Начался 8-часовой рабочий день')
market_flag = False
hour = 0
sum_task = 0
while hour < 8:
  hour += 1
  print(hour, 'час')
  count_task = int(input('Сколько задач решит Максим? '))
  sum_task += count_task
  wife = int(input('Звонит жена. Взять трубку? (1-да, 0-нет) '))
  if wife == 1 and market_flag == False:
    market_flag = True
print('Рабочий день закончился. Всего выполнено задач: ', sum_task)
if market_flag:
  print('Нужно зайти в магазин')

# Максим программирует целый день на работе и вечером идёт домой.
# Каждый час начальство кидает ему несколько задач,
# которые нужно решить до следующего рабочего часа.
# И вдобавок каждый час Максиму звонит супруга.
# Он знает, что если он возьмёт трубку, то жена попросит зайти вечером в магазин.
 
# Напишите программу,
# в которой считается, сколько задач выполнил Максим за день (8 часов).
# Если он хоть раз взял трубку,
# то в конце дополнительно выводите сообщение: «Нужно зайти в магазин».
 
# Пример:
# Начался 8-часовой рабочий день
# 1 час
# Сколько задач решит Максим? 1
# Звонит жена. Взять трубку? (1-да, 0-нет) 0
 
# 2 час
# Сколько задач решит Максим? 2
# Звонит жена. Взять трубку? (1-да, 0-нет) 0
 
# 3 час
# Сколько задач решит Максим? 3
# Звонит жена. Взять трубку? (1-да, 0-нет) 0
 
# 4 час
# Сколько задач решит Максим? 4
# Звонит жена. Взять трубку? (1-да, 0-нет) 1
 
# 5 час
# Сколько задач решит Максим? 5
# Звонит жена. Взять трубку? (1-да, 0-нет) 0
 
# 6 час
# Сколько задач решит Максим? 1
# Звонит жена. Взять трубку? (1-да, 0-нет) 0
 
# 7 час
# Сколько задач решит Максим? 2
# Звонит жена. Взять трубку? (1-да, 0-нет) 1
 
# 8 час
# Сколько задач решит Максим? 3
# Звонит жена. Взять трубку? (1-да, 0-нет) 0
 
# Рабочий день закончился. Всего выполнено задач: 21
# Нужно зайти в магазин