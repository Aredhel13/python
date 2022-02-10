
deck = int(input('Сколько всего карточек? '))
sum_deck = sum_card = 0
for i in range(1, deck):
  card = int(input('Введите номер имеющейся карты: '))
  sum_card += card
  sum_deck += i
print('Номер потерянной карточки:', sum_deck + deck - sum_card)