# Задание №3: Работа с файлами и потоками ввода-вывода

## Описание задания

Это практическое задание целью получение навыков работы с файлами, сериализацией и десериализацией данных на Python.

## Требования

### 1. Изучение методов открытия файла и чтение/запись данных

**Что необходимо сделать:**
- Ознакомиться с методами открытия файлов (режимы `r`, `w`, `a`, `rb`, `wb`)
- Понять разницу между текстовым и двоичным режимом
- Изучить работу с context manager (`with` statement)
- Реализовать функции для чтения и записи текстовых файлов

**Реализовано в:** `file_operations.py`

```python
# Пример использования
from file_operations import write_text, read_text

# Запись текста
write_text("greeting.txt", "Привет, мир!")

# Чтение текста
content = read_text("greeting.txt")
print(content)  # "Привет, мир!"
```

### 2. Создание приложения для работы с двоичными данными

**Что необходимо сделать:**
- Реализовать функции для записи и чтения двоичных данных
- Работать с байтовыми последовательностями
- Использовать модуль `struct` для упаковки/распаковки данных

**Реализовано в:** `file_operations.py` и `examples/binary_data.py`

```python
# Пример использования
from file_operations import write_binary, read_binary

# Запись двоичных данных
data = b'\x48\x65\x6C\x6C\x6F'  # "Hello" в hex
write_binary("data.bin", data)

# Чтение двоичных данных
loaded_data = read_binary("data.bin")
print(loaded_data.decode('utf-8'))  # "Hello"
```

### 3. Сериализация и десериализация объектов

**Что необходимо сделать:**
- Использовать модуль `pickle` для сериализации пользовательских объектов
- Реализовать функции сохранения и загрузки объектов
- Применить альтернативные форматы (JSON)
- Понимать различия между pickle и JSON

**Реализовано в:** `serialization.py`

#### Pickle (двоичная сериализация)

```python
from serialization import PickleSerializer
from models import User

# Создание объекта
user = User(1, "Иван", "ivan@example.com")

# Сериализация (сохранение)
PickleSerializer.serialize(user, "user.pkl")

# Десериализация (загрузка)
loaded_user = PickleSerializer.deserialize("user.pkl")
print(loaded_user)  # User(id=1, name='Иван', email='ivan@example.com')
```

#### JSON (текстовая сериализация)

```python
from serialization import JSONSerializer

# Сохранение словаря
data = {"name": "Мария", "age": 25, "city": "Москва"}
JSONSerializer.serialize(data, "person.json")

# Загрузка
loaded_data = JSONSerializer.deserialize("person.json")
print(loaded_data)  # {'name': 'Мария', 'age': 25, 'city': 'Москва'}
```

## Структура проекта

```
file-io-serialization-task/
├── README.md                    # Основная документация
├── ASSIGNMENT.md               # Описание задания (этот файл)
├── models.py                   # Определение классов данных
├── file_operations.py          # Функции для работы с файлами
├── serialization.py            # Модули сериализации (Pickle, JSON)
├── main.py                     # Интерактивное приложение
├── examples/
│   ├── binary_data.py          # Примеры работы с двоичными данными
│   └── json_alternative.py     # Примеры работы с JSON
├── tests/
│   ├── test_models.py          # Тесты для моделей
│   ├── test_file_ops.py        # Тесты для операций с файлами
│   └── test_serialization.py   # Тесты для сериализации
└── data/                       # Директория для хранения файлов
```

## Ключевые концепции

### 1. Режимы открытия файлов

| Режим | Описание | Тип |
|-------|---------|------|
| `r` | Чтение | Текст |
| `w` | Запись (перезапись) | Текст |
| `a` | Запись в конец | Текст |
| `rb` | Чтение | Двоичный |
| `wb` | Запись (перезапись) | Двоичный |
| `ab` | Запись в конец | Двоичный |

### 2. Context Manager (with statement)

```python
# ✓ Правильно - файл автоматически закроется
with open('file.txt', 'r') as f:
    content = f.read()

# ✗ Неправильно - файл может остаться открытым
f = open('file.txt', 'r')
content = f.read()
# f.close() - может быть забыто
```

