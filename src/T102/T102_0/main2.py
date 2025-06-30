shop = {}

def create_message(products):
    messange = ''
    for product, price in products.items():
        messange += ' {0} {1}'.format(product, price)
    return messange

def write_to_file(shop=shop):

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

    elif user_group not in shop:
        shop.update({user_group:{}})
        shop[user_group].update(products)
        write_to_file()
        
    else: 'Error'

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