# Провайдеры

## Инициализация Telegram

Для работы с провайдером Telegram необходимо:
- [Создать API id и API hash](https://my.telegram.org/apps);
- Добавить значения в переменные окружения: TELEGRAM_API_ID, TELEGRAM_API_HASH, TELEGRAM_BASE_USERS (список пользователей, которые всегда будут во всех чатах, минимум - 2);
- После этого получить Auth Key используя команду `python manage.py telegram_auth_key` и полученную строку добавить в переменную окружения TELEGRAM_STRING_SESSION.


## Инициализация Gitlab
Провайдер Gitlab позволяет давать доступ группам к конкретному проекту(ВАЖНО! пользователи которым дается доступ должны уже иметь аккаунт в gitlab-e)
Для работы с провайдером необходимо:
- [Создать](https://gitlab.com/-/profile/personal_access_tokens) личный токен owner-у проекта (желательно Expiration date очистить, чтобы токен был постоянный)
- Добавить токен в переменную окружения `GITLAB_PRIVATE_TOKEN`
- Если используется self-hosted gitlab в переменную окружения `GITLAB_API_HOST` добавить ссылку, по умолчанию https://gitlab.com
- Создать проект если еще не создан, и узнать project_id. `Setting -> General -> Project ID`
- При создании нового провайдера нужно определится с ролью, возможные значения можно подсмотреть [здесь](https://docs.gitlab.com/ee/api/members.html) или [здесь](gitlab/models.py)
