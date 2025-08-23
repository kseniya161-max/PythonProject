from src.product import Product, Category
# """ Исполняемый код из product.py"""
# product1 = Product("banana", "Only big size", 150, 174.50)
# product2 = Product("apple", "Only red", 200, 67.80)
# product3 = Product("orange", "Argentina", 80, 95.00)
#
#
# category = Category("fruit", "import", [product1, product2, product3])
#
#
# print("Новое количество продуктов в категории:", category.get_product_count())
# print("Общее количество продуктов:", Category.product_count)
# print("Количество категорий:", Category.category_count)
# print(category.get_product_list)
# product4 = Product.new_product("pear", "red", 520, 187)
# print(f"Название: {product4.name}, Описание: {product4.description}, "
#       f"Количество на складе: {product4.quantity}, цена {product4.price} ")
# product4.price = 200  # new_price будет 200
# product4.price = -10  # new_price -10
# print(product4.price)  # Выведет 200

# Исполняемый код для проверки метода add_product

#
# product1 = Product("banana", "Only big size", 150, 174.50)
# product2 = Product("apple", "Only red", 200, 67.80)
# product3 = Product("orange", "Argentina", 80, 95.00)
#
# # Категории с пустыми продуктами
# category = Category("fruit", "import", [])

# Начальное количество
# print("Начальное количество продуктов в категории:", category.get_product_count())
#
# # Добавляем продукты в категорию
# category.add_product(product1)
# category.add_product(product2)
# category.add_product(product3)
#
# # Проверяем количество продуктов после добавления
# print("Количество продуктов в категории после добавления:", category.get_product_count())
#
# # Выводим список продуктов в категории
# print("Список продуктов в категории:")
# print(category.get_product_list)

# if __name__ == "__main__":
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [product1, product2, product3]
#     )
#
#     print(category1.products)
#     product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
#     category1.add_product(product4)
#     print(category1.products)
#     print(category1.product_count)
#
#     new_product = Product.new_product(
#         {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
#          "quantity": 5})
#     print(new_product.name)
#     print(new_product.description)
#     print(new_product.price)
#     print(new_product.quantity)
#
#     new_product.price = 800
#     print(new_product.price)
#
#     new_product.price = -100
#     print(new_product.price)
#     new_product.price = 0
#     print(new_product.price)


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))

    print(category1.products)

    # print(product1 + product2)
    # print(product1 + product3)
    # print(product2 + product3)