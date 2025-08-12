class Product:
    """Создаем класс Product"""

    def __init__(self, name: str, description: str, quantity: int, price: float):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price


class Category:
    """Создаем класс Category"""
    # атрибут класса считает количество категорий
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products  # Тут хранятся product1, product1, product1
        Category.category_count += 1   # Добавляем +1 Категорию


    def add_product(self, product: Product):
        """Метод который добавляет приватный продукт в категорию"""
        self.__products.append(product)  # Тут добавляем атрибут product в приватные атрибуты
        Category.product_count += 1    # Уыеличиваем количество продуктов в категории product1, product1, product1

    def get_product_count(self):
        """Возвращает количество продуктов в категории"""
        return len(self.__products)


""" Исполняемый код из product.py"""
product1 = Product("banana", "Only big size", 150, 174.50)
product2 = Product("apple", "Only red", 200, 67.80)
product3 = Product("orange", "Argentina", 80, 95.00)


category = Category("fruit", "import", [product1, product2, product3])


print("Новое количество продуктов в категории:", category.get_product_count())
print("Общее количество продуктов:", Category.product_count)
print("Количество категорий:", Category.category_count)


