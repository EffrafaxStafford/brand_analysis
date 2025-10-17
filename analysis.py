import csv
from enum import Enum


class Column(Enum):  
    NAME = 0
    BRAND = 1
    PRICE = 2
    RATING = 3


def reader(filenames: list) -> list:
    data = list()
    for filename in filenames:
        with open(filename, "r") as file:
            filedata = csv.reader(file)
            for row in filedata:
               if row not in data:
                  data.append(row)
    return data[1:]


def get_brand_ratings(data: list) -> dict:
    brand_ratings = dict()
    for record in data:
       brand = record[Column.BRAND.value]
       rating = float(record[Column.RATING.value])
       brand_ratings[brand] = brand_ratings.get(brand, []) + [rating]
    return brand_ratings


def get_avg_brand_ratings(brand_ratings: dict) -> dict:
    avg_brand_ratings = dict()
    for brand, ratings in brand_ratings.items():
        avg_brand_ratings[brand] = round(sum(ratings) / len(ratings), 2)
    return avg_brand_ratings

