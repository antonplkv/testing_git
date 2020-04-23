def count_sum(*args):
    return sum(args)


def count_smth(*args):
    return args, args


if __name__ == '__main__':
    count_sum(1, 2, 10, 8)
    count_smth()