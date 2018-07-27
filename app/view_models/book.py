# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/7/27 21:34
# @Author : '红文'
# @File : book.py
# @Software: PyCharm


class BookViewModel:
    def package_single(self, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = 1
        pass

    def package_collection(self, keyword):
        pass

    def __cut_book_data(self, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'],
            'author': '、'.join(data['author']),
            'price': data['price'],
            'summary': data['summary'],
            'image': data['image']
        }
        pass
