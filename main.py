def count_sum(*args):
    return sum(args)


def count_smth(*args):
    return args


if __name__ == '__main__':
    count_sum(1, 2, 3, 8)
    count_smth()