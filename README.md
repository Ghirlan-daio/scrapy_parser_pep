# Асинхронный парсер PEP

### Над проектом работал: Dmitry Stepanov [Ghirlan-daio](https://github.com/Ghirlan-daio)

Парсер собирает информацию о статусах документов PEP (оф. страница: https://peps.python.org/) и выводит результат в два csv-файла:
- в первом находится список всех документов PEP — их номер, название и статус;
- во втором содержится информация о количестве документов PEP в каждом статусе.

### Парсер реализован на базе фреймворка **Scrapy**.

## Подготовка к запуску парсера
#### Клонируйте репозиторий и перейдите в него:

```git clone git@github.com:Ghirlan-daio/scrapy_parser_pep.git```

```cd scrapy_parser_pep```

#### Создайте и активируйте виртуальное окружение:

```python -m venv venv```

```source venv/Scripts/activate```

#### Установите зависимости проекта:

```pip install -r requirements.py```

## Запуск парсера

```scrapy crawl pep```