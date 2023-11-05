# testing

https://github.com/Nicodde/testing.git

1. Клонируйте репозиторий:

   >`git clone https://github.com/Nicodde/testing.git`

2. Перейдите в директорию проекта:

    >`cd <название_директории>`


## issue-01

Doctest тесты для функции `encode()`.
Чтобы запустить тесты, введите в терминале команду:

    python -m doctest -o NORMALIZE_WHITESPACE -v issue_01.py

Также можно просто запустить файл - необходимые флаги уже прописаны в файле.

## issue-02

Tесты для функции `decode()`, которые проводятся с помощью `pytest.mark.parametrize`.

Для запуска необходим пакет `pytest`. Его можно установить с помощью следующей команды:

    pip install pytest

Чтобы запустить тесты, введите в терминале команду:

    python -m pytest -v issue_02.py

## issue-03

Тесты для функции `fit_transform()` с использованием `unittest`.

Чтобы запустить тесты, введите в терминале команду:

    python -m unittest -v issue_03.py

## issue-04

Тесты для функции `fit_transform()` с использованием `pytest`.

Для запуска необходим пакет `pytest`. Его можно установить с помощью следующей команды:

    pip install pytest

Чтобы запустить тесты, введите в терминале команду:

    python -m pytest -v issue_04.py

## issue-05

Тесты для функции `what_is_year_now` с использованием замены реального обращения к API через `unittest.mock`, 100% покрытием и отчетом о покрытии в виде директории с html файлами.

Для запуска необходимы пакет `pytest`. Его можно установить с помощью следующей команды:

    pip install pytest

Чтобы запустить тесты, введите в терминале команду:

    python -m pytest -v -s issue_05.py

Чтобы посмотреть процент покрытия, введите в терминале команду:

    python -m pytest -q issue_05.py --cov=issue_05

Чтобы создать html отчет, введите в терминале команду:

    python -m pytest -q issue_05.py --cov=issue_05 --cov-report html
