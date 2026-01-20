"""
Тесты для модуля сериализации
"""
import pytest
import sys
import os
sys.path.insert(0, '..')

from serialization import PickleSerializer, JSONSerializer
from models import User, Product, Database
from pathlib import Path

# Тестовая директория
TEST_DIR = "test_data"


@pytest.fixture(scope="function")
def test_directory():
    """Убедиться и очистить тестовую директорию"""
    Path(TEST_DIR).mkdir(exist_ok=True)
    yield TEST_DIR
    # Очистить после теста
    import shutil
    if os.path.exists(TEST_DIR):
        shutil.rmtree(TEST_DIR)


class TestPickleSerializer:
    """Тесты для pickle сериализера"""
    
    def test_serialize_user(self, test_directory):
        """Проверить сериализацию User"""
        user = User(1, "Тестовый", "test@example.com")
        PickleSerializer.serialize(user, "test_user.pkl", test_directory)
        
        assert os.path.exists(os.path.join(test_directory, "test_user.pkl"))
    
    def test_deserialize_user(self, test_directory):
        """Проверить десериализацию User"""
        original_user = User(2, "Оригинал", "original@example.com")
        PickleSerializer.serialize(original_user, "test_user.pkl", test_directory)
        
        loaded_user = PickleSerializer.deserialize("test_user.pkl", test_directory)
        
        assert loaded_user == original_user
        assert loaded_user.user_id == original_user.user_id
        assert loaded_user.name == original_user.name
        assert loaded_user.email == original_user.email
    
    def test_serialize_deserialize_database(self, test_directory):
        """Проверить сериализацию/десериализацию Database"""
        db = Database()
        db.add_user(User(1, "Jude", "jude@example.com"))
        db.add_user(User(2, "Grace", "grace@example.com"))
        db.add_product(Product(1, "Item1", 100.00, 5))
        db.add_product(Product(2, "Item2", 200.00, 3))
        
        PickleSerializer.serialize(db, "test_db.pkl", test_directory)
        loaded_db = PickleSerializer.deserialize("test_db.pkl", test_directory)
        
        assert len(loaded_db.users) == 2
        assert len(loaded_db.products) == 2
        assert loaded_db.users[0].name == "Jude"
        assert loaded_db.products[0].price == 100.00
    
    def test_serialize_to_bytes(self):
        """Проверить сериализацию в байты"""
        user = User(3, "ByteUser", "byte@example.com")
        data = PickleSerializer.serialize_to_bytes(user)
        
        assert isinstance(data, bytes)
        assert len(data) > 0
    
    def test_deserialize_from_bytes(self):
        """Проверить десериализацию из байтов"""
        original_user = User(4, "ByteTest", "bytetest@example.com")
        data = PickleSerializer.serialize_to_bytes(original_user)
        
        loaded_user = PickleSerializer.deserialize_from_bytes(data)
        
        assert loaded_user == original_user
        assert loaded_user.name == "ByteTest"


class TestJSONSerializer:
    """Тесты для JSON сериализера"""
    
    def test_serialize_dict(self, test_directory):
        """Проверить сериализацию словаря"""
        data = {"name": "John", "age": 30, "city": "Ню-Йорк"}
        JSONSerializer.serialize(data, "test_dict.json", test_directory)
        
        assert os.path.exists(os.path.join(test_directory, "test_dict.json"))
    
    def test_deserialize_dict(self, test_directory):
        """Проверить десериализацию словаря"""
        original_data = {"name": "Alice", "age": 25, "city": "Париж"}
        JSONSerializer.serialize(original_data, "test_dict.json", test_directory)
        
        loaded_data = JSONSerializer.deserialize("test_dict.json", test_directory)
        
        assert loaded_data == original_data
        assert loaded_data["name"] == "Alice"
    
    def test_serialize_list(self, test_directory):
        """Проверить сериализацию списка"""
        items = [
            {"id": 1, "name": "Item1", "price": 100},
            {"id": 2, "name": "Item2", "price": 200}
        ]
        JSONSerializer.serialize(items, "test_list.json", test_directory)
        
        assert os.path.exists(os.path.join(test_directory, "test_list.json"))
    
    def test_deserialize_list(self, test_directory):
        """Проверить десериализацию списка"""
        original_items = [
            {"id": 1, "name": "Product1"},
            {"id": 2, "name": "Product2"},
            {"id": 3, "name": "Product3"}
        ]
        JSONSerializer.serialize(original_items, "test_list.json", test_directory)
        
        loaded_items = JSONSerializer.deserialize("test_list.json", test_directory)
        
        assert len(loaded_items) == 3
        assert loaded_items[0]["name"] == "Product1"
    
    def test_serialize_nested_data(self, test_directory):
        """Проверить сериализацию ложенных данных"""
        nested = {
            "company": "ACME Corp",
            "departments": [
                {"name": "IT", "employees": 10},
                {"name": "HR", "employees": 5}
            ]
        }
        JSONSerializer.serialize(nested, "test_nested.json", test_directory)
        
        loaded = JSONSerializer.deserialize("test_nested.json", test_directory)
        
        assert loaded["company"] == "ACME Corp"
        assert len(loaded["departments"]) == 2
        assert loaded["departments"][0]["name"] == "IT"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
