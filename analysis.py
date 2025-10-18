import csv
from enum import Enum


def read_csv_file(filenames: list) -> list:
    data = list()
    for filename in filenames:
        with open(filename, "r") as file:
            filedata = csv.DictReader(file)
            for row in filedata:
               if row not in data:
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
            union[column1.index(sub_row[col1])][col2].extend(sub_row[col2])
    return union


def write_csv_file(filename: str, data: list) -> None:
    with open(filename, mode='w') as file:
        fieldnames = list(data[0].keys())
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(data)


# def get_avg_brand_ratings(brand_ratings: dict) -> dict:
#     avg_brand_ratings = dict()
#     for brand, ratings in brand_ratings.items():
#         avg_brand_ratings[brand] = round(sum(ratings) / len(ratings), 2)
#     return avg_brand_ratings

