from queue import Queue
import threading
import time


class System(object):
    def __init__(self):
        self.bufferSize = 10
        self.buffer = Queue(self.bufferSize)
        self.count = 1

    def producer(self, name):
        while True:
            self.buffer.join()  # 等待task_done()发送信号
            self.buffer.put(self.count)
            print("%s正在写第%d个产品\t" % (name, self.count))
            self.count += 1
            time.sleep(0.1)

    def customer(self, name):
        while True:
            x = self.buffer.get()
            print("\t%s正在取第%d个产品\t" % (name, x))
            self.buffer.task_done()  # 取完后发送信号
            time.sleep(1)


if __name__ == '__main__':
    system = System()
    t1 = threading.Thread(target=system.producer, args=("生产者",))
    t2 = threading.Thread(target=system.customer, args=("消费者",))
    t1.start()
    t2.start()
