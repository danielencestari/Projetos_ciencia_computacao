import time
from tech_news.database import create_news
import requests
from parsel import Selector  # seletor em geral é o css


def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3,
                                headers={"user-agent": "Fake user-agent"})
        response.raise_for_status()
    except (requests.ReadTimeout, requests.HTTPError):
        return None
    return response.text


def scrape_novidades(html_content):
    selector = Selector(html_content)
    list = []
    select = "a.cs-overlay-link::attr(href)"
    for url in selector.css(select):
        list.append(url.get())
    return list


def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page = "a.next ::attr(href)"
    for url in selector.css(next_page):
        return url.get()


def scrape_noticia(html_content):
    selector = Selector(html_content)
    url = selector.css("[rel='canonical']::attr(href)").get().strip()
    title = selector.css("h1.entry-title::text").get().strip()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("a.url::text").get()
    comments_count = len(selector.css(".comment-list li").getall())
    summary = selector.css(".entry-content > p:first-of-type *::text").getall()
    tags = selector.css(".post-tags a::text").getall()
    category = selector.css("span.label::text").get()

    return {
         'url': url,
         'title': title,
         'timestamp': timestamp,
         'writer': writer,
         'comments_count': comments_count,
         'summary': ''.join(summary).strip(),
         'tags': tags,
         'category': category
     }


def get_tech_news(amount):
    url = 'https://blog.betrybe.com'
    next_url = '/'
    notices = []

    content = fetch(url)
    if content is not None:
        while next_url:
            url_news = scrape_novidades(content)
            for url_new in url_news:
                content_new = fetch(url_new)
                notices.append(scrape_noticia(content_new))
                if len(notices) >= amount:
                    create_news(notices)
                    return notices
            next_url = scrape_next_page_link(content)
            content = fetch(next_url)
    create_news(notices)
    return notices
