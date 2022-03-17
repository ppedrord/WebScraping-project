"""import threading
from time import time, sleep
from threading import Thread, Lock
import imdbGenreSpider"""


if __name__ == '__main__':

    import time; start = time.time()

    number_threads = 5
    list_threads = list()
    list = imdbGenreSpider.creating_targets()
    for i in range(number_threads):
        list_pages = imdbGenreSpider.divide_work(list, i, number_threads)
        thread = threading.Thread(name=str(i), target=imdbGenreSpider.finding_movie_data)
        list_threads.append(thread)

    for t in list_threads:
        t.start()

    for t in list_threads:
        t.join()

    print(time.time()-start)

