# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/7/25 15:23
# @Author : '红文'
# @File : __init__.py
# @Software: PyCharm
from flask import Blueprint


# 蓝图 blueprint
web = Blueprint('web', __name__)


from app.web import book
from app.web import user
