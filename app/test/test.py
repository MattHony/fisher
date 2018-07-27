"""
   thread:线程实例的理解
"""

import threading
import time


def worker():
    print('i am thread')
    t = threading.current_thread()
    time.sleep(10)
    print(t.getName())

# 多线程  更充分的利用CPU的性能优势


new_t = threading.Thread(target=worker, name='qiyue-thread')
new_t.start()

t = threading.current_thread()
t.getName()
