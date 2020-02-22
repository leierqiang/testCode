import threading
import time

def coding():
    for i in range(3):
        print("c"*30)
        time.sleep(1)


def drawing():
    for i in range(3):
        print("d"*30)
        time.sleep(1)

def main():
    # start_time =  time.time()
    t1 = threading.Thread(target=coding)  # 注:coding()就是一般的线性，coding是调用多线程
    t2 = threading.Thread(target=drawing)
    t1.start()
    t2.start()
    # end_time = time.time()
    # print(str(end_time - start_time))
    # return str(end_time - start_time)

if __name__ == '__main__':
    main()
    # time_all = main()
    # print("总时间=%s" % (time_all))
