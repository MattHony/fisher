# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/7/26 21:28
# @Author : '红文'
# @File : test2.py
# @Software: PyCharm
import threading
from werkzeug.local import LocalStack
import time

my_stack = LocalStack()
my_stack.push(1)
print('in main threading before push, value is ' + str(my_stack.top))


def worker():
    # 新线程
    print('in new thread before push,value is ' + str(my_stack.top))
    my_stack.push(2)
    print('in new thread after push,value is ' + str(my_stack.top))


new_t = threading.Thread(target=worker, name='qiyue-thread')
new_t.start()
time.sleep(2)

# 主线程
print('finally, the main thread value is' + str(my_stack.top))
