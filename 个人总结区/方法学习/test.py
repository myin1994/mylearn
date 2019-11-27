import traceback
import sys


def traceback_test():
    try:
        # raise SyntaxError('traceback_test')
        print(1/0)
    except :
        a,b,exception = sys.exc_info()
        traceback.print_tb(exception)


if __name__ == '__main__':
    traceback_test()