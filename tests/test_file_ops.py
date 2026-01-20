"""
Тесты для модуля работы с файлами
"""
import pytest
import sys
import os
sys.path.insert(0, '..')

from file_operations import (
    write_text, read_text, write_binary, read_binary,
    file_exists, get_file_size, delete_file, list_files,
    ensure_data_dir
)
from pathlib import Path

# Тестовая директория
TEST_DIR = "test_files"


@pytest.fixture(scope="function")
def test_directory():
    """Установить и очистить тестовую директорию"""
    ensure_data_dir(TEST_DIR)
    yield TEST_DIR
    # Очистить после теста
    import shutil
    if os.path.exists(TEST_DIR):
        shutil.rmtree(TEST_DIR)


class TestTextOperations:
    """Тесты для текстовых операций"""
    
    def test_write_text(self, test_directory):
        """Проверить запись текста"""
        content = "Привет, мир!"
        write_text("test.txt", content, test_directory)
        
        assert os.path.exists(os.path.join(test_directory, "test.txt"))
    
    def test_read_text(self, test_directory):
        """Проверить чтение текста"""
        original_content = "Привет, Питон!"
        write_text("test.txt", original_content, test_directory)
        
        read_content = read_text("test.txt", test_directory)
        
        assert read_content == original_content
    
    def test_write_read_multiline(self, test_directory):
        """Проверить многострочные тексты"""
        content = """"Line 1
Line 2
Line 3Линия 4Линия 5"""
        write_text("multiline.txt", content, test_directory)
        
        read_content = read_text("multiline.txt", test_directory)
        
        assert read_content == content
        assert read_content.count('\n') == 4


class TestBinaryOperations:
    """Тесты для двоичных операций"""
    
    def test_write_binary(self, test_directory):
        """Проверить запись двоичных данных"""
        data = bytes([0x48, 0x65, 0x6C, 0x6C, 0x6F])  # "Hello"
        write_binary("test.bin", data, test_directory)
        
        assert os.path.exists(os.path.join(test_directory, "test.bin"))
    
    def test_read_binary(self, test_directory):
        """Проверить чтение двоичных данных"""
        original_data = bytes([0x01, 0x02, 0x03, 0x04, 0x05])
        write_binary("test.bin", original_data, test_directory)
        
        read_data = read_binary("test.bin", test_directory)
        
        assert read_data == original_data
    
    def test_binary_text_encoding(self, test_directory):
        """Проверить кодирование текста"""
        text = "Hello, Мир!"
        binary_data = text.encode('utf-8')
        write_binary("encoded.bin", binary_data, test_directory)
        
        read_data = read_binary("encoded.bin", test_directory)
        decoded_text = read_data.decode('utf-8')
        
        assert decoded_text == text


class TestFileManagement:
    """Тесты для администрирования файлами"""
    
    def test_file_exists(self, test_directory):
        """Проверить наличие файла"""
        write_text("test.txt", "content", test_directory)
        
        assert file_exists("test.txt", test_directory) == True
        assert file_exists("nonexistent.txt", test_directory) == False
    
    def test_get_file_size(self, test_directory):
        """Проверить получение размера файла"""
        content = "Hello"
        write_text("test.txt", content, test_directory)
        
        size = get_file_size("test.txt", test_directory)
        
        assert size > 0
    
    def test_delete_file(self, test_directory):
        """Проверить удаление файла"""
        write_text("to_delete.txt", "content", test_directory)
        assert file_exists("to_delete.txt", test_directory) == True
        
        result = delete_file("to_delete.txt", test_directory)
        
        assert result == True
        assert file_exists("to_delete.txt", test_directory) == False
    
    def test_list_files(self, test_directory):
        """Проверить список файлов"""
        write_text("file1.txt", "content1", test_directory)
        write_text("file2.txt", "content2", test_directory)
        write_binary("file3.bin", b"binary", test_directory)
        
        files = list_files(test_directory)
        
        assert len(files) == 3
        assert "file1.txt" in files
        assert "file2.txt" in files
        assert "file3.bin" in files
    
    def test_list_empty_directory(self, test_directory):
        """Проверить список архивированных файлов"""
        empty_dir = os.path.join(test_directory, "empty")
        ensure_data_dir(empty_dir)
        
        files = list_files(empty_dir)
        
        assert len(files) == 0
    
    def test_ensure_data_dir(self):
        """Проверить сохранение директории"""
        test_dir = "ensure_test_dir"
        ensure_data_dir(test_dir)
        
        assert os.path.exists(test_dir)
        assert os.path.isdir(test_dir)
        
        # Очистить
        import shutil
        shutil.rmtree(test_dir)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
