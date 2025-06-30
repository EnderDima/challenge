shop = {}

def print_products(shop = shop):
    for product, price in shop.items():
        print(product + ' - ' + str(price))

def add_products(shop = shop, **products):
    shop.update(products)
    return shop

def update_prices(new_price, shop =shop):
    for product, price in shop.items():
        shop.update({product: price + new_price})
    return shop

add_products(сыр=100, хлеб=50, молоко=30)

update_prices(20)

print_products()