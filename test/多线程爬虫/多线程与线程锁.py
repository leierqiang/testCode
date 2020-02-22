import threading
import time

tickets = 0


def get_ticks():
    global tickets
    for i in range(10000000):  # 数小时正常，大了才能看到快慢对比
        tickets += 1
    print('tickets:%s' % (tickets))


def main():
    for i in range(3):  # 这3个线程在同时运行，修改变量的顺序不确定
        t = threading.Thread(target=get_ticks)
        t.start()


if __name__ == '__main__':
    """
    Python的多线程是在一个进程中，共享(变量)资源,不能保证先后顺序,因此需要线程锁
    """
    main()
# 应该是10000000 20000000 30000000，结果有时候是有时不是，原因是进程中的线程都是共享变量
# tickets:11742514
# tickets:11913719


# import threading
#
# tickets = 0
# gLock = threading.Lock()
#
# def get_ticks():
#     global tickets
#     gLock.acquire()  #加线程锁
#     for i in range(10000000):  # 数小时正常，大了才能看到快慢对比
#         tickets += 1
#     gLock.release()  #解线程锁
#     print('tickets:%s' % (tickets))
#
#
# def main():
#     for i in range(3):
#         t = threading.Thread(target=get_ticks)
#         t.start()
#
#
# if __name__ == '__main__':
#     """
#     Python的多线程是在一个进程中，共享(变量)资源,不能保证先后顺序,因此需要线程锁
#     """
#     main()
#
# # tickets:10000000
# # tickets:20000000
# # tickets:30000000
