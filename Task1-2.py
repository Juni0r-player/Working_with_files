#Задание №1
with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for i in file:
        recipe_name = i.strip()
        ingredients_count = file.readline()
        list_ingredients = []
        for j in range(int(ingredients_count)):
            recipe = file.readline().strip().split(' | ')
            product, quantity, word = recipe
            list_ingredients.append({'ingredient_name': product, 'quantity': quantity, 'measure': word})
        file.readline()
        cook_book[recipe_name] = list_ingredients
            
#Задание №2
def get_shop_list_by_dishes(dishes: list, person_count:int):
    shop_product = {}
    for dish in dishes:
        if dish in cook_book: # Если ингридиент уже есть в словаре
            for product in cook_book[dish]: # {'ingredient_name': 'Картофель', 'quantity': '1', 'measure': 'кг'}
                if product['ingredient_name'] in shop_product:
                    shop_product[product['ingredient_name']]['quantity'] += int(product['quantity']) * person_count
                else:
                    shop_product[product['ingredient_name']] = {'measure': product['measure'], 'quantity': int(product['quantity']) * person_count}
        else:
            print('Блюда нет в кулинарной книге')
    print(shop_product)                    
                        

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)                   
    
    
    

# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }    