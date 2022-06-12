import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')

API_TOKEN = os.environ.get('API_TOKEN')
API_URL = f'https://api.telegram.org/bot{API_TOKEN}/sendMessage'
API_SETWEBHOOK_URL = f'https://api.telegram.org/bot{API_TOKEN}/setWebhook'

# webhook settings
WEBHOOK_HOST = os.environ.get('WEBHOOK_HOST')
WEBHOOK_PATH = '/webhook'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = 'localhost'
WEBAPP_PORT = 5000

# database settings
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')


def get_dsn():
    try:
        DSN = os.environ.get('DATABASE_URL')
        assert DSN is not None
    except:
        print('using .env file')
        print(f'{DB_HOST=}')
        DSN = f'postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
        print(DSN)

    return DSN

