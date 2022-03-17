import threading
from time import time, sleep
from threading import Thread, Lock

numbers = [2139079, 1214759, 1516637, 1852285]


def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i


start = time()
for number in numbers:
    list(factorize(number))
end = time()
print('Took %.3f seconds' % (end - start))


class FactorizeThread(Thread):
    def __init__(self, number):
        super().__init__()
        self.factors = None
        self.number = number

    def run(self):
        self.factors = list(factorize(self.number))


start = time()
threads = []
for number in numbers:
    thread = FactorizeThread(number)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
end = time()
print('Took %.3f seconds' % (end - start), "to do this with threads\n\n")


"""def wait():
    count = 0
    while True:
        print(count)
        count += 1
        sleep(2)"""


"""t1 = threading.Thread(target=wait, name='Wait 1', daemon=True)
t1.start()
print((threading.enumerate())[1].is_alive())
print(t1.name, "\n")

t2 = threading.Thread(target=wait, name='Wait 2', daemon=True)
t2.start()
print((threading.enumerate())[1].is_alive())
print(t2.name)"""


def wait_2():
    sleep(2)
    print("finished")


class MyThread(threading.Thread):
    def __init__(self, target, name='MyThread'):
        super().__init__()
        self.target = target
        self.name = name

    def run(self):
        self.target()


t = MyThread(wait_2)
t.start()
print(t.name, "\n")

c = 0
lock = Lock()


def count_30000():
    global c
    lock.acquire()
    try:
        while c < 30000:
            c += 1
        print(c)
    finally:
        lock.release()


def count_100000():
    global c
    x = 340
    lock.acquire()
    try:
        while c < 100000:
            c += 1
        print(c)
    finally:
        lock.release()


t_0 = Thread(target=count_30000, name='30000', daemon=True)
t_0.start()

t_1 = Thread(target=count_100000, name='100000')
t_1.start()
