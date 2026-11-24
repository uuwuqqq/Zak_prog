# Zak_prog
Вот краткий текстовый словарь-шпаргалка для твоего репозитория (в формате Markdown), который удобно читать и использовать как справочник:

### Ввод и преобразование типов

* **`input()`** — выводит приглашение в терминал и считывает введенный пользователем текст (всегда возвращает строку).
* **`int()`** — преобразует значение в целое число.
* **`float()`** — преобразует значение в число с плавающей точкой (десятичное).
* **`str()`** — преобразует значение в текстовую строку.

### Математические операторы

* **`//` (Целочисленное деление)** — делит число нацело с округлением результата вниз до ближайшего целого.
* **`%` (Остаток от деления)** — возвращает остаток от деления одного числа на другое (часто используется для проверки четности или выделения младших разрядов).

### Форматирование вывода (f-строки)

* **`:.3f`** — округляет число с плавающей точкой до указанного количества знаков после запятой (например, до 3 знаков).
* **`:02`** — задает минимальную ширину поля и заполняет пустое пространство слева нулями (например, для вывода времени `05`).

### Работа со строками и срезами

* **`len()`** — возвращает количество элементов (или символов) в объекте.
* **`[0]`** — обращение к первому элементу или символу по индексу.
* **`[-1]`** — обращение к самому последнему элементу или символу (индексация с конца).
* **`.upper()`** — метод строк, переводящий весь текст в верхний регистр (большие буквы).
* **`[::-1]`** — срез с шагом `-1`, переворачивающий строку или список задом наперед (реверс).
* **`.count()`** — метод, подсчитывающий количество вхождений определенного символа или подстроки.
Вот список ключевых встроенных функций, методов и конструкций из презентации и практики, которые важно знать для тестов и занятий:

* **`range(start, stop, step)`**
* *Значение:* Создает последовательность целых чисел от `start` до `stop` (не включая правую границу) с заданным шагом `step`.
* *Применение:* Используется в циклах `for` для повторения определенное количество раз или перебора числовых диапазонов (например, годы от 1890 до 2030: `range(1890, 2031)`).


* **`enumerate(iterable, start=0)`**
* *Значение:* Принимает коллекцию и возвращает пары из индекса (порядкового номера) и самого элемента.
* *Применение:* Идеально подходит для циклов `for`, когда помимо самого элемента (например, диаметра детали или имени) нужен его порядковый номер на экране.


* **`zip(col1, col2, ...)`**
* *Значение:* Объединяет несколько параллельных коллекций в одну последовательность кортежей из пар соответствующих элементов.
* *Применение:* Используется для одновременного обхода двух и более списков (например, имен и оценок) в одном цикле `for`.


* **`list.append(item)`**
* *Значение:* Метод списка, который добавляет новый элемент `item` в самый конец существующего списка.
* *Применение:* Накопление данных внутри циклов (например, добавление подходящих годов или значений в пустой список).


* **`len(iterable)`**
* *Значение:* Возвращает общее количество элементов в коллекции (длину строки, списка, словаря и т.д.).
* *Применение:* Подсчет общего числа элементов, вычисление процента брака или долей.


* **`str.join(iterable)`**
* *Значение:* Объединяет элементы коллекции строк в одну общую строку, разделяя их символом, на котором вызван метод (например, `" ".join(...)` объединяет через пробел).
* *Применение:* Красивый вывод списков на экран (например, вывод по 10 годов в ряд).


* **Тернарный условный оператор (`x if condition else y`)**
* *Значение:* Позволяет записать условие выбора одного из двух значений в одну строку.
* *Применение:* Короткое присваивание переменной значения в зависимости от выполнения условия (например, `"sude" if number % 2 == 0 else "liche"`).


* **List Comprehension (`[expression for item in iterable if condition]`)**
* *Значение:* Компактный генератор списков, позволяющий в одну строчку создать и профильтровать новый список.
* *Применение:* Быстрое создание списков без громоздких циклов с `append()` (например, отбор положительных квадратов чисел).

