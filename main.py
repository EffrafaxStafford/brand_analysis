import argparse

from analysis import read_csv_file, union_columns, write_csv_file, calc_avg_values, sorted_data


parser = argparse.ArgumentParser(description="Анализ рейтинга брендов")
parser.add_argument("--files", help="Название файлов", nargs="*")
parser.add_argument("--report", help="Название отчета", default="average-rating")
args, unknown = parser.parse_known_args()


if __name__ == '__main__':
    data = read_csv_file(args.files)
    union = union_columns(data)
    calc_avg_values(union)
    sorted_data(union)
    write_csv_file(args.report, union)
