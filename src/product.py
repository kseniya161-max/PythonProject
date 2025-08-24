class Product:
    """Создаем класс Product"""

    def __init__(self, name: str, description: str, quantity: int, price: float):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.__price = price

    @property
    def price(self):
        """Геттер для получения цены"""
        return self.__price

    def __str__(self):
        """Переопределяем строку методомом __str__"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


    @price.setter
    def price(self, new_price: float):
        """Сеттер для получения цены если она не меньше или равна нулю"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, product_dict: dict):
        """Класс метод который создает новый продукт на основе словаря"""
        return cls(name=product_dict["name"],
                   description=product_dict["description"],
                   price=product_dict["price"],
                   quantity=product_dict["quantity"],
                   )


class Category:
    """Создаем класс Category"""
    # атрибут класса считает количество категорий
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products  # Тут хранятся product1, product1, product1
        Category.category_count += 1   # Добавляем +1 Категорию. отслеживает количество категорий
        Category.product_count += len(products)

    def add_product(self, product: Product):
            """Метод для добавления продукта в категорию"""
            if isinstance(product, Product):
                self.__products.append(product)
                Category.product_count += 1
            else:
                raise ValueError("Только объекты класса Product могут быть добавлены.")

    def get_product_count(self):
        """Возвращает количество продуктов в категории"""
        return len(self.__products)

    @property
    def products(self):
        """Геттер который возвращает продукты"""
        return "\n".join([f"{product.name}, {product.price}руб. Остаток: {product.quantity} шт.\n"
                          for product in self.__products])


    def __str__(self):
        """Переопределен метод __str__, который возвращает строку"""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name},  количество продуктов: {total_quantity} шт."
