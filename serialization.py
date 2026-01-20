"""
Модуль для сериализации и десериализации объектов
"""
import pickle
import json
from typing import Any, TypeVar
from pathlib import Path

T = TypeVar('T')


class PickleSerializer:
    """сериалайзер для pickle"""
    
    @staticmethod
    def serialize(obj: Any, filename: str, directory: str = 'data') -> None:
        """Сериализовать объект в pickle файл
        
        Args:
            obj: Объект для сериализации
            filename: Название файла
            directory: Директория
        """
        Path(directory).mkdir(parents=True, exist_ok=True)
        file_path = Path(directory) / filename
        
        try:
            with open(file_path, 'wb') as f:
                pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
            print(f"✓ Объект сериализован в '{file_path}'")
        except Exception as e:
            print(f"✗ Ошибка сериализации: {e}")
            raise
    
    @staticmethod
    def deserialize(filename: str, directory: str = 'data') -> Any:
        """Десериализовать объект из pickle файла
        
        Args:
            filename: Название файла
            directory: Директория
        
        Returns:
            Десериализованный объект
        """
        file_path = Path(directory) / filename
        
        try:
            with open(file_path, 'rb') as f:
                obj = pickle.load(f)
            print(f"✓ Объект десериализован из '{file_path}'")
            return obj
        except Exception as e:
            print(f"✗ Ошибка десериализации: {e}")
            raise
    
    @staticmethod
    def serialize_to_bytes(obj: Any) -> bytes:
        """Сериализовать объект в байты
        
        Args:
            obj: Объект для сериализации
        
        Returns:
            сериализованные байты
        """
        return pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL)
    
    @staticmethod
    def deserialize_from_bytes(data: bytes) -> Any:
        """Десериализовать объект из байтов
        
        Args:
            data: байты для десериализации
        
        Returns:
            десериализованный объект
        """
        return pickle.loads(data)


class JSONSerializer:
    """сериалайзер для JSON"""
    
    @staticmethod
    def serialize(obj: Any, filename: str, directory: str = 'data') -> None:
        """Сериализовать объект в JSON файл
        
        Args:
            obj: Объект для сериализации
            filename: Название файла
            directory: Директория
        """
        Path(directory).mkdir(parents=True, exist_ok=True)
        file_path = Path(directory) / filename
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(obj, f, indent=2, ensure_ascii=False, default=str)
            print(f"✓ Объект сериализован в '{file_path}'")
        except Exception as e:
            print(f"✗ Ошибка сериализации: {e}")
            raise
    
    @staticmethod
    def deserialize(filename: str, directory: str = 'data') -> Any:
        """Десериализовать объект из JSON файла
        
        Args:
            filename: Название файла
            directory: Директория
        
        Returns:
            десериализованный объект
        """
        file_path = Path(directory) / filename
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                obj = json.load(f)
            print(f"✓ Объект десериализован из '{file_path}'")
            return obj
        except Exception as e:
            print(f"✗ Ошибка десериализации: {e}")
            raise
