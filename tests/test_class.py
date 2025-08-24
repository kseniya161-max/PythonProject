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
    product_data = ({"name": "Samsung Galaxy S23 Ultra",
                     "description": "256GB, Серый цвет, 200MP камера",
                     "price": 180000.0, "quantity": 5})
    product = Product.new_product(product_data)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


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


@pytest.fixture
def product_galaxy():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product_iphone():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product_xiaomi():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def category_smartphones(product_galaxy, product_iphone, product_xiaomi):
    return Category("Смартфоны",
                    "Смартфоны, как средство не только коммуникации, "
                    "но и получения дополнительных функций для удобства жизни",
                    [product_galaxy, product_iphone, product_xiaomi])


def test_adding_product(product_galaxy, product_iphone):
    expected = product_galaxy.quantity * product_galaxy.price + product_iphone.quantity * product_iphone.price
    assert (product_galaxy + product_iphone) == expected


def test_string_product(category_smartphones):
    expected = "Смартфоны,  Количество продуктов: 421000.0 шт."
    assert str(category_smartphones) == expected
