from src.product import Product, Category
""" Исполняемый код из product.py"""
product1 = Product("banana", "Only big size", 150, 174.50)
product2 = Product("apple", "Only red", 200, 67.80)
product3 = Product("orange", "Argentina", 80, 95.00)


category = Category("fruit", "import", [product1, product2, product3])


print("Новое количество продуктов в категории:", category.get_product_count())
print("Общее количество продуктов:", Category.product_count)
print("Количество категорий:", Category.category_count)
print(category.get_product_list)
product4 = Product.new_product("pear", "red", 520, 187)
print(f"Название: {product4.name}, Описание: {product4.description}, "
      f"Количество на складе: {product4.quantity}, цена {product4.price} ")
product4.price = 200  # new_price будет 200
product4.price = -10  #new_price -10
print(product4.price)  # Выведет 200


