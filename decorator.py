from datetime import datetime
import requests

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
def get_status(*args, **kwargs):
    url = ','.join(args)
    response = requests.get(url=url)
    return response.status_code

if __name__ == '__main__':
    get_status('https://github.com/')
