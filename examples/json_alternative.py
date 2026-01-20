"""
Пример работы с JSON (pickle альтернатива)
"""
import sys
sys.path.insert(0, '..')

from serialization import JSONSerializer
from models import User, Product, Order


def example_dict_to_json():
    """Пример 1: Осхранение словаря в JSON"""
    print("📌 Пример 1: Осхранение словаря")
    print("-" * 50)
    
    person = {
        "им": "Александр",
        "возраст": 28,
        "город": "Чита",
        "профессия": "Программист"
    }
    
    print(f"Осхраняемые данные:")
    for key, value in person.items():
        print(f"  {key}: {value}")
    
    JSONSerializer.serialize(person, "person.json")


def example_list_of_dicts():
    """Пример 2: Осхранение списка совюностей"""
    print("\n📌 Пример 2: Осхранение листа совюностей")
    print("-" * 50)
    
    students = [
        {
            "ид": 1,
            "им": "Иван",
            "группа": "101",
            "оценки": [4, 5, 3, 4, 5]
        },
        {
            "ид": 2,
            "им": "Мария",
            "группа": "102",
            "оценки": [5, 5, 5, 4, 5]
        },
        {
            "ид": 3,
            "им": "Петр",
            "группа": "101",
            "оценки": [3, 4, 3, 3, 4]
        }
    ]
    
    print(f"Осхраняемые студенты: {len(students)}")
    for student in students:
        avg_score = sum(student["оценки"]) / len(student["оценки"])
        print(f"  {student['им']} - группа {student['группа']}, средняя: {avg_score:.1f}")
    
    JSONSerializer.serialize(students, "students.json")


def example_nested_json():
    """Пример 3: Неоличные JSON данные"""
    print("\n📌 Пример 3: Вложенные JSON данные")
    print("-" * 50)
    
    company = {
        "название": "ООО МегаКорп",
        "город": "Курск",
        "офисы": {
            "разработка": {
                "ответственный": "Владимир",
                "сотрудники": 15
            },
            "маркетинг": {
                "ответственный": "Олег",
                "сотрудники": 8
            }
        }
    }
    
    print(f"Осхраняемая компания: {company['название']}")
    print(f"Офисы:")
    for dept, info in company["офисы"].items():
        print(f"  {dept}:")
        print(f"    Ответственный: {info['ответственный']}")
        print(f"    Сотрудников: {info['сотрудники']}")
    
    JSONSerializer.serialize(company, "company.json")


def example_config_file():
    """Пример 4: Настройки приложения"""
    print("\n📌 Пример 4: Настройки приложения")
    print("-" * 50)
    
    config = {
        "app_name": "FileIOApp",
        "version": "1.0.0",
        "debug": True,
        "database": {
            "host": "localhost",
            "port": 5432,
            "username": "admin",
            "password": "secret123"
        },
        "features": ["serialization", "binary_io", "json_support"],
        "logging": {
            "level": "INFO",
            "file": "app.log",
            "max_size": 1000000
        }
    }
    
    print("Настройки:")
    print(f"  Приложение: {config['app_name']} v{config['version']}")
    print(f"  Отладка: {config['debug']}")
    print(f"  База данных: {config['database']['host']}:{config['database']['port']}")
    print(f"  Функции: {', '.join(config['features'])}")
    
    JSONSerializer.serialize(config, "config.json")


def main():
    print("\n" + "="*50)
    print("Примеры работы с JSON")
    print("="*50)
    
    example_dict_to_json()
    example_list_of_dicts()
    example_nested_json()
    example_config_file()
    
    print("\n" + "="*50)
    print("✓ Все примеры выполнены!")
    print("="*50)
    print("\nОткрытые JSON файлы: data/*.json")


if __name__ == "__main__":
    main()
