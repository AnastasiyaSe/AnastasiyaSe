import datetime
from contextlib import redirect_stdout


def logger (function):
    def writer(*args, **kwargs):

        function(*args, **kwargs)
        with open('logger.txt', 'w', encoding='utf-8') as log:
            log.write(f'название функции:{function.__name__}\n')
            log.write(f'время вызова функции:{datetime.datetime.now()}\n')
            log.write(f'аргументы функции:{args},{kwargs}\n')
            result = function(*args, **kwargs)
            log.write(f'результат функции:{result}')
            return result
    return writer





@logger
def foo(a, b, c):
    return a+b+c


foo(1,2,3)