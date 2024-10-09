from itertools import count

with open('recipes.txt', 'r', encoding='utf-8') as f:
  cook_book = {}
  for line in f:
    ingredients = []
    dish = line.strip()
    count = int(f.readline().strip())
    for n in range(count):
      ingredient_name, quantity, measure = f.readline().strip().split('|')
      ingredient = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
      ingredients.append(ingredient)
    cook_book.update({dish: ingredients})
    f.readline().strip()

def get_shop_list_by_dishes(dishes, person_count):
  list_bludo = {}
  for bludo in cook_book.keys():
    for n in dishes:
      if n == bludo:
        for a in cook_book.get(n):
          b = a.copy()
          b.pop('ingredient_name')
          if a['ingredient_name'] not in list_bludo:
            b['quantity'] = int(b['quantity'])*person_count
          else:
            b['quantity'] = int(b['quantity'])*person_count+list_bludo[a.get('ingredient_name')]['quantity']
          list_bludo.update({a.get('ingredient_name') : b})
          # print(list_bludo[a.get('ingredient_name')]['quantity'])
  return list_bludo

print(get_shop_list_by_dishes(['Омлет', 'Омлет', 'Запеченный картофель'], 3))