shop = {
    'мучное':{
        'хлеб': 100
    }
}

def add_products(user_group, shop = shop, **products):
    if user_group in shop:
        shop[user_group].update(products)
    elif user_group not in shop:
        shop.update({user_group:{}})
        shop[user_group].update(products)
    else:
         return 'Error'
    return shop
    

def print_all_products(shop = shop):
    for group, array in shop.items():
        print('Раздел: ' + group)
        for product, price in array.items():
            print(product + ' - '+ str(price))

add_products('молочное', Сыр = 200, Молоко = 100)
print_all_products()
