import sys


def add_sys(arg_list):
    integer_list = [int(x) for x in arg_list]
    return sum(integer_list)


if __name__ == "__main__":
    args = sys.argv
    result = add_sys(args[1:])
    print("addition is", result)
