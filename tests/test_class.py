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
    return Category("fruit", "import", ["product1", "product2"])


def test_category(class_category):
    """Тест на инициализацию category"""
    assert class_category.name == "fruit"
    assert class_category.description == "import"
    assert class_category.products == ["product1", "product2"]


def test_product_count():
    """ Тест подсчитывает количество в product"""
    Product.product_count = 0
    product1 = Product("banana", "Only big size", 150, 174.50)
    product2 = Product("apple", "Only red", 200, 67.80)
    assert Product.product_count == 2


def test_category_count():
    """ Тест подсчитывает количество в category"""
    Category.category_count = 0
    category = Category("fruit", "import", ["product1", "product2"])
    assert Category.category_count == 1
