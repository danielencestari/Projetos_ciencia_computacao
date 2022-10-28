from datetime import datetime
from tech_news.database import search_news


def search_by_title(title):
    by_title = []
    query = ({"title": {"$regex": f"{title.lower()}"}})
    news = search_news(query)
    for new in news:
        by_title.append((new["title"], new["url"]))
    return by_title


def search_by_date(date):
    format = '%d/%m/%Y'
    by_date = []
    try:
        input = datetime.fromisoformat(date)
        formated_date = datetime.strftime(input, format)
        news = search_news({"timestamp": formated_date})
        for new in news:
            by_date.append(tuple([new['title'], new['url']]))
        return by_date
    except ValueError:
        raise ValueError('Data inválida')


def search_by_tag(tag):
    by_tag = []
    query = {"tags": {"$regex": f"{tag}", "$options": "i"}}
    news = search_news(query)
    for new in news:
        by_tag.append((new["title"], new["url"]))
    return by_tag


def search_by_category(category):
    by_category = []
    query = {"category": {"$regex": f"{category}", "$options": "i"}}
    news = search_news(query)
    for new in news:
        by_category.append((new["title"], new["url"]))
    return by_category
