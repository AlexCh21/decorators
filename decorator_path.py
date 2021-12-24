from datetime import datetime
import requests

file_path = 'files_dec.txt'

def get_log(path):
    def decorator(function):
        def foo(*args, **kwargs):
            date_time = datetime.now()
            name_function = function.__name__
            result = function(*args, **kwargs)
            with open(path, 'w', encoding='utf-8') as file:
                file.write(f'Дата/время: {date_time}\n'
                           f'Имя функции: {name_function}\n'
                           f'Аргументы: {args, kwargs}\n'
                           f'Результат: {result}\n')
            return result
        return foo
    return decorator

@get_log(file_path)
def get_status(*args, **kwargs):
    url = ','.join(args)
    response = requests.get(url=url)
    return response.status_code

if __name__ == '__main__':
    get_status('https://github.com/')
