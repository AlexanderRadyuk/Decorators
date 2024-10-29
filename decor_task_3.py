import datetime


def logger(old_function):
    def new_function(*args, **kwargs):
        moment = str(datetime.datetime.now().strftime('%m/%d/%y %H:%M:%S'))
        # moment = str(datetime.datetime.now())
        func_name = old_function.__name__
        result = old_function(*args, **kwargs)
        with open('task3.log', 'a', encoding='utf-8') as f:
            f.write(f'{func_name}\t{result}\t{moment} func inputs{args} and{kwargs}\n')
        return result
    return new_function


@logger
def flat_generator(list_to_flatten):
    cursor_main: int = 0
    cursor_aux: int = 0
    for _ in list_to_flatten:
        cursor_main += 1
        if isinstance(list_to_flatten[cursor_main - 1], list):
            while cursor_aux < len(list_to_flatten[cursor_main - 1]):
                cursor_aux += 1
                yield list_to_flatten[cursor_main - 1][cursor_aux - 1]
            else:
                cursor_aux = 0
            continue
        else:
            yield list_to_flatten[cursor_main - 1]


list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

print(list(flat_generator(list_of_lists_1)))

