def count_sum(*args):
    return sum(args)


def count_smth(*args):
    return args, args


if __name__ == '__main__':
    count_sum(1, 2, 10, 8)
    count_smth()


def count_smth():
    import time
    while True:
        print('Periodic task')
        time.sleep(60)