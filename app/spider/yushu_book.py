from app.libs.httper import Http
from flask import current_app


class YuShuBook:
    # per_page = 15
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&start={}&count={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = Http.get(url)
        # 返回result为json格式的dict
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        # url = cls.isbn_url.format(keyword, cls.per_page, (page-1)*cls.per_page)
        url = cls.isbn_url.format(keyword, current_app.config['PER_PAGE'], cls.calculate_start(page))
        result = Http.get(url)
        return result

    @staticmethod
    def calculate_start(page):
        return (page-1)*current_app.config['PER_PAGE']
