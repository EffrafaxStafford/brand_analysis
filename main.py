import argparse

from analysis import reader, get_brand_ratings, get_avg_brand_ratings


parser = argparse.ArgumentParser(description="Анализ рейтинга брендов")
parser.add_argument("--files", help="Название файлов", nargs="*")
parser.add_argument("--report", help="Название отчета", default="average-rating")
args, unknown = parser.parse_known_args()


if __name__ == '__main__':
    data = reader(args.files)
    brand_ratings = get_brand_ratings(data)
    avg_brand_ratings = get_avg_brand_ratings(brand_ratings)

