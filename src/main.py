from src. product import Product, Category

""" Исполняемый код из product.py"""
product1 = Product("banana", "Only big size", 150, 174.50)
product2 = Product("apple", "Only red", 200, 67.80)
product3 = Product("orange", "Argentina", 80, 95.00)


category = Category("fruit", "import", [product1, product2, product3])


print("Новое количество продуктов в категории:", len(category.products))
print("Общее количество продуктов:", Category.product_count)
print("Количество категорий:", Category.category_count)


