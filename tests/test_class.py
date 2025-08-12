import pytest
from src.product import Product
from src.product import Category


@pytest.fixture
def class_product():
    return Product("banana", "Only big size", 150, 174.50)


def test_product(class_product):
    """Тест на инициализацию Product"""
    assert class_product.name == "banana"
    assert class_product.description == "Only big size"
    assert class_product.quantity == 150
    assert class_product.price == 174.50


@pytest.fixture
def class_category():
    return Category("fruit", "import", ["product1", "product2", "product3"])


def test_category_count():
    """ Тест проверяет подсчет количество в category"""
    Category.category_count = 0
    category = Category("fruit", "import", ["product1", "product2"])
    assert Category.category_count == 1


def test_price_getter():
    """Тестирует корректную цену"""
    product = Product("banana", "Only big size", 150, 174.50)
    # Устанавливаем корректную цену
    assert product.price == 174.50


def test_new_product():
    product = Product.new_product("pear", "red", 520, 187)
    assert product.name == "pear"
    assert product.description == "red"
    assert product.quantity == 520
    assert product.price == 187


def test_one_get_product_count():
    product1 = Product("banana", "Only big size", 150, 174.50)
    category = Category("fruit", "import", [product1])
    assert product1 == product1
    assert category == category


def test_get_product_count():
    product1 = Product("banana", "Only big size", 150, 174.50)
    product2 = Product("apple", "Only red", 200, 67.80)
    category = Category("fruit", "import", [product1])
    assert category.get_product_count() == 1
    category.add_product(product2)
    assert category.get_product_count() == 2


def test_add_invalid_product():
    category = Category("fruit", "import", [])
    with pytest.raises(ValueError, match="Только объекты класса Product могут быть добавлены."):
        category.add_product("not a product")


def test_add_product_success():
    product = Product("banana", "Only big size", 150, 174.50)
    category = Category("fruit", "import", [])
    category.add_product(product)
    assert category._Category__products[0] == product