### 3. Pickle vs JSON

| Аспект | Pickle | JSON |
|--------|--------|------|
| Формат | Двоичный | Текстовый |
| Читаемость | Нечитаемо | Читаемо |
| Типы | Поддерживает все Python типы | Только базовые типы |
| Безопасность | Небезопасна (может выполнить код) | Безопасна |
| Совместимость | Только Python | Универсальна |

### 4. Struct - упаковка данных

```python
import struct

# Упаковка данных
data = struct.pack('I20s', 42, b'John')  # int + 20-байтовая строка

# Распаковка данных
user_id, user_name = struct.unpack('I20s', data)
```

## Классы и объекты

### User
```python
user = User(user_id=1, name="Иван", email="ivan@example.com")
```

### Product
```python
product = Product(product_id=1, name="Ноутбук", price=50000.00, stock=5)
```

### Order
```python
order = Order(order_id=1, user=user, products=[product], total=50000.00)
order.complete()  # Изменить статус
order.cancel()    # Отменить заказ
```

### Database
```python
db = Database()
db.add_user(user)
db.add_product(product)
db.add_order(order)
found_user = db.get_user(1)
```

## Примеры использования

### Пример 1: Простое сохранение и загрузка текста

```bash
python main.py
# Выбрать опцию 1 - сохранить User
# Выбрать опцию 2 - загрузить User
```

### Пример 2: Работа с двоичными данными

```bash
python examples/binary_data.py
```

### Пример 3: Работа с JSON

```bash
python examples/json_alternative.py
```

## Тестирование

### Запуск всех тестов

```bash
pytest tests/ -v
```

### Запуск конкретного теста

```bash
pytest tests/test_models.py::TestUser::test_user_creation -v
```

### Запуск с покрытием кода

```bash
pytest tests/ --cov=. --cov-report=html
```

## Ошибки и их решения

### Проблема: FileNotFoundError при загрузке

**Решение:** Убедитесь, что файл существует. Используйте функцию `file_exists()` перед чтением.

```python
if file_exists("user.pkl"):
    user = PickleSerializer.deserialize("user.pkl")
```

### Проблема: UnicodeDecodeError при чтении двоичных данных

**Решение:** Используйте двоичный режим (`rb`) и декодируйте при необходимости.

```python
# ✗ Неправильно
content = read_text("data.bin")  # Ошибка!

# ✓ Правильно
data = read_binary("data.bin")
content = data.decode('utf-8')
```

### Проблема: Pickle несовместим между версиями Python

**Решение:** Используйте JSON для совместимости между версиями.

```python
# Вместо Pickle
JSONSerializer.serialize(data, "file.json")
```

## Практические задачи

1. **Создать приложение для управления адресной книгой**
   - Сохранять контакты в файл (pickle или JSON)
   - Загружать контакты из файла
   - Добавлять, удалять, обновлять контакты

2. **Реализовать систему логирования**
   - Писать логи в файл
   - Читать и анализировать логи
   - Ротация файлов логов

3. **Создать конвертер формата данных**
   - Преобразовать pickle → JSON
   - Преобразовать JSON → pickle
   - Поддержка CSV формата

## Полезные ссылки

- [Python файловые операции](https://docs.python.org/3/tutorial/inputoutput.html)
- [Модуль pickle](https://docs.python.org/3/library/pickle.html)
- [Модуль json](https://docs.python.org/3/library/json.html)
- [Модуль struct](https://docs.python.org/3/library/struct.html)
- [Context managers](https://docs.python.org/3/library/stdtypes.html#context-manager-types)

## Заключение

Это задание охватывает основные аспекты работы с файлами и сериализацией данных в Python. Вы научитесь:

✓ Открывать и закрывать файлы правильно
✓ Работать с текстовыми и двоичными данными
✓ Сохранять и загружать сложные объекты
✓ Выбирать подходящий формат сериализации
✓ Обрабатывать ошибки при работе с файлами
✓ Писать тесты для файловых операций
