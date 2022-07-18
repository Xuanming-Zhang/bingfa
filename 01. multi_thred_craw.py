import time

import blog_spider
import threading


def time_decorator(method_name):
    def outter(func):
        def wrapper():
            start = time.time()
            print(method_name+" starts")
            func()
            print(method_name+" ends")
            end = time.time()
            print("takes", end - start, "seconds")
        return wrapper
    return outter


@time_decorator("singel thread")
def single_thread():
    for url in blog_spider.urls:
        blog_spider.craw(url)


@time_decorator("multi thread")
def multi_thread():
    threads = []
    for url in blog_spider.urls:
        threads.append(threading.Thread(target=blog_spider.craw, args=(url,)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    single_thread()
    multi_thread()
    print("zhangxuanming")
    #aaa
