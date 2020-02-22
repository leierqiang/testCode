"""
多线程爬虫的生产者与消费者之间用多线程联系

"""

# lock版本的

import threading
import random
import time

gMoney = 1000
gLock = threading.Lock()

# 通过gTimes控制



class Procuer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(100, 1000)
            gLock.acquire()
            gMoney += money
            gLock.release()
            print("线程%s产生了%s的money,剩余%s的money\n" % (threading.current_thread(), money, gMoney))
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(100, 1000)
            gLock.acquire()
            gMoney -= money
            if gMoney <= 0:
                break
            gLock.release()
            print("线程%s消费了%s的money,剩余%s的money" % (threading.current_thread(), money, gMoney))
            time.sleep(0.5)


def main():
    for i in range(2):
        t = Procuer()
        t.start()

    for i in range(2):
        t = Consumer()
        t.start()


if __name__ == '__main__':
    main()
