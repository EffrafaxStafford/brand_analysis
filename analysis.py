import csv
from enum import Enum


def reader(filenames: list) -> list:
    data = list()
    for filename in filenames:
        with open(filename, "r") as file:
            filedata = csv.DictReader(file)
            for row in filedata:
               if row not in data:
                  data.append(row)
    print(*data, sep='\n')
    return data


def union_columns(data: list, col1='brand', col2='rating') -> list:
    union, column1 = list(), list()
    for row in data:
        sub_row = {k:v if k==col1 else [v] for k,v in row.items() if k in (col1, col2)}
        if sub_row[col1] not in column1:
            column1.append(sub_row[col1])
            union.append(sub_row)
        else:
            union[column1.index(sub_row[col1])][col2].extend(sub_row[col2])
    return union


# def get_brand_ratings(data: list) -> dict:
#     brand_ratings = dict()
#     for record in data:
#        brand = record[Column.BRAND.value]
#        rating = float(record[Column.RATING.value])
#        brand_ratings[brand] = brand_ratings.get(brand, []) + [rating]
#     return brand_ratings


# def get_avg_brand_ratings(brand_ratings: dict) -> dict:
#     avg_brand_ratings = dict()
#     for brand, ratings in brand_ratings.items():
#         avg_brand_ratings[brand] = round(sum(ratings) / len(ratings), 2)
#     return avg_brand_ratings

