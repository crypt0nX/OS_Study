import time
import threading
from threading import Semaphore
import random

writerMutex = Semaphore(1)  # 对于资源控制的互斥信号量
readerMutex = Semaphore(1)  # 对于计数器的互斥信号量
readerCount = 0
sleepTime = 1


def reader(num):
    print('reader' + str(num) + ' waiting to read\n', end='')
    readerMutex.acquire()
    global readerCount
    if readerCount == 0:
        writerMutex.acquire()
    readerCount += 1
    readerMutex.release()
    print('reader' + str(num) + ' reading\n', end='')
    time.sleep(sleepTime)
    print('reader' + str(num) + ' finish read\n', end='')
    readerMutex.acquire()
    readerCount -= 1
    if readerCount == 0:
        writerMutex.release()
    readerMutex.release()


def writer(num):
    print('writer' + str(num) + ' waiting to write\n', end='')
    writerMutex.acquire()
    print('writer' + str(num) + ' writing\n', end='')
    time.sleep(sleepTime)
    print('writer' + str(num) + ' finish write\n', end='')
    writerMutex.release()


if __name__ == '__main__':
    times = 10
    readerWriterIndex = []
    for _ in range(times):
        readerWriterIndex.append(random.randint(0, 1))
    print(readerWriterIndex)
    readerIndex = 1
    writerIndex = 1
    for i in readerWriterIndex:
        if i == 1:
            t = threading.Thread(target=reader, args=(readerIndex,))
            readerIndex += 1
            t.start()
        else:
            t = threading.Thread(target=writer, args=(writerIndex,))
            writerIndex += 1
            t.start()
