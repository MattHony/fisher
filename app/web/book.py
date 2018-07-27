from flask import jsonify, request

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key

from app.spider.yushu_book import YuShuBook
from . import web


# @web.route('/book/search/<q>/<page>')
@web.route('/book/search')
def search():
    """
        q :普通关键字 （keyword) isbn
        page
    """
    # 第一种方式 验证方法q,page
    # q = request.args['q']
    # page = request.args['page']
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()     # strip()除去q前后存在空格
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
        return jsonify(result)
    else:
        return jsonify(form.errors)
    # return json.dumps(result), 200, {'content-type': 'application/json'}
