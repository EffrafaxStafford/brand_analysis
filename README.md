# brand_analysis

## Описание

Инструмент для анализа и агрегации данных из CSV-файлов. Программа группирует данные по 2-м столбцам, вычисляет средние значения (для числовых данных) и генерирует отчеты в виде таблицы (выводится на консоль) и csv-файлов.

## Установка

1. Клонируйте репозиторий и перейдите в папку проекта:

    ```bash
    git clone https://github.com/EffrafaxStafford/brand_analysis.git
    cd brand_analysis
    ```

2. Создайте виртуальное окружение, активируйте его и установите зависимости:

    ```bash
    python -m venv venv
    source venv\scripts\activate
    pip install -r requirements.txt
    ```

## Использование

Запустите программу с параметрами командной строки:

```bash
python main.py \
    --files file1.csv file2.csv \
    --report brand-analysis \
    --columns brand score
```

### Параметры командной строки

 --files: Список csv-файлов для анализа (обязательный)

 --report: Имя выходного файла (по умолчанию: "average-rating")

 --columns: Названия колонок для группировки (по умолчанию: ["brand", "rating"])

## Примеры запуска

Входные данные для запуска лежат в папке csv_data.

**1. Генерация отчета о среднем рейтинге по брендам из двух файлов.**

```bash
python main.py --files csv_data/products1.csv csv_data/products2.csv
```

Содержимое отчета `average-rating`:

```
brand,rating
apple,4.55
samsung,4.53
xiaomi,4.37

```

Вывод в терминал:

```bash
+----+---------+----------+
|    | brand   |   rating |
+====+=========+==========+
|  1 | apple   |     4.55 |
+----+---------+----------+
|  2 | samsung |     4.53 |
+----+---------+----------+
|  3 | xiaomi  |     4.37 |
+----+---------+----------+
```

**2. Генерация отчета о средней цене по брендам из двух файлов.**


```bash
python main.py \
    --files csv_data/products1.csv csv_data/products2.csv \
    --report average-price \
    --columns brand price
```

Содержимое отчета `average-price`:
```
brand,price
samsung,849.0
apple,706.5
xiaomi,215.67

```

Вывод в терминал:
```bash
+----+---------+---------+
|    | brand   |   price |
+====+=========+=========+
|  1 | samsung |  849    |
+----+---------+---------+
|  2 | apple   |  706.5  |
+----+---------+---------+
|  3 | xiaomi  |  215.67 |
+----+---------+---------+
```

**3. Генерация отчета о наименовании моделей по брендам из двух файлов.**


```bash
python main.py \
    --files csv_data/products1.csv csv_data/products2.csv \
    --report brand-analysis \
    --columns brand name
```

Содержимое отчета `brand-analysis`:
```
name,brand
poco x5 pro / redmi 10c / redmi note 12,xiaomi
galaxy z flip 5 / galaxy s23 ultra / galaxy a54,samsung
iphone se / iphone 13 mini / iphone 15 pro / iphone 14,apple

```

Вывод в терминал:
```bash
+----+--------------------------------------------------------+---------+
|    | name                                                   | brand   |
+====+========================================================+=========+
|  1 | poco x5 pro / redmi 10c / redmi note 12                | xiaomi  |
+----+--------------------------------------------------------+---------+
|  2 | galaxy z flip 5 / galaxy s23 ultra / galaxy a54        | samsung |
+----+--------------------------------------------------------+---------+
|  3 | iphone se / iphone 13 mini / iphone 15 pro / iphone 14 | apple   |
+----+--------------------------------------------------------+---------+
```

## Тестирование

Для запуска тестов запустите `pytest`. Для просмотра покрытия добавьте параметр `--cov=.`:

    ```bash
    pytest --cov=.
    ```
