from argparse import Namespace

from main import main


default_report = 'average-rating'
none_args = Namespace(files=None, report=default_report)
incorrect_args_1 = Namespace(
    files=['file_does_not_exist'], report=default_report)
incorrect_args_2 = Namespace(
    files=['file_does_not_exist', 'csv_data/products1.csv'],
    report=default_report)
miss_args = Namespace(
    files=['csv_data/products1.csv'],
    report=default_report,
    miss_arg1='miss',
    miss_arg2=[1, 2])
correct_args_1 = Namespace(
    files=['csv_data/products1.csv'],
    report=default_report)
correct_args_2 = Namespace(
    files=['csv_data/products1.csv', 'csv_data/products2.csv'],
    report=default_report)


def test_none_args():
    main(none_args)
    test_file = 'test_data/empty_file'
    with open(test_file) as file1, open(default_report) as file2:
        assert file1.read() == file2.read()


def test_incorrect_args_1():
    main(incorrect_args_1)
    test_file = 'test_data/empty_file'
    with open(test_file) as file1, open(default_report) as file2:
        assert file1.read() == file2.read()


def test_incorrect_args_2():
    main(incorrect_args_2)
    test_file = 'test_data/average-rating-products1'
    with open(test_file) as file1, open(default_report) as file2:
        assert file1.read() == file2.read()


def test_miss_args():
    main(miss_args)
    test_file = 'test_data/average-rating-products1'
    with open(test_file) as file1, open(default_report) as file2:
        assert file1.read() == file2.read()


def test_correct_args_1():
    main(correct_args_1)
    test_file = 'test_data/average-rating-products1'
    with open(test_file) as file1, open(default_report) as file2:
        assert file1.read() == file2.read()


def test_correct_args_2():
    main(correct_args_2)
    test_file = 'test_data/average-rating-products1-products2'
    with open(test_file) as file1, open(default_report) as file2:
        assert file1.read() == file2.read()