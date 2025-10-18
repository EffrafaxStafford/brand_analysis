import csv
from tabulate import tabulate
from statistics import mean


def read_csv_file(filenames: list) -> list:
    data = list()
    for filename in set(filenames):
        with open(filename, "r") as file:
            filedata = csv.DictReader(file)
            for row in filedata:
                data.append(row)
    return data


def union_columns(data: list, col1: str = 'brand', col2: str = 'rating') -> list:
    union, column1 = list(), list()
    for row in data:
        sub_row = {k:v if k==col1 else [v] for k,v in row.items() if k in (col1, col2)}
        if sub_row[col1] not in column1:
            column1.append(sub_row[col1])
            union.append(sub_row)
        else:
            union[column1.index(sub_row[col1])][col2] += sub_row[col2]
    return union


def write_csv_file(filename: str, data: list) -> None:
    with open(filename, mode='w') as file:
        columns = list(data[0].keys())
        csv_writer = csv.DictWriter(file, fieldnames=columns)
        csv_writer.writeheader()
        csv_writer.writerows(data)


def calc_avg_values(data: list) -> None:
    for row in data:
        for k, v in row.items():
            if isinstance(v, list):
                row[k] = round(mean(map(float, v)), 2)


def sorted_data(data: list) -> None:
    data.sort(key=lambda x: list(x.values())[1], reverse=True)


def print_result(data: list) -> None:
    print(tabulate(data,
                   headers='keys',
                   tablefmt='grid',
                   showindex=range(1, len(data) + 1)))