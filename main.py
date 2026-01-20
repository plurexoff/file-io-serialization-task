"""
Основное приложение для работы с файлами и сериализацией
"""
from models import User, Product, Order, Database
from serialization import PickleSerializer, JSONSerializer
from file_operations import write_binary, read_binary, delete_file, list_files


def print_menu():
    """Печать меню"""
    print("\n" + "="*50)
    print("ФАЙЛОВАЯ ГОВОЛОВ И СЕРИАЛИЗАЦИЯ")
    print("="*50)
    print("1. Сохранить объект User (пикл)")
    print("2. Загрузить объект User (пикл)")
    print("3. Сохранить БД (пикл)")
    print("4. Загрузить БД (пикл)")
    print("5. Сохранить Данные (JSON)")
    print("6. Посмотреть файлы")
    print("7. Открыть бинарные данные")
    print("8. Удалить файл")
    print("0. Выход")
    print("="*50)


def demo_save_user():
    """Демо: сохранить объект User"""
    print("\n👤 Сохранение объекта User...")
    
    # Составление пользователя
    user = User(
        user_id=1,
        name="Петр Петров",
        email="petr@example.com"
    )
    
    print(f"Объект: {user}")
    
    # Сериализация
    PickleSerializer.serialize(user, "user.pkl")
    print(f"Файл осхранен: data/user.pkl")


def demo_load_user():
    """Демо: загрузить объект User"""
    print("\n👤 Загрузка объекта User...")
    
    try:
        user = PickleSerializer.deserialize("user.pkl")
        print(f"Остается объект: {user}")
        print(f"Открыта: {user.created_at}")
    except FileNotFoundError:
        print("✗ Файл не найден. сначала сохраните объект.")


def demo_save_database():
    """Демо: сохранить БД"""
    print("\n💾 Сохранение базы данных...")
    
    # Составление базы данных
    db = Database()
    
    # Увеличение пользователей
    users = [
        User(1, "Анастасия", "anastasia@example.com"),
        User(2, "Борис", "boris@example.com"),
        User(3, "Виктория", "victoria@example.com"),
    ]
    for user in users:
        db.add_user(user)
    
    # Увеличение продуктов
    products = [
        Product(1, "Лаптоп", 50000.00, 5),
        Product(2, "Пульт", 1500.00, 20),
        Product(3, "Книга", 300.00, 100),
    ]
    for product in products:
        db.add_product(product)
    
    print(f"БД: {db}")
    
    # сериализация
    PickleSerializer.serialize(db, "database.pkl")
    print(f"Файл осхранен: data/database.pkl")


def demo_load_database():
    """Демо: загружить БД"""
    print("\n💾 Загружка базы данных...")
    
    try:
        db = PickleSerializer.deserialize("database.pkl")
        print(f"Навдена БД: {db}")
        print(f"\nПользователи:")
        for user in db.users:
            print(f"  - {user}")
        print(f"\nПродукты:")
        for product in db.products:
            print(f"  - {product}")
    except FileNotFoundError:
        print("✗ Файл не найден. сначала сохраните БД.")


def demo_save_json():
    """Демо: сохранить данные (JSON)"""
    print("\n📌 Сохранение данных (JSON)...")
    
    data = {
        "комнаты": [
            {
                "а": 1,
                "им": "Анна",
                "почта": "anna@example.com",
                "цена": 3000.00
            },
            {
                "а": 2,
                "им": "Виктор",
                "почта": "viktor@example.com",
                "цена": 2500.00
            }
        ]
    }
    
    JSONSerializer.serialize(data, "data.json")
    print(f"Файл осхранен: data/data.json")


def demo_list_files():
    """Демо: посмотреть файлы"""
    print("\n📁 Наявные файлы:")
    
    files = list_files()
    if not files:
        print("✗ В директории data/ нет файлов")
    else:
        for i, file in enumerate(files, 1):
            print(f"  {i}. {file}")


def demo_binary_data():
    """Демо: работа с двоичными данными"""
    print("\n📋 Работа с двоичными данными...")
    
    # Одание двоичных данных
    binary_data = bytes([
        0x48, 0x65, 0x6C, 0x6C, 0x6F,  # "Hello"
        0x20,                           # space
        0x57, 0x6F, 0x72, 0x6C, 0x64   # "World"
    ])
    
    print(f"Оданные: {binary_data}")
    print(f"Декодированные: {binary_data.decode('utf-8')}")
    
    # Осхранение
    write_binary("binary_data.bin", binary_data)
    print(f"Файл осхранен: data/binary_data.bin")
    
    # данные загруженные
    loaded_data = read_binary("binary_data.bin")
    print(f"Загруженные данные: {loaded_data.decode('utf-8')}")


def demo_delete_file():
    """Демо: удалить файл"""
    print("\n🗑 Удаление файла...")
    
    filename = input("Введите название файла для удаления: ")
    delete_file(filename)


def main():
    """Основная выносливость"""
    while True:
        print_menu()
        choice = input("Обывате вариант: ").strip()
        
        if choice == "1":
            demo_save_user()
        elif choice == "2":
            demo_load_user()
        elif choice == "3":
            demo_save_database()
        elif choice == "4":
            demo_load_database()
        elif choice == "5":
            demo_save_json()
        elif choice == "6":
            demo_list_files()
        elif choice == "7":
            demo_binary_data()
        elif choice == "8":
            demo_delete_file()
        elif choice == "0":
            print("\n🛶 До свидания!")
            break
        else:
            print("✗ Невалидный выбор. Попытайтесь снова.")


if __name__ == "__main__":
    main()
