class Product:
    """Создаем класс Product"""
    # Атрибут класса который считает количество продуктов
    product_count = 0

    def __init__(self, name: str, description: str, quantity: int, price: float):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price
        Product. product_count += 1   # Добавляем +1 Product


class Category:
    """Создаем класс Category"""
    # атрибут класса считает количество категорий
    category_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1   # Добавляем +1 Категорию


product1 = Product("banana", "Only big size", 150, 174.50)
product2 = Product("apple", "Only red", 200, 67.80)

category = Category("fruit", "import", [product1, product2])

print(Product. product_count)
print(Category.category_count)
