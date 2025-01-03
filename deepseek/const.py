import os

DEEPSEEK_API_KEY = os.environ.get('DEEPSEEK_API_KEY', None)

DEFAULT_TEMP = 1.0
TEMPERATURE = {
    'Coding_Math': 0,
    'Data_Cleaning_Analysis':	1.0,
    'General_Conversation':	1.3,
    'Translation':	1.3,
    'Creative_Writing':	1.5
}

API_USER_BAL = "https://api.deepseek.com/user/balance"
API_CHAT_COM = "https://api.deepseek.com/chat/completions"
API_CHAT_FIM = "https://api.deepseek.com/beta/completions"
API_CHAT_MOD = "https://api.deepseek.com/models"


DEFAULT_SYS_PROM = "You are a helpful assistant"
DEFAULT_USR_PROM = "Hi"
