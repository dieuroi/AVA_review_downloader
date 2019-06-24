from getreviews import *
import threading


class Crawler(threading.Thread):
    def run(self):
        while True:
            pic_id = queue.get()
            downloadingreviews(pic_id)
            time.sleep(1)


def multiprocess(num):
    for i in range(num):
        c = Crawler()
        c.start()


if __name__ == '__main__':
    genRe()
    readfile('AVA.txt', 0)
    multiprocess(15)