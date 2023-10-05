from threading import Thread
import time
import random
from threading import Lock


def foo(i):
    time.sleep(random.random() * 2)
    print('without lock', i)


def foo_lock(i, lock):
    time.sleep(random.randint(1, 2))
    lock.acquire()
    print('with lock:', i)
    lock.release()


def mutil_threading(count):
    t_list = []
    for i in range(0, count):
        t = Thread(target=foo, args=[i])
        t_list.append(t)
        t.start()

    for t in t_list:
        t.join()


def mutil_threading_lock(count):
    lock = Lock()
    t_list = []
    for i in range(0, count):
        t = Thread(target=foo_lock, args=[i, lock])
        t_list.append(t)
        t.start()

    for t in t_list:
        t.join()


if __name__ == '__main__':
    # mutil_threading(100)
    mutil_threading_lock(100)
    print('结束')
