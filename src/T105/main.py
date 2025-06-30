import os
from read import print_file
shop = {}

def update_shop(dir_name = 'shop', shop=shop):
    tree = os.walk(dir_name)
    for root, dirs, files in tree:
        for file in files:
            group = print_file('shop/' + file)
            group = group.split(' ')
            
            names = group[1::2]
            prices = group[2::2]
            
            products = {}
            products.update(zip(names,prices))
            
            shop.update({file:products})

            pass


def create_message(products):
    messange = ''
    for product, price in products.items():
        messange += ' {0} {1}'.format(product, price)
    return messange

def write_to_file(shop=shop):
    if shop == {}:
        return 'В магазине ничего нет'

    for group,products in shop.items():
        file_name = 'shop/' + group
        file_group = open(file_name, 'w', encoding='utf-8')
        file_group.write(create_message(products))
        file_group.close()
    else: 'Error'
    return file_name

def add_products(user_group, products, shop = shop):
    if user_group in shop:
        shop[user_group].update(products)
        write_to_file()
        update_shop()
    elif user_group not in shop:
        shop.update({user_group:{}})
        shop[user_group].update(products)
        write_to_file()
        
    else: 'Error'

update_shop()

loop = True

while loop:
    groop = input('Введите название раздела, который вы хотите добавить или изменить: \n')
    number = int(input('Сколько товаров хотите добавить: \n'))
    i = 1
    products = {}
    while i <= number:
        product = input('Ведите название товара: ')
        price = int(input('Введите цену товара {0}: '.format(product)))

        products.update({product:price})
        i += 1
        if i > number:
            add_products(groop, products)
            loop = False

print(shop)