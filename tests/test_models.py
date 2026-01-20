"""
Тесты для моделей
"""
import pytest
import sys
sys.path.insert(0, '..')

from models import User, Product, Order, Database


class TestUser:
    """Тесты для класса User"""
    
    def test_user_creation(self):
        """Поверить составление пользователя"""
        user = User(1, "Владимир", "vladimir@example.com")
        assert user.user_id == 1
        assert user.name == "Владимир"
        assert user.email == "vladimir@example.com"
    
    def test_user_equality(self):
        """Проверить равенство пользователей"""
        user1 = User(1, "Андрей", "andrey@example.com")
        user2 = User(1, "Андрей", "andrey2@example.com")
        assert user1 == user2
    
    def test_user_repr(self):
        """Проверить строковыо представление"""
        user = User(1, "Дмитрий", "dmitry@example.com")
        repr_str = repr(user)
        assert "User" in repr_str
        assert "1" in repr_str
        assert "Дмитрий" in repr_str


class TestProduct:
    """Тесты для класса Product"""
    
    def test_product_creation(self):
        """Поверить составление продукта"""
        product = Product(1, "Лаптоп", 50000.00, 5)
        assert product.product_id == 1
        assert product.name == "Лаптоп"
        assert product.price == 50000.00
        assert product.stock == 5
    
    def test_product_equality(self):
        """Проверить равенство продуктов"""
        prod1 = Product(1, "Ните", 100.00, 10)
        prod2 = Product(1, "Ните", 100.00, 20)
        assert prod1 == prod2
    
    def test_product_repr(self):
        """Проверить строковыо представление"""
        product = Product(2, "Монитор", 15000.00, 3)
        repr_str = repr(product)
        assert "Product" in repr_str
        assert "2" in repr_str
        assert "Монитор" in repr_str


class TestOrder:
    """Тесты для класса Order"""
    
    def test_order_creation(self):
        """Поверить составление заказа"""
        user = User(1, "Георгий", "george@example.com")
        products = [
            Product(1, "Ните", 100.00, 2),
            Product(2, "Монитор", 300.00, 1)
        ]
        order = Order(1, user, products, 400.00)
        
        assert order.order_id == 1
        assert order.user == user
        assert len(order.products) == 2
        assert order.total == 400.00
        assert order.status == "pending"
    
    def test_order_complete(self):
        """Проверить завершение заказа"""
        user = User(2, "Елена", "elena@example.com")
        order = Order(2, user, [], 1000.00)
        
        order.complete()
        assert order.status == "completed"
    
    def test_order_cancel(self):
        """Проверить отмену заказа"""
        user = User(3, "Олег", "oleg@example.com")
        order = Order(3, user, [], 2000.00)
        
        order.cancel()
        assert order.status == "cancelled"


class TestDatabase:
    """Тесты для класса Database"""
    
    def test_database_creation(self):
        """Поверить составление базы"""
        db = Database()
        assert len(db.users) == 0
        assert len(db.products) == 0
        assert len(db.orders) == 0
    
    def test_add_user(self):
        """Поверить добавление пользователя"""
        db = Database()
        user = User(1, "Татьяна", "tatiana@example.com")
        db.add_user(user)
        
        assert len(db.users) == 1
        assert db.users[0] == user
    
    def test_add_product(self):
        """Поверить добавление продукта"""
        db = Database()
        product = Product(1, "Книга", 250.00, 50)
        db.add_product(product)
        
        assert len(db.products) == 1
        assert db.products[0] == product
    
    def test_get_user(self):
        """Поверить получение пользователя"""
        db = Database()
        user = User(5, "Сергей", "sergey@example.com")
        db.add_user(user)
        
        found_user = db.get_user(5)
        assert found_user is not None
        assert found_user == user
    
    def test_get_product(self):
        """Поверить получение продукта"""
        db = Database()
        product = Product(3, "Телевизор", 25000.00, 2)
        db.add_product(product)
        
        found_product = db.get_product(3)
        assert found_product is not None
        assert found_product == product


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
