import csv


def reader(filenames: list) -> list:
    data = list()
    for filename in filenames:
        with open(filename, "r") as file:
            filedata = csv.reader(file)
            for row in filedata:
               if row not in data:
                  data.append(row)
    return data[1:]
