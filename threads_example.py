from time import time
from threading import Thread

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
print('Took %.3f seconds' % (end - start))
