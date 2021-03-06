# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/7/25 16:47
# @Author : '红文'
# @File : book.py
# @Software: PyCharm

# 验证层
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
