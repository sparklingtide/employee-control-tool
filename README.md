# Employee Management Tool

## Развертывание dev-окружения

### Установка на чистую систему

1. Необходим установленный python3.10, для управления зависимостями используется [poetry](https://python-poetry.org/docs/#installation)
2.
    ```shell
    $ poetry install --no-root
    $ poetry shell
    ```
3. Так же необходимо установить и настроить PostgreSQL (предпочтительная версия — 14). После установки и настройки ресурсов (например, БД в Postgres) требуется вписать доступы от сервисов в файл `.env` (либо же указать в переменных среды другим способом). Доступные для редактирования переменные с примерами значений можно посмотреть в файле `.env.template`.
4.
    ```shell
    $ pre-commit install
    ```

### docker-compose

```shell
  $ make compose-up
  $ make compose-enter
  $ make runserver
```

Для остановки окружения:

```shell
  $ make compose-down
```

`make compose-enter` открывает новый шелл внутри app-контейнера (например, для миграций, или же запуска `./manage.py shell_plus` для дебага)

## Git workflow

У проекта есть одно окружение — [emt.sparklingtide.dev](emt.sparklingtide.dev), которое на текущий момент является dev-окружением. Оно соответствует ветке master (все обновления на этой ветке автоматически выкатываются сюда)

Все новые фичи разрабатываются в отдельных ветках, МРы отправляются другим участникам команды на ревью, после одного ревью можно сливать в master и передавать фронту/выкатывать на стейдж и т.д.

## Code Style

Задается пресетами isort/black/flake8, единственное, что требуется сделать — установить pre-commit hook:

```shell
pre-commit install
```

Соответствие правилам проверяется в пайплайнах мерж-реквестов и в ветке dev.

## Предостережения

- не стоит редактировать файл `settings.py` напрямую: если необходимо изменить какие-то уже существующие значения, это можно сделать редактированием переменных окружения в файле `.env`
