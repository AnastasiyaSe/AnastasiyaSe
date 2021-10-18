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



cook_book = {}

lines = 0
with open(r'C:\Users\Анастасия\PycharmProjects\netology\rec.txt') as f:
    for line in f:
        lines = lines + 1


with open(r'C:\Users\Анастасия\PycharmProjects\netology\rec.txt') as f:
    for i in range(lines):
        dish_name = f.readline().strip()
        count = f.readline().strip()
        if count != '':
            count = int(count)
        else:
            break
        ing_list = list()
        for _ in range(count):
                ingr = f.readline().strip()
                splited = ingr.split('|')
                ing_dict = {}

                ing_dict['ingredient_name'] = splited[0]
                ing_dict['quantity'] = splited[1]
                ing_dict['measure'] = splited[2]
                ing_list.append(ing_dict)
        f.readline()
        cook_book[dish_name] = ing_list




@path_file(path_f)
def get_shop_list_by_dishes(dishes, person_count):
    count_food = {}
    for i in range(len(dishes)):
        ing = {}
        ing['quantity'] = int(cook_book[dishes[i]][0]['quantity'])*person_count
        ing['measure'] = cook_book[dishes[i]][0]['measure']
        count_food[cook_book[dishes[i]][0]['ingredient_name']] = ing

        print(count_food)

get_shop_list_by_dishes(['omelet','omelet'], 2)

