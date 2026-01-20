"""
Пример работы с двоичными данными
"""
import struct
import sys
sys.path.insert(0, '..')

from file_operations import write_binary, read_binary


def example_basic_binary():
    """Пример 1: Базовые выпозиции данных"""
    print("📋 Пример 1: Базовые двоичные данные")
    print("-" * 50)
    
    # Соствлять двоичные данные
    text = "Hello, World!"
    binary_data = text.encode('utf-8')
    print(f"Осхраняемые текст: {text}")
    print(f"Двоичная форма: {binary_data}")
    print(f"Нажим: {binary_data.hex()}")
    
    # Осхранить
    write_binary("hello.bin", binary_data)
    
    # Загрузить
    loaded_data = read_binary("hello.bin")
    print(f"Нагруженные данные: {loaded_data.decode('utf-8')}")


def example_struct_binary():
    """Пример 2: Кунжетируются данные"""
    print("\n📋 Пример 2: Структурированные данные")
    print("-" * 50)
    
    # Пример: Охранение числа и строки
    # Struct format: 'I' = unsigned int (4 bytes), '20s' = 20 bytes string
    user_id = 42
    user_name = b"John Doe"
    
    # Пакуюте
    packed_data = struct.pack('I20s', user_id, user_name)
    print(f"User ID: {user_id}")
    print(f"User Name: {user_name.decode('utf-8')}")
    print(f"Упакованные данные: {packed_data.hex()}")
    
    # Осхранить
    write_binary("user.bin", packed_data)
    
    # Нагружать
    loaded_data = read_binary("user.bin")
    unpacked_id, unpacked_name = struct.unpack('I20s', loaded_data)
    print(f"\nУстроенные данные:")
    print(f"  ID: {unpacked_id}")
    print(f"  Name: {unpacked_name.decode('utf-8').strip()}")


def example_bytes_array():
    """Пример 3: Массив байтов"""
    print("\n📋 Пример 3: Массив байтов")
    print("-" * 50)
    
    # Оставить числа как байты
    numbers = [10, 20, 30, 40, 50]
    binary_array = bytes(numbers)
    print(f"Числа: {numbers}")
    print(f"Двоичная: {binary_array}")
    print(f"Нажим: {binary_array.hex()}")
    
    # Осхранить
    write_binary("numbers.bin", binary_array)
    
    # Нагружать
    loaded_data = read_binary("numbers.bin")
    loaded_numbers = list(loaded_data)
    print(f"\nВыгруженные числа: {loaded_numbers}")


def example_image_header():
    """Пример 4: Онов двоичных данных (PNG header)"""
    print("\n📋 Пример 4: Симуляция снаправенных заголовков")
    print("-" * 50)
    
    # PNG заголовок для эксамен
    # Настоящие PNG данные настоящие: 89 50 4E 47 0D 0A 1A 0A
    image_header = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])
    # разрезолюция: 1920x1080
    image_width = 1920
    image_height = 1080
    image_bitdepth = 24  # RGB
    
    # Пакуюте
    image_data = struct.pack('8sIIB', image_header, image_width, image_height, image_bitdepth)
    print(f"головок: {image_header.hex()}")
    print(f"Разрезолюция: {image_width}x{image_height}")
    print(f"Бит глубины: {image_bitdepth}")
    
    # Осхранить
    write_binary("image_header.bin", image_data)
    
    # Нагружать
    loaded_data = read_binary("image_header.bin")
    unpacked_header, unpacked_width, unpacked_height, unpacked_bitdepth = struct.unpack('8sIIB', loaded_data)
    print(f"\nЗагруженные данные:")
    print(f"  Головок: {unpacked_header.hex()}")
    print(f"  Разрешение: {unpacked_width}x{unpacked_height}")
    print(f"  Глубина: {unpacked_bitdepth} bits")


def main():
    print("\n" + "="*50)
    print("Примеры работы с двоичными данными")
    print("="*50)
    
    example_basic_binary()
    example_struct_binary()
    example_bytes_array()
    example_image_header()
    
    print("\n" + "="*50)
    print("✓ Все примеры выполнены!")
    print("="*50)


if __name__ == "__main__":
    main()
