from datetime import datetime
import hashlib

def get_log(function):
    def foo(*args, **kwargs):
        date_time = datetime.now()
        name_function = function.__name__
        result = function(*args, **kwargs)
        with open('files_dec.txt', 'w', encoding='utf-8') as file:
            file.write(f'Дата/время: {date_time}\n'
                       f'Имя функции: {name_function}\n'
                       f'Аргументы: {args, kwargs}\n'
                       f'Результат: {result}\n')
        return result
    return foo

@get_log
def get_hash(path: str):
    with open(path) as file:
        for line in file:
            yield hashlib.md5(line.encode()).hexdigest()

if __name__ == '__main__':
    get_hash('wiki.txt')
