import os
from dotenv import load_dotenv

load_dotenv()

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

