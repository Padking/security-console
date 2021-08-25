# Security console
Урок № 1 модуля "Знакомство с Django: ORM" от devman

## Описание

Пульт охраны банка


### Особенности

* отображает на страницах сайта таблицу:
  + активных карточек
  + о состоянии хранилища с частотой обновления информации 1 раз в ~10 секунд
  + о подозрительных посещениях по конкретной карточке

### Используемые технологии

* Django
* psycopg2

### Требования к окружению

* Python 3.7 и выше,
* Linux/Windows,
* Переменные окружения (ПеО).

Проект настраивается через ПеО, достаточно указать их в файле `.env`.
Передача значений ПеО происходит с использованием [environs](https://pypi.org/project/environs/).

#### Параметры проекта

|       Ключ        |     Значение     |   По умолчанию   |
|-------------------|------------------|------------------|
|`ALLOWED_HOSTS`| Разрешённые хосты |`['0.0.0.0', '127.0.0.1', 'localhost']`|
|`DEBUG`| Режим отладки |`False`|
|`DJANGO_SETTINGS_MODULE`| Файл `manage.py` |`project.settings`|
|`SECRET_KEY`| Уникальное непредсказуемое значение |-|

#### Параметры подключения к БД

По умолчанию, используется СУБД PostgreSQL.

|       Ключ        |     Значение     |   По умолчанию   |
|-------------------|------------------|------------------|
|`DB_ENGINE`| Имя движка СУБД | - |
|`DB_PSQL_HOST`| Адрес СУБД | - |
|`DB_PSQL_PORT`| Порт СУБД | - |
|`DB_PSQL_NAME`| Имя БД | - |
|`DB_PSQL_USER`| Имя пользователя БД | - |
|`DB_PSQL_USERPASSWORD`| Пароль пользователя БД | - |


### Установка

```bash
git clone https://github.com/Padking/security-console.git  # клонирование проекта
cd security-console
```
`mkvirtualenv -p` <path> <virtualenv's_name>  # создание каталога виртуального окружения (ВО)*

`setvirtualenvproject` <virtualenv's_path> <project's_path>  # связывание каталогов ВО и проекта
```bash
pip install -r requirements.txt # установка зависимостей
cd django-orm-watching-storage
python manage.py runserver 0.0.0.0:8000  # запуск скрипта
```

### Пример запуска

```
$ python manage.py runserver 0.0.0.0:8000
Performing system checks...

System check identified no issues (0 silenced).
August 18, 2021 - 15:24:28
Django version 1.11.29, using settings 'project.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
```

\* с использованием [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/index.html)
