"""
Модели данных для приложения
"""
from datetime import datetime
from typing import List


class User:
    """Класс пользователя"""
    
    def __init__(self, user_id: int, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.created_at = datetime.now()
    
    def __repr__(self) -> str:
        return f"User(id={self.user_id}, name='{self.name}', email='{self.email}')"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, User):
            return False
        return self.user_id == other.user_id and self.name == other.name


class Product:
    """Класс продукта"""
    
    def __init__(self, product_id: int, name: str, price: float, stock: int):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
    
    def __repr__(self) -> str:
        return f"Product(id={self.product_id}, name='{self.name}', price={self.price}$, stock={self.stock})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Product):
            return False
        return (self.product_id == other.product_id and 
                self.name == other.name and 
                self.price == other.price)


class Order:
    """Класс заказа"""
    
    def __init__(self, order_id: int, user: User, products: List[Product], total: float):
        self.order_id = order_id
        self.user = user
        self.products = products
        self.total = total
        self.created_at = datetime.now()
        self.status = "pending"
    
    def __repr__(self) -> str:
        product_names = ', '.join([p.name for p in self.products])
        return f"Order(id={self.order_id}, user='{self.user.name}', products=[{product_names}], total={self.total}$, status='{self.status}')"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Order):
            return False
        return self.order_id == other.order_id and self.user == other.user
    
    def complete(self):
        """Completed the order"""
        self.status = "completed"
    
    def cancel(self):
        """Cancel the order"""
        self.status = "cancelled"


class Database:
    """Класс для работы с базой данных"""
    
    def __init__(self):
        self.users: List[User] = []
        self.products: List[Product] = []
        self.orders: List[Order] = []
    
    def add_user(self, user: User) -> None:
        """Добавить пользователя"""
        if not any(u.user_id == user.user_id for u in self.users):
            self.users.append(user)
    
    def add_product(self, product: Product) -> None:
        """Добавить продукт"""
        if not any(p.product_id == product.product_id for p in self.products):
            self.products.append(product)
    
    def add_order(self, order: Order) -> None:
        """Добавить заказ"""
        if not any(o.order_id == order.order_id for o in self.orders):
            self.orders.append(order)
    
    def get_user(self, user_id: int) -> User:
        """Получить пользователя по ID"""
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None
    
    def get_product(self, product_id: int) -> Product:
        """Получить продукт по ID"""
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None
    
    def __repr__(self) -> str:
        return f"Database(users={len(self.users)}, products={len(self.products)}, orders={len(self.orders)})"
