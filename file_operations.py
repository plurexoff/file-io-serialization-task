"""
Операции для работы с файлами
"""
import os
from pathlib import Path
from typing import Union


def ensure_data_dir(directory: str = 'data') -> str:
    """Обеспечить существование директории"""
    Path(directory).mkdir(parents=True, exist_ok=True)
    return directory


def write_text(filename: str, content: str, directory: str = 'data') -> None:
    """Записать текст в файл
    
    Args:
        filename: Название файла
        content: Содержимое для записи
        directory: Директория
    """
    ensure_data_dir(directory)
    file_path = os.path.join(directory, filename)
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Файл '{file_path}' успешно сохранён")
    except IOError as e:
        print(f"✗ Ошибка при записи: {e}")
        raise


def read_text(filename: str, directory: str = 'data') -> str:
    """Прочитать текст из файла
    
    Args:
        filename: Название файла
        directory: Директория
    
    Returns:
        Одочтенное содержимое
    """
    file_path = os.path.join(directory, filename)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"✓ Набор данных из '{file_path}'")
        return content
    except IOError as e:
        print(f"✗ Ошибка при чтении: {e}")
        raise


def write_binary(filename: str, data: bytes, directory: str = 'data') -> None:
    """Записать двоичные данные в файл
    
    Args:
        filename: Название файла
        data: Двоичные данные
        directory: Директория
    """
    ensure_data_dir(directory)
    file_path = os.path.join(directory, filename)
    try:
        with open(file_path, 'wb') as f:
            f.write(data)
        print(f"✓ Файл '{file_path}' успешно сохранён ({len(data)} байт)")
    except IOError as e:
        print(f"✗ Ошибка при записи: {e}")
        raise


def read_binary(filename: str, directory: str = 'data') -> bytes:
    """Прочитать двоичные данные из файла
    
    Args:
        filename: Название файла
        directory: Директория
    
    Returns:
        Одочтенные двоичные данные
    """
    file_path = os.path.join(directory, filename)
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        print(f"✓ Набор данных из '{file_path}' ({len(data)} байт)")
        return data
    except IOError as e:
        print(f"✗ Ошибка при чтении: {e}")
        raise


def file_exists(filename: str, directory: str = 'data') -> bool:
    """Проверить существование файла
    
    Args:
        filename: Название файла
        directory: Директория
    
    Returns:
        True если файл существует
    """
    file_path = os.path.join(directory, filename)
    return os.path.exists(file_path)


def get_file_size(filename: str, directory: str = 'data') -> int:
    """Получить размер файла в байтах
    
    Args:
        filename: Название файла
        directory: Директория
    
    Returns:
        Размер в байтах
    """
    file_path = os.path.join(directory, filename)
    if os.path.exists(file_path):
        return os.path.getsize(file_path)
    return 0


def delete_file(filename: str, directory: str = 'data') -> bool:
    """Удалить файл
    
    Args:
        filename: Название файла
        directory: Директория
    
    Returns:
        True если файл успешно удален
    """
    file_path = os.path.join(directory, filename)
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"✓ Файл '{file_path}' удален")
            return True
        else:
            print(f"✗ Файл '{file_path}' не найден")
            return False
    except IOError as e:
        print(f"✗ Ошибка при удалении: {e}")
        return False


def list_files(directory: str = 'data') -> list:
    """Получить перечень всех файлов в директории
    
    Args:
        directory: Директория
    
    Returns:
        Лист названий файлов
    """
    if not os.path.exists(directory):
        return []
    return [
        f for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f))
    ]
