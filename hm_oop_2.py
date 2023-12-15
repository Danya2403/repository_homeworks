def remove_item(self, id: int, amount_to_remove: int, removeAll=False):
    if id in super().get_list_of_products().keys():
        difference = super().get_list_of_products()[id][1] - amount_to_remove
        if difference == 0 or removeAll is True:
            super().get_list_of_products().pop(id)
        elif not difference < 0:
            super().get_list_of_products()[id] = (
                super().get_list_of_products()[id][0], super().get_list_of_products()[id][1] - amount_to_remove)
        else:
            raise ValueError("Нельзя удалить больше количества товара из списка, чем есть")
    else:
        raise ValueError("Товара с таким id нет")


class Category(ProductList):

    def init(self, name: str):
        super().init()
        self.name = name

    def get_name(self):
        return self.__name

    def __str(self):
        return f"{self.name}, {super().__str()}"


class Basket(ProductListWithAmount):

    def init(self):
        super().init()

    def make_purchase(self, ids_list):
        for id in ids_list:
            if super().get_list_of_products() is not None and \
                    id in super().get_list_of_products().keys():
                print(super().get_list_of_products()[id][0].get_name(), super().get_list_of_products()[id][1])
                amount_to_remove = super().get_list_of_products()[id][1]
                name_of_product = super().get_item(id)[0].get_name()
                try:
                    super().get_list_of_products()[id][0].remove_stock(amount_to_remove)
                    super().remove_item(id, amount_to_remove)
                    print(f"Вы успешно купили товар {name_of_product}, {amount_to_remove} штук")
                except ValueError as error:
                    print(f"Вы попытались купить слишком много товара: {error}")

            else:
                print("Такого товара нет в корзине")


class User:
    def init(self, login: str, password: str, basket: Basket):
        self.__login = login
        self.__password = password
        self.__basket = basket

    def get_basket(self):
        return self.__basket

    def get_login(self):
        return self.__login


def print_user_basket(user: User):
    basket = user.get_basket()
    print(f"Корзина {user.get_login()}", end="\t")
    for key, value in basket.get_list_of_products().items():
        print(f"id {key}, Продукт: {value[0]}, Кол-во в корзине: {value[1]}", end=" \\\ ")
    print()


print("Создадим несколько Категорий: ")

groceries = Category("Groceries")
chemistry = Category("Chemistry")
pizza = Product("Пицца", 1, 1000, 100, 2)
lazanya = Product("Лазанья", 3, 1000, 4, 4)
sredstvo = Product("Чистящее средство", 2, 500, 100, 3)

groceries.add_item(pizza)
groceries.add_item(lazanya)
chemistry.add_item(sredstvo)

print(groceries, chemistry, sep="\n")
user1 = User('Петя', '1234', Basket())
user2 = User('Вася', 'BestPassword1234', Basket())
print()
print("Создали двух пользователей Петю и Васю, но пока их корзину пусты")
print_user_basket(user1)
print_user_basket(user2)
print()
print("Петя и Вася добавляют продукты в корзину")
user1.get_basket().add_item(groceries.get_item(1), 1)
user2.get_basket().add_item(chemistry.get_item(2), 1)

print("Теперь их корзины выглядят так")

print_user_basket(user1)
print_user_basket(user2)

print("Петя и Вася совершают покупки")
user1.get_basket().make_purchase([1])
user2.get_basket().make_purchase([2])

print("Покупки совершенны")
print_user_basket(user1)
print_user_basket(user2)
print(f"На складе осталось кол-во: {pizza}, {sredstvo}")
print("\nПетя решает купить еще Лазанью и Чистящее средство: ")
user1.get_basket().add_item(groceries.get_item(3), 1)
user1.get_basket().add_item(chemistry.get_item(2), 3)

print_user_basket(user1)

user1.get_basket().make_purchase([2, 3])

print("Покупка совершенна")
print_user_basket(user1)
print(f"На складе осталось кол-во: {lazanya}, {sredstvo}")