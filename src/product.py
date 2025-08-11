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
        self.products = products
        Category.category_count += 1   # Добавляем +1 Категорию
        Category.product_count += len(products)  # К уже существующему количеству добавляем product
