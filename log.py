import datetime

def log_cash (mod):
     with open('log.txt', 'a', encoding='utf-8') as file:
         file.write(f'{mod}. Время запроса: {str(datetime.now)} /n')