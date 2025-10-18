import argparse

from analysis import (read_csv_file, group_by_columns,
                      write_csv_file, calc_avg_values,
                      sorted_data, print_result)


def main(args: argparse.Namespace) -> None:
    data = read_csv_file(args.files)
    group_data = group_by_columns(data, *args.columns)
    calc_avg_values(group_data)
    sorted_data(group_data)
    write_csv_file(args.report, group_data)
    print_result(group_data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Анализ рейтинга брендов')
    parser.add_argument('--files', help='Название файлов', nargs='*')
    parser.add_argument('--report', help='Название отчета',
                        default='average-rating')
    parser.add_argument('--columns', help='Названия столбцов для отчета',
                        nargs=2, default=['brand', 'rating'])
    args, unknown = parser.parse_known_args()
    main(args)
