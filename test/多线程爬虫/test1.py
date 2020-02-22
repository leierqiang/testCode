import threading
import time


# 继承一个方法就能实现线程管理
class CodingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print('%s正在执行第%s个线程'%(threading.current_thread(), x))
            time.sleep(1)

def main():
    t1 = CodingThread()
    t1.start()


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(str(end_time - start_time))

# <CodingThread(Thread-15, started 12860)>正在执行第0个线程
# <CodingThread(Thread-15, started 12860)>正在执行第1个线程
# <CodingThread(Thread-15, started 12860)>正在执行第2个线程