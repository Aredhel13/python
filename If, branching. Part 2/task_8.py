print('Задача 8. Новоселье')

square = int(input('Введите площадь квартиры (кв.м.): '))
cost = int(input('Введите стоимсоть квартиры (млн): '))
if (square >= 100 and cost <= 10) or (square >= 80 and cost <= 7):
  print('Ура! Квартира подходит!')
else:
  print('Квартира не подходит')

# Семья из трёх человек устала тесниться в однушке и наконец решила переехать.
# При обсуждении,
# какую же всё-таки купить квартиру исходя из своих предпочтений и семейного бюджета,
# они остановились на нескольких вариантах:

# Первый вариант 
# они готовы взять квартиру попросторнее (не менее 100 квадратных метров),
# но стоимостью не более 10 млн.
 
# Второй вариант — немного расширить круг поиска,
# то есть взять квартиру поменьше (от 80 квадратный метров),
# но и стоимостью не более 7 млн.
 
# Напишите программу,
# которая получает на вход стоимость квартиры и её площадь
# и выводит сообщение о том, подходит она или нет