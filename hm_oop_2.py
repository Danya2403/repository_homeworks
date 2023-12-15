#1 задание
#class Product():
#   def __init__(self,name,id,price,rating,quantity_of_products):
#        self.name=name
#        self.id=id
#        self.price=price
#        self.rating=rating
#        self.quantity_of_products=quantity_of_products
#
#    def add_stock(self,quantity_of_products):
#        self.quantity_of_products+=quantity_of_products
#
#    def remote_stock(self, quantity_of_products):
#        if self.quantity_of_products>=quantity_of_products:
#            self.quantity_of_products-=quantity_of_products
#        else:
#            print('Товар закончился')
#    def update_quantity_of_products(self, new_quantity_of_products):
#        self.quantity_of_products=new_quantity_of_products

#    def update_price(self,new_price):
#        self.price=new_price

#    def display_product(self):
#        print("Название товара:", self.name)
#        print("ID:", self.id)
#        print("Цена:", self.price)
#        print("Рейтинг:", self.rating)
#        print("Колличесвто товара на складе:", self.quantity_of_products)

#примеры работы программы
#product_1=Product("Кроссовки",1234567,10999,4.5,50)
#product_1.update_price(200000)
#product_1.display_product()

#product_1=Product("Кроссовки",1234567,10999,4.5,50)
#product_1.update_quantity_of_products(150)
#product_1.display_product()

#product_1=Product("Кроссовки",1234567,10999,4.5,50)
#product_1.remote_stock(20)
#product_1.display_product()

#product_1=Product("Кроссовки",1234567,10999,4.5,50)
#product_1.add_stock(20)
#product_1.display_product()

#2 задание

class Product:
    def __init__(self, name, id, price, rating, stock):
        self.name = name
        self.id = id
        self.price = price
        self.rating = rating
        self.stock = stock

class Category:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("Item not found in category.")

    def get_items(self):
        return self.items

category1=Category("Electronics")
category2=Category("Clothing")

product1 = Product("Laptop", 1234, 800, 4.5, 10)
product2 = Product("Phone", 5678, 500, 4.2, 20)
product3 = Product("Shirt", 9012, 25, 3.9, 30)
product4 = Product("Jeans", 3456, 50, 4.1, 15)

category1.add_item(product1)
category1.add_item(product2)
category2.add_item(product3)
category2.add_item(product4)





