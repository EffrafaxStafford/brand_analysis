import csv
from tabulate import tabulate
from statistics import mean


def read_csv_file(filenames: list[str]) -> list[dict]:
    """Возвращает содержимое csv-файлов в виде списка словарей."""
    data = list()
    if filenames is not None:
        for filename in set(filenames):
            try:
                with open(filename, 'r') as file:
                    filedata = csv.DictReader(file)
                    for row in filedata:
                        data.append(row)
            except FileNotFoundError:
                print(f'Файл {filename} не найден')
    return data


def group_by_columns(data: list[dict],
                     col1: str = 'brand',
                     col2: str = 'rating') -> list[dict]:
    """Группирует данные по указанным колонкам."""
    group, column1 = list(), list()
    for row in data:
        sub_row = {k: v if k == col1 else [v]
                   for k, v in row.items() if k in (col1, col2)}
        if sub_row[col1] not in column1:
            column1.append(sub_row[col1])
            group.append(sub_row)
        else:
            group[column1.index(sub_row[col1])][col2] += sub_row[col2]
    return group


def write_csv_file(filename: str, data: list[dict]) -> None:
    """Записывает данные в csv-файл."""
    with open(filename, mode='w') as file:
        if data:
            columns = list(data[0].keys())
            csv_writer = csv.DictWriter(file, fieldnames=columns)
            csv_writer.writeheader()
            csv_writer.writerows(data)


def calc_avg_values(data: list[dict]) -> None:
    """Вычисляет avg-значение для числовых данных.

    Если значения не могут быть преобразованы в числа,
    объединяет их в строку через ' / '.
    """
    for row in data:
        for k, v in row.items():
            if isinstance(v, list):
                try:
                    row[k] = round(mean(map(float, v)), 2)
                except ValueError:
                    row[k] = ' / '.join(v)


def sorted_data(data: list) -> None:
    """Сортирукт данные по убыванию значений во втором столюце."""
    data.sort(key=lambda x: list(x.values())[1], reverse=True)


def print_result(data: list) -> None:
    """Выводит данные в виде таблицы с нумерацией строк."""
    print(tabulate(data,
                   headers='keys',
                   tablefmt='grid',
                   showindex=range(1, len(data) + 1)))