Проблема была в том, что текст вставился без правильной Markdown-разметки (таблицы слиплись, а у блоков кода не было тройных кавычек ```python). Плюс я убрал лишние технические ссылки вроде ``, чтобы они не мешали в чистом файле.

Ниже — готовый блок с корректной разметкой. Просто нажми кнопку «Копировать» в правом верхнем углу этого блока и вставь в свой README.md:

# Работа с файлами, пути и сериализация (Python)

## 1. Основные понятия
| Термин | Смысл |
| :--- | :--- |
| `cesta` | Где лежит файл (`data/mereni.txt`) |
| `soubor` | Последовательность байтов на диске |
| `souborový objekt` | Результат `open()`, поток данных |
| `kódování` | Правила преобразования `str ↔ bytes` |
| `formát` | Договорённость о содержимом (разделители, порядок, кодировка) |

## 2. Режимы открытия файлов (`open`)
| Режим | Смысл | Если файла нет |
| :--- | :--- | :--- |
| `"r"` | Чтение | Ошибка `FileNotFoundError` |
| `"w"` | Запись с начала (стирает файл при открытии) | Создаётся |
| `"a"` | Дописывание в конец | Создаётся |
| `"x"` | Создание нового (защита от перезаписи) | Создаётся |
| `"b"` | Байты (`"rb"`, `"wb"`) | Зависит от комбинации |

## 3. Шаблоны кода для текстовых файлов

### Запись и дописывание
```python
# Запись (перезаписывает файл)
with open("report.txt", "w", encoding="utf-8") as file:
    file.write("text\n")

# Дописывание в конец
with open("journal.txt", "a", encoding="utf-8") as file:
    file.write(f"{timestamp} | {message}\n")


Построчное чтение и валидация

with open("measurements.txt", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        cleaned = line.strip()
        if not cleaned:
            continue
        
        time_text, value_text = cleaned.split(";", maxsplit=1)
        try:
            temperature = float(value_text)
        except ValueError:
            invalid_lines.append(line_number)
            continue
        measurements.append((time_text, temperature))


⚬ Методы чтения: file.read() (весь файл строкой), file.readline() (одна строка), file.readlines() (список всех строк).

Обработка отсутствующего файла

try:
    with open("measurements.txt", encoding="utf-8") as file:
        first_line = file.readline()
except FileNotFoundError:
    print("Input file does not exist.")
else:
    print(first_line.rstrip("\n"))


Очистка строк

Метод	Что делает
rstrip("\n")	Убирает только перевод строки в конце
strip()	Убирает пробелы, табуляции и переводы строк с обоих концов

4. Текст, байты и кодировка

⚬ Правило: encoding="utf-8" всегда указывать явно.

text = "caf\u00e9"
data = text.encode("utf-8")   # str -> bytes
text2 = data.decode("utf-8")  # bytes -> str

len(text)   # 4 символа
len(data)   # 5 байтов


Бинарные числа

Читателю нужно знать: число байтов, порядок байтов и знаковость.

data = number.to_bytes(2, byteorder="little", signed=False)
with open("number.bin", "wb") as file:
    file.write(data)

restored = int.from_bytes(data, byteorder="little", signed=False)


5. Исключения

Исключение	Причина
FileNotFoundError	Путь не существует
PermissionError	Нет прав доступа
IsADirectoryError	Открыта папка вместо файла
UnicodeDecodeError	Байты не подходят под кодировку
ValueError	Неверный формат содержимого

⚬ Правила: блок try минимальный, ловим конкретное исключение, не используем широкий except Exception без нужды, не игнорируем ошибки молча.

6. Работа с путями (pathlib)

Относительный путь всегда считается от текущей рабочей папки (Path.cwd()), а не от папки скрипта.

from pathlib import Path

p = Path("outputs") / "report.txt"            # сборка пути оператором /
p.parent.mkdir(parents=True, exist_ok=True)   # создать родительскую папку
p.write_text("Done\n", encoding="utf-8")      # быстрая запись текста

p.name        # имя файла с расширением ('report.txt')
p.stem        # имя без расширения ('report')
p.suffix      # расширение ('.txt' — удобно использовать .lower())
p.exists()    # существует ли путь?
p.is_file()   # это файл?
p.resolve()   # полный (абсолютный) путь
Path.cwd()    # текущая рабочая папка

# Обход файлов
Path("photos").iterdir()       # всё содержимое одной папки
Path("photos").glob("*.txt")   # выбор по шаблону в папке
Path("photos").rglob("*")      # рекурсивный обход с подпапками


7. JSON (import json)

Сохраняет базовые типы (dict, list, str, int, float, bool, None), но не поддерживает set, tuple (превращается в list), даты и пользовательские классы.

⚬ json.dump(data, file, ensure_ascii=False, indent=2) — записать в открытый текстовый файл (ensure_ascii=False оставляет читаемой кириллицу и диакритику, indent=2 делает отступы).
⚬ json.load(file) — прочитать данные из файла в новый объект.
⚬ json.dumps(data) — преобразовать объект в строку str (s = string).
⚬ json.loads(text) — преобразовать строку str в объект.

import json

try:
    with open("books.json", "r", encoding="utf-8") as file:
        books = json.load(file)
except FileNotFoundError:
    print("Файл не найден")
except json.JSONDecodeError as error:
    print("Некорректный JSON:", error)


(После загрузки всегда проверяем структуру, обязательные ключи и типы данных вручную.)

8. CSV (import csv)

Подходит для плоских таблиц. Все прочитанные значения возвращаются как строки str — числа и булевы значения приводим вручную. Всегда открываем файл с newline="".

Запись и чтение

import csv

# Запись
fields = ["title", "author", "year", "available"]
with open("books.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()      # записывает строку заголовков
    writer.writerows(books)   # записывает список словарей

# Чтение
with open("books.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    loaded_books = list(reader)  # или построчно: for row in reader:


Безопасное приведение булевых значений

Не используем bool("False"), так как любая непустая строка даёт True.

def parse_bool(text: str) -> bool:
    normalized = text.strip().lower()
    if normalized == "true":
        return True
    if normalized == "false":
        return False
    raise ValueError("Expected true or false")


9. Pickle (import pickle)

Бинарный формат только для Python (режимы "wb" и "rb").

⚬ Критично: никогда не загружаем файлы из недоверенных источников — pickle.load() может выполнить произвольный вредоносный код.

import pickle

with open("books.pkl", "wb") as file:
    pickle.dump(books, file)

with open("books.pkl", "rb") as file:
    loaded_books = pickle.load(file)


10. Архитектура и выбор формата

⚬ Пайплайн: load_data() → summarize() → write_report(). Одна функция — одна ответственность; вычисления не зависят от input()/print(); валидация до использования значения.
⚬ Плоская таблица / Excel → CSV
⚬ Вложенная структура / обмен между языками → JSON
⚬ Большие объёмы построчно → CSV (DictReader) или JSON Lines
⚬ Свой временный кэш только для Python → pickle




# Сериализация и работа с файлами (JSON, CSV, Pickle)

## 1. JSON (`import json`)
Сохраняет базовые типы (`dict`, `list`, `str`, `int`, `float`, `bool`, `None`)[span_0](start_span)[span_0](end_span), но **не поддерживает `set`, `tuple` (превращается в `list`), даты и пользовательские классы**[span_1](start_span)[span_1](end_span)[span_2](start_span)[span_2](end_span)[span_3](start_span)[span_3](end_span).

### Основные функции
* `json.dump(data, file, ensure_ascii=False, indent=2)` — записать объект в открытый текстовый файл[span_4](start_span)[span_4](end_span).
  * `ensure_ascii=False` — сохраняет кириллицу и диакритику (чешские символы) в читаемом виде[span_5](start_span)[span_5](end_span).
  * `indent=2` — добавляет отступы для читаемости[span_6](start_span)[span_6](end_span).
* `json.load(file)` — прочитать данные из открытого файла в новый объект Python[span_7](start_span)[span_7](end_span).
* `json.dumps(data)` — преобразовать объект в строку `str` (буква `s` = string)[span_8](start_span)[span_8](end_span).
* `json.loads(text)` — преобразовать строку `str` в объект Python[span_9](start_span)[span_9](end_span).

### Пример с обработкой ошибок
```python
import json

try:
    with open("books.json", "r", encoding="utf-8") as file:
        books = json.load(file)
except FileNotFoundError:
    print("Файл не найден")
except json.JSONDecodeError as error:
    print("Некорректный JSON:", error)


(После загрузки всегда проверяем структуру, обязательные ключи и типы данных вручную.)

2. CSV (import csv)

Подходит для плоских таблиц. Все прочитанные значения возвращаются как строки str — числа и булевы значения нужно приводить вручную. Всегда открываем файл с newline="".

Запись через DictWriter

import csv

fields = ["title", "author", "year", "available"]
with open("books.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()      # записывает строку заголовков[span_18](start_span)[span_18](end_span)
    writer.writerows(books)   # записывает список словарей[span_19](start_span)[span_19](end_span)


Чтение через DictReader

import csv

with open("books.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    loaded_books = list(reader)  # или итерируемся построчно: for row in reader[span_20](start_span)[span_20](end_span)


Безопасное приведение типов из CSV

Не используем bool("False"), так как любая непустая строка даёт True.

def parse_bool(text: str) -> bool:
    normalized = text.strip().lower()
    if normalized == "true":
        return True
    if normalized == "false":
        return False
    raise ValueError("Expected true or false")


3. Pickle (import pickle)

Бинарный формат только для Python (режимы "wb" и "rb").

⚬ Критично: никогда не загружаем файлы из недоверенных источников — pickle.load() может выполнить произвольный вредоносный код.

import pickle

with open("books.pkl", "wb") as file:
    pickle.dump(books, file)

with open("books.pkl", "rb") as file:
    loaded_books = pickle.load(file)


Быстрая памятка

⚬ Плоская таблица / Excel → CSV
⚬ Вложенная структура / обмен между языками → JSON
⚬ Большие объёмы построчно → CSV (DictReader) или JSON Lines
⚬ Свой временный кэш только для Python → pickle

