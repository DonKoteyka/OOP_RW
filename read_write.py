with open('recipes.txt', 'rt') as file:
    meal = {}
    for line in file:
        meal_name = line.strip()
        item_count = int(file.readline().strip())
        dish = []
        for _ in range(item_count):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            dish.append({
                'ingredient_name' : ingredient_name,
                'quantity' : quantity,
                'measure' : measure
            })
        file.readline()
        meal.setdefault(meal_name, dish)
def get_shop_list_by_dishes(dishes, person_count):
    res = dict()
    for i in dishes:
        for items in meal.get(i):
            if items['ingredient_name'] not in res:
                res[items['ingredient_name']] = {
                    'measure':items['measure'],
                    'quantity': (int(items['quantity'])*person_count)
            }
            else:
                res[items['ingredient_name']]['quantity'] +=(int(items['quantity'])*person_count)
    return res
print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))






