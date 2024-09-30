with open('recipes.txt', 'r', encoding='utf-8') as f:
  cook_book = {}
  ingredients = []
  ingredient = {}
  for line in f:
    stroka = line.strip()
    if len(stroka) != 0 and len(stroka) > 2:
      if '|' not in stroka:
        bludo = stroka
      else:
        ingredient_name, quantity, measure = stroka.split('|')
        ingredient = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
        ingredients.append(ingredient)
    cook_book.update({bludo : ingredients})
print(cook_book)

# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#  }
# def get_shop_list_by_dishes(dishes, person_count):
#   list_bludo = {}
#   for bludo in cook_book.keys():
#     for n in dishes:
#       if n == bludo:
#         for a in cook_book.get(n):
#           b = a.copy()
#           b.pop('ingredient_name')
#           list_bludo.update({a.get('ingredient_name') : b})
#   return list_bludo
#
# print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))