import datetime

path_f = r'C:\Users\Анастасия\PycharmProjects\netology\venv\logger.txt'

def path_file(path):
    def logger (function):

            def writer(*args, **kwargs):
                function(*args, **kwargs)
                with open(path, 'w', encoding='utf-8') as log:
                        log.write(f'название функции:{function.__name__}\n')
                        log.write(f'время вызова функции:{datetime.datetime.now()}\n')
                        log.write(f'аргументы функции:{args},{kwargs}\n')
                        result = function(*args, **kwargs)
                        log.write(f'результат функции:{result}')
                        return result

            return writer
    return logger





@path_file(path_f)
def foo(a, b, c):
    print ('ab')
    return a+b+c
foo(1, 2, 3)