# Avito Ads Counter

## REST API, позволяющий следить за изменением количества объявлений в Авито по определённому поисковому запросу и региону.
Проект сделан по [тестовому заданию Avito Market Intelligeence](https://github.com/avito-tech/mi-backend-trainee-assignment).

Возможно применение для определения наиболее нагруженных запросов и регионов, а также для ведения другой статистической деятельности Avito и др.

## Стек технологий
- Python
- FastAPI
- Uvicorn
- PostgreSQL
- SQLAlchemy
- aiohttp
- BeautifulSoup4
- Scrapper API

## Обзор
### Особенности

- Код написан в асинхронном стиле. с применением asyncio и aiohttp.
- Веб-скраппинг Avito реализован через Scrapper API на бесплатном тарифе. Бесплатный тариф предлагает 5000 запросов в месяц, таким образом API поддерживает около 6 активных постоянно работающих ссылок

### Документация

Имеется два метода:

- POST /add. Принимает поисковую фразу и регион (слагом), вносит их в базу данных и возвращает id созданной записи.
  
Пример запроса:

Body
```
{
    "query": "геймпад",
    "region": "moskva"
}
```

Responce
```
{
    "id": 1
}
```

- GET /stat. Принимает на вход id связки поисковая фраза + регион и интервал, за который нужно вывести счётчики. Возвращает счётчики и соответствующие им временные метки (timestamp).
    
Пример запроса:

Body
```
{
    "id": 1,
    "start_datetime": "2023-11-24T10:00",
    "end_datetime": "2023-11-24T22:00"
}
```

Responce
```
{
    "id": 1,
    "stat": [
        {
            "quantity": 8869,
            "timestamp": "2023-11-24T11:06:53.212808"
        }
    ]
}
```
![image](https://github.com/romanov9617/avito_parsing/assets/129614130/6c3479dd-cbbe-4b1b-94a4-5bb49fb68437)

## Установка

Необходим Python 3.10+. Кроме того. необходим API Token для [Scrapper API](https://www.scraperapi.com/)
```sh
git clone https://github.com/romanov9617/avito_parsing.git.
python -m venv venv
venv/Scripts/Activate
pip install -r requirements.txt 
```

## Запуск локального сервера

```sh
python main.py
```

