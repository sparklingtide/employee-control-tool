# Провайдеры

## Инициализация Telegram

Для работы с провайдером Telegram необходимо:
- [Создать API id и API hash](https://my.telegram.org/apps);
- Добавить значения в переменные окружения: TELEGRAM_API_ID, TELEGRAM_API_HASH, TELEGRAM_BASE_USERS (список пользователей, которые всегда будут во всех чатах, минимум - 2);
- После этого получить Auth Key используя команду `python manage.py telegram_auth_key` и полученную строку добавить в переменную окружения TELEGRAM_STRING_SESSION.
